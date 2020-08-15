-- The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

-- +----+-------+--------+-----------+
-- | Id | Name  | Salary | ManagerId |
-- +----+-------+--------+-----------+
-- | 1  | Joe   | 70000  | 3         |
-- | 2  | Henry | 80000  | 4         |
-- | 3  | Sam   | 60000  | NULL      |
-- | 4  | Max   | 90000  | NULL      |
-- +----+-------+--------+-----------+
-- Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, 
-- Joe is the only employee who earns more than his manager.

-- +----------+
-- | Employee |
-- +----------+
-- | Joe      |
-- +----------+

SELECT Name AS Employee FROM Employee #注意as擺放的位置
WHERE Employee.Salary > (SELECT Salary FROM Employee AS E2 WHERE Id = Employee.ManagerId); #這邊的Employee.Salary, Employee.ManagerId 可以想像成一種attribute

-- Hey, why is 'AS E2' necessary here? I can't see why we need to create it if we don't subsequently use it...

-- Well, although it is the same table, @@ but if you want to use it for comparing like make a copy of it.@@  For example, 
-- you have Employee and Employee(copy), SQL doesn't know which table's element will be use. That's what I think.

-- FROM Employee AS E2 這邊E2 就代表不同的table 就算內容一樣 