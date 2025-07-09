# Write your MySQL query statement below
-- SELECT e1.employee_id as employee_id

-- FROM employees e1 left join salaries s1
-- ON e1.employee_id = s1.employee_id
-- where s1.employee_id is null

-- UNION

-- FROM salaries s1 left join employees e1
-- ON s1.employee_id = e1.employee_id
-- where e1.employee_id is null
-- order by e1.employee_id
SELECT e1.employee_id
FROM employees e1
LEFT JOIN salaries s1 ON e1.employee_id = s1.employee_id
WHERE s1.employee_id IS NULL  -- employee in employees but not in salaries

UNION

SELECT s1.employee_id
FROM salaries s1
LEFT JOIN employees e1 ON s1.employee_id = e1.employee_id
WHERE e1.employee_id IS NULL  -- employee in salaries but not in employees

ORDER BY employee_id;


