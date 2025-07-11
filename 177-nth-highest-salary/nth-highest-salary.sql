CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set N=N-1;
  RETURN (
      select distinct (salary) 
      from employee 
      order by salary desc
       limit 1 offset N # limit tell how many row to return and offset tell how many row to return 
  );                     # here we can also write limit N,1 (shorthand )
end