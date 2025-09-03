# Write your MySQL query statement below
-- select p.firstName , p.lastName ,a.city , a.state from Person as p left join  address as a on a.personId = p.personId;

select p1.firstName,p1.lastName,a1.city,a1.state
from person p1 left join address a1
on p1.personid=a1.personid