-- Write your MySQL query statement below

with fract as (
select
    player_id,
    DATEDIFF(event_date, min(event_date) over (partition by player_id)) = 1 as min_date
from  Activity
)
select round(sum(min_date) / count(distinct player_id), 2) as fraction
from fract
;
