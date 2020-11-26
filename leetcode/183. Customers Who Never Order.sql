-- Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

-- Table: Customers.

-- +----+-------+
-- | Id | Name  |
-- +----+-------+
-- | 1  | Joe   |
-- | 2  | Henry |
-- | 3  | Sam   |
-- | 4  | Max   |
-- +----+-------+
-- Table: Orders.

-- +----+------------+
-- | Id | CustomerId |
-- +----+------------+
-- | 1  | 3          |
-- | 2  | 1          |
-- +----+------------+
-- Using the above tables as example, return the following:

-- +-----------+
-- | Customers |
-- +-----------+
-- | Henry     |
-- | Max       |
-- +-----------+

select c.Name as Customers
from Customers c
left join Orders o on c.Id = o.CustAomerId
where o.Id IS NULL

-- 对于右表中没有对应匹配的数据记录，其所有的列都被置为 NULL，因此要查询这部分记录可以附加 IS NULL 条件：

-- 以下都對

SELECT C.NAME AS Customers
FROM Customers as C
LEFT JOIN Orders AS O ON C.ID = O.CustomerId
WHERE O.CustomerId IS NULL

SELECT C.NAME AS Customers
FROM Customers as C
LEFT JOIN Orders AS O ON C.ID = O.CustomerId
WHERE O.ID IS NULL