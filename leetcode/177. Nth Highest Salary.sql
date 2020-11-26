-- Write a SQL query to get the nth highest salary from the Employee table.

-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

-- +------------------------+
-- | getNthHighestSalary(2) |
-- +------------------------+
-- | 200                    |
-- +------------------------+

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT M, 1  #這裡是用	desc 排序
  );
END

-- 查詢欄位資料的唯一值	select distinct 欄位名 from 資料表名稱;	重複值只列一次

-- 查詢特定筆數資料	select * from 資料表名稱 limit 8, 10;	第9筆開始選取10筆

+----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 300    |
-- | 2  | 200    |
-- | 3  | 100    |
-- +----+--------+

-- declare 只能在 begin 和 end 之間

-- declare 和 set 的差異
-- 根據百度的搜尋結果得知，

-- declare 的限制是要在 begin 和 end 之間使用。
-- set 所宣告的變數會被記憶道使用者離開
-- 因此可以得知他們變數的 scope field 可以使用的區域，defalre 就像是在 function 內宣告的變數，只有 function 使用才會符合一般邏輯，
-- 否則就會出現錯誤，或者不如自己的預期；set 所宣告的變數，即使在 function 內宣告，可是離開了 function 操作仍是被允許的，
-- 所以要小心會不會和其他 function 或 procedure 命名衝突，導致有非預期的變化。

-- CREATE PROCEDURE p8 ()   
-- BEGIN   
-- DECLARE a INT;   
-- DECLARE b INT;   
-- SET a = 5;   
-- SET b = 5;   
-- INSERT INTO t VALUES (a);   
-- SELECT s1 * a FROM t WHERE s1 >= b;   
-- END; // /* I won't CALL this */   
-- 在過程中定義的變數並不是真正的定義，你只是在BEGIN/END塊內定義了而已（譯註：也就是形參）。
-- 注意這些變數和會話變數不一樣，不能使用修飾符@你必須清楚的在BEGIN/END塊中宣告變數和它們的型別。
-- 變數一旦宣告，你就能在任何能使用會話變數、文字、列名的地方使用。

-- RETURN Statement
-- RETURN expr
-- The RETURN statement terminates execution of a stored function and returns the value expr to the function caller. 
-- There must be at least one RETURN statement in a stored function. There may be more than one if the function has multiple exit points.

-- This statement is not used in stored procedures, triggers, or events. The LEAVE statement can be used to exit a stored program of those types.

















