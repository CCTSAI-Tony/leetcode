-- Write a SQL query to find all numbers that appear at least three times consecutively.

-- +----+-----+
-- | Id | Num |
-- +----+-----+
-- | 1  |  1  |
-- | 2  |  1  |
-- | 3  |  1  |
-- | 4  |  2  |
-- | 5  |  1  |
-- | 6  |  2  |
-- | 7  |  2  |
-- +----+-----+
-- For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+

SELECT Distinct(Num) as ConsecutiveNums
FROM Logs #表是Logs
WHERE (ID+1,Num) IN (Select Id, Num From Logs)
AND (ID+2,Num) IN (Select Id, Num From Logs)

-- It's looking for all instances where ID+1 has the same value in the Num column as ID. Same with ID+2, 
-- but if there's 4 in a row I dont want repeats so i used Distinct. 防止 3,3,3,3 首二都滿足條件

-- If that wasn't clear, the value 'Num' in the tuple (ID+1,NUM) or (2,1) implies we want to check that (ID,Num) 
-- or (1,1) has the same number so we do a subquery to check that (2,1) exists in the table. Then we do the same for (3,1). 
-- If this is true then it checks out that we have three consecutive 1's. The assumption is that the ID's are the natural ordering of the table.