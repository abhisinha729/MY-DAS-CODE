# Write your MySQL query statement below
select distinct employee_id,  department_id
from employee
where employee_id in (select employee_id from employee group by employee_id having count(*)=1 ) or primary_flag="Y"
group by employee_id
order by employee_id
