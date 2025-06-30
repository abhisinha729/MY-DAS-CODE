# Write your MySQL query statement below
-- select *,
-- case 
--   when sex="m" then"f"
--   when sex="f" then"m"
--   end as sex
-- from salary
update salary 
set sex= case when sex="m" then "f" when sex="f" then"m"end
