# Write your MySQL query statement below
select query_name,round(avg(rating/position),2)as quality,round(avg(if(rating<3,1,0)*100),2) as poor_query_percentage
from queries
group by query_name
#if(rating<3,1,0)) it means that if rating greater than 3 then return 0 else return 1 and as we can see dog 1 rating 5 it means it return 0  and dog 2 rating 5 it means it return 0  and dog 3 rating  1 it means it return 1 so percent is 0+0+1/100=33.33 and so on for cat also