# Write your MySQL query statement belo
select user_id,email
from users
where email regexp '^[a-zA-Z0-9]*@[a-zA-Z]*.com'
order by user_id