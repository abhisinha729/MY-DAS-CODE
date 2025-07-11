# Write your MySQL query statement below
-- select max(salary)as secondHighestSalary
-- from employee
-- where salary<(select max(salary) from employee)
select (select distinct salary 
from employee
order by  salary desc
limit 1,1) as secondhighestsalary