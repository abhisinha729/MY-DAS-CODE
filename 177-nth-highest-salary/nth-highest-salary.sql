CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set N=N-1;
  RETURN (
      select distinct (salary) 
      from employee 
      order by salary desc
       limit N,1 # limit tell how many row to return and offset tell how many row to skip
  );
end