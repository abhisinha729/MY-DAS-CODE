# Write your MySQL query statement below
-- select id,revenue as jan_revenue,revenue as feb_revenue,revenue as mar_revenue,revenue as apri_revenue,revenue as may_revenue,revenue as jun_revenue,revenue as jul_revenue,revenue as aug_revenue,revenue as sep_revenue,revenue as oct_revenue,revenue as nov_revenue,revenue as dec_revenue,
-- case
-- when month between "apr" and "dec" then null
-- else revenue 
-- from department
-- group by id;


select id,sum(case when month="jan" then revenue end) as jan_revenue,
sum(case when month="feb" then revenue end) as Feb_revenue,
sum(case when month="mar" then revenue end) as Mar_revenue,
sum(case when month="apr" then revenue end) as Apr_revenue,
sum(case when month="may" then revenue end) as May_revenue,
sum(case when month="jun" then revenue end) as Jun_revenue,
sum(case when month="jul" then revenue end) as Jul_revenue,
sum(case when month="aug" then revenue end) as Aug_revenue,
sum(case when month="sep" then revenue end) as Sep_revenue,
sum(case when month="oct" then revenue end) as Oct_revenue,
sum(case when month="nov" then revenue end) as Nov_revenue,  
sum(case when month="dec" then revenue end) as Dec_revenue
from department
group by id