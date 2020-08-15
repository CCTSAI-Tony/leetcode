-- Write a SQL query to find all duplicate emails in a table named Person.

-- +----+---------+
-- | Id | Email   |
-- +----+---------+
-- | 1  | a@b.com |
-- | 2  | c@d.com |
-- | 3  | a@b.com |
-- +----+---------+
-- For example, your query should return the following for the above table:

-- +---------+
-- | Email   |
-- +---------+
-- | a@b.com |
-- +---------+

SELECT email
FROM person
GROUP BY email
HAVING COUNT(email) > 1

-- MySQL GROUP BY 语句
-- GROUP BY 语句根据一个或多个列对结果集进行分组。

-- 在分组的列上我们可以使用 COUNT, SUM, AVG,等函数。

-- 我试过用where，但是where不行，但是having可以，求大神解释一下！感谢

-- where 不能用于 filter groupby之后的结果

-- 对Email字段聚合 通过having子句可以迅速判断Email 有没有重复