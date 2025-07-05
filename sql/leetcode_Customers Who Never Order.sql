# Write your MySQL query statement below


select cstm.name as Customers
from Customers as cstm
left join Orders as ord
on cstm.id = ord.customerId
where ord.id is null
;


select Customers.name as Customers
from Customers
where Customers.id not in
(
    select Orders.customerId from Orders
);