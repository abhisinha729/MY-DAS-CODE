# Write your MySQL query statement below
-- select a.name Employee from  Employee a join Employee b on a.managerId=b.Id where a.salary>b.salary

select e1.name as employee
from employee e1  left join employee e2
on e1.managerid=e2.id
where e1.salary>e2.salary


