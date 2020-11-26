-- Write a SQL query to get the second highest salary from the Employee table.

-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+

-- Oracle
SELECT max(Salary) as "SecondHighestSalary" 
FROM (
    
    SELECT Salary, dense_rank() over(ORDER BY Salary DESC) as dense_rank 
    from Employee
    
    ) WHERE dense_rank=2;

-- Not very fast while works for Nth highest and easy to understand.
-- Using MAX to handle returning NULL scenario, MIN will also work.

Introduction to MySQL RANK() function

The RANK() function assigns a rank to each row within the partition of a result set. The rank of a row is specified by one plus the number of ranks that come before it.
 
-- 也可以加入ID

SELECT max(Salary) as "SecondHighestSalary" FROM (
    SELECT ID, Salary, dense_rank() over(ORDER BY Salary DESC) as dense_rank
    from Employee
    ) WHERE dense_rank=2;





-- MySQL
SELECT MAX(Salary) AS 'SecondHighestSalary'
FROM Employee
WHERE Salary < (SELECT MAX(Salary)
               FROM Employee);