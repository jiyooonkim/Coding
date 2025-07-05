--# Write your MySQL query statement below

select
    product_id, year as first_year, quantity, price
from Sales
where (product_id, year)
    in (
        select distinct
            product_id, min(year) over( partition by product_id ) as first_year
        from Sales
        )
;