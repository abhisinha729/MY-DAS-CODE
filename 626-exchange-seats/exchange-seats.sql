# Write your MySQL query statement below
select case 
when id=(select max(id) from seat) and mod(id,2)=1 then id
when 
 mod(id,2)=1 then id+1 else id-1 end as id,student 
from seat 
order by id asc



-- SELECT 
--     CASE 
--         WHEN id = (SELECT MAX(id) FROM seat) AND MOD(id, 2) = 1 THEN id
--         WHEN MOD(id, 2) = 1 THEN id + 1 
--         ELSE id - 1 
--     END AS id,
--     student 
-- FROM seat
-- ORDER BY id;
