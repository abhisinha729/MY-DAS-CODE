# Write your MySQL query statement below
select  id, count(id)as num

from (
    select requester_id as id from requestaccepted

union all

select accepter_id as id from requestaccepted
) as friendcount
group by id
order by num desc
limit 1