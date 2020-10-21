'''
Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.

 

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
 

Constraints:

1 <= s.length <= 1000
s has only lowercase English letters.
1 <= k <= s.length
'''

mem[i,j] = n => means it takes n delete to make s[i:j] a palindrome.
if s[i] == s[j-1] then mem[i,j] = mem[i+1, j-1] i, j => left, right
else mem[i,j] = min(mem[i, j-1], mem[i+1,j]) + 1 => 消掉s[i], 還是s[j-1], 都要付出一個代價
for any i==j or i+1 ==j mem[i,j] = 0, because i==j is empty string and i+1==j is single char.
Time: O(n^2)
Space: O(n^2)

#刷題用這個, top down memo, time complexity O(n^2), space complexity O(n^2)
#思路: dp top down, dp[i][j] => s[i:j] => dp[i][j] = dp[i+1][j-1] if s[i] == s[j-1], else dp[i][j] = min(dp[i][j-1], dp[i+1][j]) + 1
#重複子問題, dp[j][k] 左邊, 右邊內縮的順序不同, 但內縮後遇到的子問題有可能重複
#dp[i][j] 代表: 使s[i:j+1] 變成palindrom 需要remove的字數, base case dp[i][j] = 0 if i == j or i+1 = j
#最後return dp[0][len(s)] <= k
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        mem = {}
        return self.helper(s, 0, len(s), mem) <= k
    
    def helper(self, s, left, right, mem):
        if left == right or left + 1 == right: # empty string or single letter
            return 0
        if (left, right) in mem:
            return mem[(left, right)]
        if s[left] == s[right-1]:
            mem[(left, right)] = self.helper(s, left+1, right-1, mem)
        else:
            mem[(left, right)] = min(self.helper(s, left+1, right, mem), self.helper(s, left, right-1, mem)) + 1
        return mem[(left, right)]



#自己重寫, time complexity O(n^2), space complexity O(n^2)
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        memo = {}
        return self.dfs(s, 0, len(s), memo) <= k
    
    def dfs(self, s, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == j or i + 1 == j:
            return 0
        if s[i] == s[j-1]:
            memo[(i, j)] = self.dfs(s, i+1, j-1, memo)
        else:
             memo[(i, j)] = min(self.dfs(s, i+1, j, memo), self.dfs(s, i, j - 1, memo)) + 1
        return memo[(i, j)]




















