'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

'''

#自己重寫 刷題用這個 time complexity O(n), 題目有說non empty string
#思路 經典dp 此題有陷阱, 會出現leading zero, 雖然題目說s是從字串轉換來的, dp[i] => s[:i] 有幾種轉化方式
#此題比較要注意的地方就是base case 條件要寫清楚, 不然base case會出現錯的值
#這題比較trick 的就是 dp[0] = 1, 是為了要讓 valid s[0:2] 可以算在 dp[2] 裡面
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[:1] != "0" else 0
        for i in range(2, len(s) + 1):
            if 0 < int(s[i-1:i]) <= 9: #ex: "122 4", 因為"122" 有三種轉化方式, 因此 "122 4" 也是三種
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26: #ex: "12 24", 因為"12" 有兩種轉化方式, 因此"12 24" 也是兩種, 所以"1224" 有五種
                dp[i] += dp[i-2]
        return dp[len(s)]


# 重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[:1] != "0" else 0
        for i in range(2, len(s) + 1):
            if 0 < int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]


# 重寫第三次, time complexity O(n), space complexity O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0
        for i in range(2, len(s) + 1):
            if 1 <= int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]



#自己重寫 time complexity O(n)
#思路: 此題有陷阱, 會出現leading zero, 雖然題目說s是從字串轉換來的, dp[i] => s[:i] 有幾種轉化方式
#此題比較要注意的地方就是base case 條件要寫清楚, 不然base case會出現錯的值
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1 and s == "0":  #避免 s = "0"
            return 0
        if len(s) == 1: # ex: s = "5", 避免index out of range
            return 1
        dp = [0] * (len(s) + 1)
        dp[1] = 1 if s[:1] != "0" else 0

        if 10 <= int(s[:2]) <= 26 and s[:2] not in ["10", "20"]:
            dp[2] = 2
        elif s[:2] in ["10", "20"] or (s[1] != "0" and s[0] != "0"):  #05, 50 都不行parse
            dp[2] = 1
        else:
            dp[2] = 0
        
        for i in range(3, len(s) + 1):
            if 0 < int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

                
class Solution:
    def numDecodings(s): 
    if not s:
        return 0

    dp = [0 for x in range(len(s) + 1)] #dp法  
    
    # base case initialization
    dp[0] = 1 #若 s[:2] = "12" => dp[2] += dp[0], 此時dp[0] = 1 才能讓dp[2] += 1種 parse way
    dp[1] = 0 if s[0] == "0" else 1   #(1)

    for i in range(2, len(s) + 1): 
        # One step jump 處理一個字 ex: 12312 3
        if 0 < int(s[i-1:i]) <= 9:    #(2) 避免 s[i-1] == "0"
            dp[i] += dp[i - 1]
        # Two step jump 處理兩個字 ex: 1231 23
        if 10 <= int(s[i-2:i]) <= 26: #(3)   #這邊不能用elif, 不然只會考慮一種狀況
            dp[i] += dp[i - 2]
    return dp[len(s)]


#自己想的 naive backtracking, 會碰到很多重複分支, 或許可以用memo紀錄重複分支的結果, 但有點複雜, 跟leetcode 10 使用memo的情況不像, leetcode 10 像修枝, 剪掉不需要的葉子
class Solution:
    def numDecodings(self, s: str) -> int:
        self.res = 0
        self.dfs(s)
        return self.res
    
    def dfs(self, s):
        if not s:
            self.res += 1
            return 
        for i in range(1,3):
            if int(s[:i]) == 0 or int(s[:i]) > 26:
                return 
            if i > 1 and s[:i][0] == "0":
                return 
            if i == 2 and s[i:] == s[i-1:]:
                return 
            self.dfs(s[i:])


        return dp[len(s)]







    '''
Problem Reduction: variation of n-th staircase with n = [1, 2] steps.

Approach: We generate a bottom up DP table.

The tricky part is handling the corner cases (e.g. s = "30").

Most elegant way to deal with those error/corner cases, is to allocate an extra space, dp[0].

Let dp[ i ] = the number of ways to parse分析 the string s[: i]

For example:
s = "231"
index 0: extra base offset. dp[0] = 1
index 1: # of ways to parse "2" => dp[1] = 1
index 2: # of ways to parse "23" => "2 3" and "23", dp[2] = 2
index 3: # of ways to parse "231" => "2 3 1" and "23 1" => dp[3] = 2




Notes of Wisdom:
(1): Handling s starting with '0'. Alternative: I would recommend treating as an error condition and immediately returning 0. 
It's easier to keep track and it's an optimization.
(2) (3): Pay close attention to your comparators. For (1) you want 0 <, not 0 <= . For (2) you want 10 <=, not 10 <



#以下跟此題沒關
Check this out to understand the difference:

>>> a = 2
>>> if a > 1: a = a+1
...
>>> if a > 2: a = a+1
...
>>> a
4
versus

>>> a = 2
>>> if a > 1: a = a+1
... elif a > 2: a = a+1
...
>>> a
3
The first case is equivalent to two distinct if's with empty else statements (or imagine else: pass); in the second case elif is part of the first if statement.

























    '''