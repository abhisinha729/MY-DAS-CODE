# Write your MySQL query statement below
-- select name,bonus
-- from employee e
-- left join bonus b
-- on e.empid = b.empid 
-- where b.bonus is null or b.bonus<1000;


select e1.name,b1.bonus
from employee e1 left join bonus b1
on e1.empid=b1.empid 
where b1.bonus is null or b1.bonus <1000

