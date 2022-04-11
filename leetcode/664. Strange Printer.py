'''
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.

 

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
'''

# Let dp(i, j) be the number of turns needed to print S[i:j+1].

# Note that whichever turn creates the final print of S[i], might as well be the first turn, 
# and also there might as well only be one print, since any later prints on interval [i, k] could just be on [i+1, k]. # 重要

# So suppose our first print was on [i, k]. We only need to consider prints where S[i] == S[k], 
# because we could instead take our first turn by printing up to the last printed index where S[k] == S[i] to get the same result.

# Then, when trying to complete the printing of interval [i, k] (with S[i] == S[k]), 
# the job will take the same number of turns as painting [i, k-1]. 
# This is because it is always at least as good to print [i, k] first in one turn rather than separately.

# Also, we would need to complete [k+1, j]. So in total, our candidate answer is dp(i, k-1) + dp(k+1, j). 
# Of course, when k == i, our candidate is 1 + dp(i+1, j): we paint S[i] in one turn, then paint the rest in dp(i+1, j) turns.

# 刷題用這個, dp top down, time complexity O(n^3), space complexity O(n^2)
# 思路: dp(i, j) 代表 S[i:j+1], 因為print 只能print 一樣的character, 基本 dp(i, j) <= 1 + dp(i + 1, j)
# 但是若中間 k index => s[i] == s[k], dp(i, k) == dp(i, k-1), 這樣一來 dp(i, j) = dp(i, k-1) + dp(k+1, j) => 減少print turn
class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}
        def dp(i, j):
            if i > j: 
                return 0
            if (i, j) not in memo:
                ans = dp(i+1, j) + 1
                for k in range(i+1, j+1):
                    if s[k] == s[i]:
                        ans = min(ans, dp(i, k-1) + dp(k+1, j))
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, len(s) - 1)

# 重寫第二次, time complexity O(n^3), space complexity O(n^2)
class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}
        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = 1 + dp(i+1, j)
            for k in range(i+1, j+1):
                if s[i] == s[k]:
                    memo[(i, j)] = min(memo[(i, j)], dp(i, k-1) + dp(k+1, j))
            return memo[(i, j)]
        dp(0, len(s) - 1)
        return memo[(0, len(s)-1)]



