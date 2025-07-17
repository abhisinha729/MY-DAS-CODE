# Write your MySQL query statement below
select c.customer_id
from customer c  inner join product p
on c.product_key=p.product_key
-- where c.customer_id in (select customer_id from customer where )
-- where c.product_key=p.product_key
group by c.customer_id
having count(distinct p.product_key)= (select count(product_key)from product)
