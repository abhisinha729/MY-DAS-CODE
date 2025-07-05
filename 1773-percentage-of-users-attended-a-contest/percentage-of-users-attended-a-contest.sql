# Write your MySQL query statement below
select contest_id as contest_id, ROUND(COUNT(DISTINCT user_id) * 100 / (SELECT COUNT(*) FROM users), 2) AS percentage
from register
group by contest_id
order by percentage desc,contest_id asc