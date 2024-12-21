'''
        독립적 DAG 유지해야 하므로 DAG 안의 task 단위 호출 방안 모색
        ExternalTaskSensor 사용이유
        - 상위 dag의 상태에 따라 하위 dag 실행을 위함
        - 특징 : 부모 dag가 완료될 때까지 시작하지 않고 대기
        - 여러 업스트림의 dag 및 task에 의존성 생성 할 수 있으며, 호출해야 하는 dag가 추가된다 하더라도 기존의 업스트림 dag를 수정할 필요가 없기 떄문
         - 하위 새로 생겨나는 dag에 추가하는 방식
         - 현재 구조에서는
            - DAG1 >> DAG2 >> DAG4
            - DAG1 >> DAG3
            방식으로 수행 되도록
         - Upstream 의 상태값 여부에 따라 하위 dag 실행 할 수 있는 이점 있음
            DAG2, DAG3 에 ExternalTaskSensor 적용

         DummyOperator 사용 이유
         임시 operator


'''

from airflow import DAG
from airflow.operators.sensors import ExternalTaskSensor
from airflow.operators.dummy import DummyOperator

from datetime import datetime, timedelta

start_date = datetime(2024, 11, 1)
default_args = {
    'owner': 'Analytics',
    "email": ["xxxx@gmail.com"],
    "email_on_failure": True,
    'depends_on_past': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=10),
    'trigger_rule': "all_success",
}


# ### DAG1 ####
with DAG(
        dag_id='loading_raw_data',
        default_args=default_args,
        description='loading_raw_data',
        schedule_interval='30 3 * * *',
        start_date=datetime(2024, 11, 1),
        catchup=False,
) as dag1:
    loading_raw_data_task = DummyOperator(
        task_id='loading_raw_data_task'
    )
    loading_raw_data_task


# ### DAG2 ####
with DAG(
        dag_id='aggregate_data',
        default_args=default_args,
        description='aggregattion_row_data',
        schedule_interval='* 7 * * *',  # 상위 dag 와 동일하게 설정
        start_date=datetime(2024, 11, 1),
        catchup=False,
) as dag2:

    dag2_sensor = ExternalTaskSensor(
        task_id='wait_for_loading_raw_data_task',
        external_dag_id='loading_raw_data',
        external_task_id='loading_raw_data_task',
        allowed_states=['success'],     # 대기해야하는 upstream dag의 상태
        start_date=start_date,
        execution_delta=timedelta(hours=3, minutes=30),     # 3시간 30분전에 시작한 Dag(loading_raw_data) 확인
        mode='reschedule',  # dag1 의 loading_raw_data_task 가 완료 될 때 까지 up_for_reschedule 상태로 대기 상태
        timeout=3600,       # task의 최대 대기 실행 시간. 초 단위
    )

    aggregate_data_task = DummyOperator(
        task_id='aggregate_data_task'
    )
    dag2_sensor >> aggregate_data_task


# ### DAG3 ####
with DAG(
        dag_id='independent_task',
        default_args=default_args,
        description='independent_row_data',
        schedule_interval='15 6 * * *',
        start_date=datetime(2024, 11, 1),
        catchup=False,
) as dag3:
    dag2_sensor = ExternalTaskSensor(
        task_id='wait_for_loading_raw_data_task',
        external_dag_id='loading_raw_data',
        external_task_id='loading_raw_data_task',
        allowed_states=['success'],  # 대기해야하는 upstream dag의 상태
        start_date=start_date,
        execution_delta=timedelta(hours=2, minutes=45),  # 2시간 45분 전에 시작한 Dag(loading_raw_data) 확인
        mode='reschedule',  # dag1 의 loading_raw_data_task 가 완료 될 때 까지 up_for_reschedule 상태로 대기 상태
        timeout=3600,  # task의 최대 대기 실행 시간. 초 단위
    )

    independent_task = DummyOperator(
        task_id='independent_task'
    )
    dag2_sensor >> independent_task


# ### DAG4 ####
with DAG(
        dag_id='making_daily_report',
        default_args=default_args,
        description='making_daily_report',
        schedule_interval='30 7 * * *',
        start_date=datetime(2024, 11, 1),
        catchup=False,
) as dag4:

    dag2_sensor = ExternalTaskSensor(
        task_id='wait_for_loading_raw_data_task',
        external_dag_id='aggregate_data',
        external_task_id='aggregate_data_task',
        allowed_states=['success'],  # 대기 해야 하는 upstream dag의 상태
        start_date=start_date,
        execution_delta=timedelta(minutes=30),  # 30분전에 시작한 Dag(aggregate_data) 확인
        mode='reschedule',  # dag1 의 loading_raw_data_task 가 완료 될 때 까지 up_for_reschedule 상태로 대기 상태
        timeout=3600,  # task의 최대 대기 실행 시간. 초 단위
    )

    making_daily_report_task = DummyOperator(
        task_id='making_daily_report_task'
    )
    dag2_sensor >> making_daily_report_task
