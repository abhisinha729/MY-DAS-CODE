# Write your MySQL query statement below
-- select  c.name as customers from customers c left join orders o on c.id=o.customerId where o.id is null; 

select c1.name as Customers
from customers c1 left join orders o1
on c1.id=o1.customerid
where o1.customerid is null
