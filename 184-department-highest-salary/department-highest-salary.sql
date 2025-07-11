# Write your MySQL query statement below
select d1.name as department,e1.name as employee,e1.salary as salary
from employee e1  join department d1
on e1.departmentid=d1.id
where e1.salary in(select max(salary)from employee where departmentid=d1.id )

