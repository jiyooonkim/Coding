
 < spark sql 버전>

 a.
 select drivers.* total_distance_km
 from
  (select user_id, sum(distance_km) as total_distance_km
  from  trip_logs 
  where 
	trip_status = 'completed' 
    and traffic_conditions='혼잡' 
    and  add_months(trip_start_time, -6) 
    and  total_distance_km >=50
  group by user_id ) as recently_trip_logs, drivers
  where recently_trip_logs.user_id = drivers.user_id
  ;
  
b.  트럭 운전자중 가장 많이 방문한(destination) 찾고 -> 운전자 기본정보 찾기
  
--  SELECT *
--  /*+ BROADCASTJOIN */  drivers.region, drivers.destination, count(drivers.destination)
--  FROM vehicle_info
--  JOIN  trip_logs
--  JOIN drivers
--  ON vehicle_info.vehicle_id = trip_logs.vehicle_id
--	and drivers.user_id = trip_logs.user_id
--  where trip_status = 'completed' and model_type = 'TRUCK'
--  group by drivers.region;
  
  

select region, destination, count(destination)
from
    vehicle_info vch_inf, trip_logs trp_log, drivers drv
where
    trp_log.trip_status = 'completed'
    and vch_inf.model_type = 'TRUCK'
    and trp_log.user_id = drv.user_id
    and trp_log.vehicle_id = vch_inf.vehicle_id
group by region
order by  count(destination) desc  limit 1
;


c.
select vch_inf.*
from
    vehicle_info as vch_inf
right join
broadcast
    (
        select user_id , sum(distance_km)
        from
            trip_logs
        group by user_id
        order by sum(distance_km) desc limit 5
    ) as top_user
on top_user.user_id = vch_inf.user_id


  
  

2-a.
- drivers 과 vehicle_info join 이후  trip_logs join 하려고 하였으나
 join 대상 컬럼이 없음 ->운전자별 소유 차량 정보 테이블 있었으면 좋겠음
- partition 전략
trip_logs 테이블 partition 컬럼 생성
- 데이터 압축
  parquet snappy compression


2-b.
- bloomFilterJoin
spark.sql.bloomFilterJoin.enabled=true
bloomFilter join 역할: 사전에 작성된 filter(where절)을 먼저 수행후 join 하므로 성능에 향상 기대 효과
- optimized join
spark.sql.optimizer.sizeBasedJoinReorder.enabled=true
optimized join 역할 : 테이블 순서를 필터, 규모에 따라 재정의
원래 spark join 방식은 작은것 부터 큰 순서대로 수행
작은 규모부터 join시 셔플링 비용 최소화
- broad cast join
optimized join 역할 : join 테이블 편차가 심할 떄 사용
작은 테이블을 "broadcast(작은테이블)" 으로 사용
- 적당한 excutor, core 할당
- cache 사용(클러스터 메모리 효율적인 사용 목적)
 자주 사용되는 쿼리 (위 테이블에서는 trip_status 가 'completed' ) 조건절 쿼리를 캐쉬에 넣어두고 필요할 때마다 호출




필수 과제 2번
1. EMR 클러스터의 설정을 어떻게 조정해야 하는지 구체적으로 설명해주세요.(예: Spark 설정 파라미터, 클러스터 구성 등)
물리메모리 초과 원인 : 할당된 메모리 값보다 더 많은 인스턴스 요구 되는 상황
EMR에서 spark 작업 할당은 spark-defaults.conf를 기본으로 실행하나 대량 작업 요구시 더 많은 excutor, core 개수 할당 필요로함, sparkContext를 On-demand 로 직접 할당 가능
- 메모리 부족시 해결 방안
shuffle partition 수 조정 : 골고루 분산 될 수 있는 방향으로 우선 생각
menory 향상 : 하나의 코어당 사용할 수 있는 메모리 증설
core 향상
* 무조건적인 core, memory 부터 향상시킨다면 전반적인 클러스터 사용율 올라감, 다른 작업을 대기 시간이 길어지거나 spark 강제 종료 등의 현상이 일어날 수 있음
쿼리 기반 튜닝 -> partition -> memory -> core 순으로 최적화 하는 방향 지향

- spark 구성 파라미터
spark.excutor.memory : 작업 실행하는 각 excutor 에 대한 메모리 크기
spark.excutor.core : 각 excutor에 할당되는 코어개수
spark.driver.memory : diver 메모리 크기
spark.driver.core : 각 diver에 사용될 코어 수
spark.sql.shuffle.partitions : join, group by 등 연산 수행시 shuffle partition 개수 할당(partition 또는 task 수 할당 됨)
spark.shuffle.compress : 맵 출력이 압축되어 공간을 절약
spark.dynamicAllocation.enabled : 리소스 동적할당 역할,
최대/최소 excutor 할당 가능 그 안에서 작업 부하에 따라 애플리케이션에 할당된 실행자(excutor 단위) 수 유연하게 사용가능,
 특정 어플리케이션에서 extuor 독점하게 될 우려도 있어 모니터링 필수,
spark.shuffle.service.enabled : 외부 셔플 서비스 활성화 , spark.dynamicAllocation.enabled과 동적할당 위해 함께 사용
- 클러스터 구성
{
"Name":"AmazonEMRMaster",
    "Configurations" : [
        {
        "Classification": "spark-defaults",
        "Properties": {
            "spark.driver.memory": "14g",
            "spark.driver.core": "8",
            "spark.driver.memoryOverhead": "1g",
            "spark.excutor.memory": "14g",
            "spark.excutor.core": "8",
            "spark.executor.memoryOverhead": "1g",
            "spark.sql.shuffle.partitions": "500",
            "spark.shuffle.compress": "true",
            "spark.dynamicAllocation.enabled": "true",
            "spark.shuffle.service.enabled": "true"
         }
        }
    ]
}
* 참고
- Spark Driver.*는 Spark 애플리케이션의 중앙 제어 역할, client 또는 cluster 여부에 따라 달라짐
- Spark Executor.*는 각 워커 노드에서 작업을 실행 하는 역할


2.이 오류가 발생한 원인을 분석하고, 이를 해결하기 위한 방안을 제시해주세요.
- 파일은 있으나 s3 접근 권한 없어서 읽지 못할 경우 발생
- 해결방안
    - S3 버킷에 읽기 액세스를 차단할 수 있는 버킷 정책 제한이 있는지 확인 필요(s3:ListAllMyBuckets, s3:GetBucketLocation, s3:ListBucket 등 사용자 권한 부여)
    - IAM 권한 설정 :  Amazon S3 버킷에서 리소스 기반 정책을 테스트
    예시 >
        {
            "Version": "2024-11-29",
            "Statement": [
                {
                    "Sid": "user1 만 my-bucket 버킷 접근, 가져오기 가능",
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:iam::0001:user/user1"
                    },
                    "Action": [
                        "s3:ListBucket",
                        "s3:ListAllMyBuckets",
                        "s3:GetBucketLocation",
                        "s3:GetObject",
                    ],
                    "Resource": "arn:aws:s3:::my-bucket"
                }
            ]
        }

데이터 접근 권한 및 S3 경로 설정 에서의 주의사항을 설명해주세요.
- s3 버킷에 익명 엑세스 권한 부여 : 익명 엑세스 권한 부여시 모두(전세계, 제한없이) 접근 가능
- 객체 소유권 : ACL을 비활성화로 해당 계정에서 IAM 사용자 추가해 사용자별 접근 가능하도록
(*참고, ACL을 활성화시 타 계정으로도 접근 가능함, 보안을 위해 객체마다 접근 권한 부여 방식)
- 버킷 퍼블릭 엑세스 차단 설정 : 외부에서 읽지 못하도록 설정, 경우에 따라 차단 할 경우 "모든 퍼블랙 엑세스차단"을 비활성화 하고 옵션 단위 선택
- 업무 보안을 위해 모든 엑세스 차단 또는 ACL 이용하여 차단 지향
- 버킷 접근 제어 방법
    - 버킷 정책 vs IAM 정책
        - 리소스기반 제어(버킷 단위 제어) : 해당 버킷에 권한 가진 사용자만 객체에 접근 가능
        - 사용자기반 제어(IAM 제어) : IAM 계정에서 s3 접근 권한(policy) 설정 통해 사용자 단위로 접근 허용 또는 거부


- 주의사항
    - Bucket(버킷) : Region 단위 중복 이름 사용 불가, 하나의 계정당 최대 100개 버킷 생성 가능
                    버킷 소유권 이전 불가
                    버킷안에 버킷 생성 불가
    - Object(객체) : 모든 데이터, 파일


3. 장애를 예방하기 위한 모니터링 및 알림 시스템을 제안해주세요.
(예: CloudWatch, SNS 알림, EMR 자체 모니터링 툴 등을 활용한 장애 감지 및 대응 방법)
장애가 발생하기 전에 사전에 문제를 발견할 수 있는 전략을 설명해주세요.
- 시스템 모니터링 알림
    목적 : CPU 사용율, 디스크 I/O 및 네트워크 사용률 실시간 모니터링 대응 및 개선 목적
    사용 기술 : CloudWatch(경보 알림 설정), SNS(이메일 수신 알림용)
- EC2 리소스 모니터링
    목적 : CloudWatch 콘솔 대시보드로 인스턴스 상태(메모리 사용율, 파일 시스템 손상, 커널 등) 제공 및 알람
    사용 기술 : CloudWatch
- EMR 모니터링
    목적 : 클러스터 내 진행상황 추적, 유휴 클러스터 확인, 노드 저장소 부족, 스토리지 부족 등 미리 알림으로 받아
    CloudTrail을 통해 Amazon EMR 호출 규칙 생성 후 대응
    사용 기술 : CloudTrail, CloudWatch

- CloudWatch 대시보드, 경보 사용
    - 일정 수치 이상의 시스템 사용율, 위험도에 따른 알림 사전 발생

- EventBridge : 이벤트 로그에 따라 조치 규칙 구성으로 대응



필수 과제 3번
airflow.py

필수 과제 4번
 개인식별정보 처리
 실시간 데이터 7일치 처리
 비식별화 데이터로만 월간 집계 데이터

1&2. 데이터 접근 권한 설정
방법1
- 컬럼단위 접근권한 설정
AWS Lake Formation 에서 Athena 쿼리 사용하여 Amazon S3 접근할 떄 적용됨
Table 에 Column 단위 접근 권할 설정 가능 AWS Lake Formation > Data Permission > Grant 탭에서
IAM 사용자 및 역할에 대해 접근 할 수 있도록 설정 가능
테이블에서 제외할 열 선택 가능 (개인식별 정보:user_name, date_of_birth, gender)
- EMR, Glue, Athena 에서도 동일한 방법으로 정책 사용 가능

방법2
- 컬럼 단위 암호화 사용으로 별도 테이블 제공
    개인식별정보는 암호화
    개인 식별정보 필요한 경우(마케팅팀) 복호화 하여 사용
    비식별 데이터만 사용할 경우 암호화 된 데이터 그대로 사용 하거나 개인식별 정보는 제외 후 재식별화 하여 사용



2. 데이터 마트 구조 설계
방법2. 운영과 마케팅 공통 제공
CREATE EXTERNAL TABLE `presonal_campaign`(
    user_id BIGINT,
    user_name VARCHAR(100),
    date_of_birth DATE,
    gender VARCHAR(10),
    address VARCHAR(50),
    regist_date TIMESTAMP,
    subscription_type VARCHAR(30), -- 예 : 무료 , 유료 , 프리미엄
    active_user BOOLEAN,
    trip_id BIGINT,
    vehicle_id BIGINT,
    trip_start_time TIMESTAMP,
    trip_end_time TIMESTAMP,
    origin VARCHAR(100),
    destination VARCHAR(100),
    distance_km DOUBLE,
    average_speed_kmh DOUBLE,
    fuel_consumed_liters DOUBLE,
    traffic_conditions VARCHAR(100),
    trip_status VARCHAR(100),
    reg_dt TIMESTAMP
  )
 partitioned by (
     part_year string,
     part_month string,
     part_day string,
     part_hour string,
     part_minute string
 )
STORED AS INPUTFORMAT
    'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
    'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
    's3://xxxx.xxxxx.xx/presonal_campaign/'



방법1. 운영과 마케팅 별도 제공
## 마케팅팀 제공
CREATE TABLE presonal_campaign(
    user_id BIGINT,
    user_name VARCHAR(100),
    date_of_birth DATE,
    gender VARCHAR(10),
    trip_start_time TIMESTAMP,
    trip_end_time TIMESTAMP,
    reg_dt TIMESTAMP comment '데이터삽입시간',
    destination VARCHAR(100)
);

## 운영팀 제공
CREATE TABLE month_aggretation(
    user_id BIGINT,
    trip_id BIGINT,
    vehicle_id BIGINT,
    trip_start_time TIMESTAMP,
    trip_end_time TIMESTAMP,
    origin VARCHAR(100),
    destination VARCHAR(100),
    distance_km DOUBLE,
    average_speed_kmh DOUBLE,
    fuel_consumed_liters DOUBLE,
    traffic_conditions VARCHAR(100),
    trip_status VARCHAR(100),
    part_year string comment '년 파티션컬럼',
    part_month string comment '월 파티션컬럼'
);



3. 협업 및 커뮤니케이션
집계(user_profiles) 데이터는 배치로 갱신 되는 정보계 구축 방향성 제시
로그 데이터는 실시간 단위 적재 하되, 필요에 따라 (일,시간,분 단위) 배치로 적재하는 데이터 마트 별도 설계 방안 제시

b.
목적
요구사항
해결방안 제시
아키텍처 설계
시뮬레이션(일부 아키텍처 예시)