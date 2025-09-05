# Write your MySQL query statement below
-- select w1.id
-- from weather w1
-- inner join weather w2
-- where datediff(w1.recorddate,w2.recorddate)=1# datediff  is function that give difference between dates
-- and w1.temperature > w2.temperature


select w1.id
from weather w1 join weather w2
-- on w1.id=w2.id
where datediff(w1.recorddate,w2.recorddate)=1 and w1.temperature > w2.temperature