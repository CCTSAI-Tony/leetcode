-- The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.

-- +----+-------+--------+--------------+
-- | Id | Name  | Salary | DepartmentId |
-- +----+-------+--------+--------------+
-- | 1  | Joe   | 70000  | 1            |
-- | 2  | Jim   | 90000  | 1            |
-- | 3  | Henry | 80000  | 2            |
-- | 4  | Sam   | 60000  | 2            |
-- | 5  | Max   | 90000  | 1            |
-- +----+-------+--------+--------------+
-- The Department table holds all departments of the company.

-- +----+----------+
-- | Id | Name     |
-- +----+----------+
-- | 1  | IT       |
-- | 2  | Sales    |
-- +----+----------+
-- Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, 
-- your SQL query should return the following rows (order of rows does not matter).

-- +------------+----------+--------+
-- | Department | Employee | Salary |
-- +------------+----------+--------+
-- | IT         | Max      | 90000  |
-- | IT         | Jim      | 90000  |
-- | Sales      | Henry    | 80000  |
-- +------------+----------+--------+
-- Explanation:

-- Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.

SELECT dep.Name as Department, emp.Name as Employee, emp.Salary 
from Department dep, Employee emp 
where emp.DepartmentId=dep.Id  #為兩表搭建橋樑 
and emp.Salary=(Select max(Salary) from Employee e2 where e2.DepartmentId=dep.Id); #Employee e2 避免重複, 關鍵字dep.Id



SELECT d.Department, e.Name as Employee, e.Salary
FROM (
    SELECT d.Name AS Department, d.Id AS dId, MAX(e.Salary) AS Salary
    FROM Employee e
    LEFT JOIN Department d
    ON e.DepartmentID = d.Id
    GROUP BY Department, dId
    ) d
INNER JOIN Employee e
ON d.Salary = e.Salary
AND d.dId = e.DepartmentId;

-- Subquery joins the department name and gets the max salary for each department
-- Outer query joins the employee name (via salary and department ID)


-- INNER JOIN（内连接,或等值连接）：获取两个表中字段匹配关系的记录。
-- LEFT JOIN（左连接）：获取左表所有记录，即使右表没有对应匹配的记录。
-- RIGHT JOIN（右连接）： 与 LEFT JOIN 相反，用于获取右表所有记录，即使左表没有对应匹配的记录。 
































