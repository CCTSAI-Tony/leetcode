
-- SQL Schema
-- Table: Person

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | PersonId    | int     |
-- | FirstName   | varchar |
-- | LastName    | varchar |
-- +-------------+---------+
-- PersonId is the primary key column for this table.
-- Table: Address

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | AddressId   | int     |
-- | PersonId    | int     |
-- | City        | varchar |
-- | State       | varchar |
-- +-------------+---------+
-- AddressId is the primary key column for this table.
 

-- Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:

-- FirstName, LastName, City, State


# Write your MySQL query statement below

basic left join: 902ms.

SELECT FirstName, LastName, City, State
FROM Person
LEFT JOIN Address
ON Person.PersonId = Address.PersonId;A

-- 也可以
SELECT PERSON.FIRSTNAME ,PERSON.LASTNAME,ADDRESS.CITY,ADDRESS.STATE
FROM PERSON
LEFT JOIN ADDRESS
ON PERSON.PERSONID = ADDRESS.PERSONID


left join + using: 907ms

SELECT FirstName, LastName, City, State
FROM Person
LEFT JOIN Address
USING(PersonId);

natural left join: 940ms

SELECT FirstName, LastName, City, State
FROM Person
NATURAL LEFT JOIN Address;
left join is the fastest compare to the two others.






-- '''
-- char　varchar(variable character)

-- 　　　　　儲存單位 : 1 Byte
-- --------------------------------------------------------------
-- char[(n)]   　n必須是1到8000的值。
-- varchar[(n|max)]    　n可以是1到8000之間的值。max表示儲存體大小上限， 2^31-1 個位元組(2 GB)

-- 從上表可以很簡單的看出，多了var前置英文字，表示儲存資料的長度是否固定。

-- 舉個簡單的例子好了，若現在資料表有兩個欄位:
-- col1　char(10)
-- col2　varchar(10)
-- 存入相同的資料「Hello」

-- col1 會自動在「Hello」後面補空白，存滿10 Bytes
-- col2 會根據資料大小變更儲存空間，以「Hello」為例，則存了5 Bytes

-- 若以資料查詢的效能來說，使用varchar相對節省空間，索引速度自然較快。
-- '''