'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
'''

# Python DP solutions 
# O(m*n) space, time complexity O(m*n), 思路 典型點dp解法 先處理邊界情況 再botom up
class Solution:
    r, c, l= len(s1), len(s2), len(s3)  #row, column, 
    if r+c != l:
        return False
    dp = [[True for _ in range(c+1)] for _ in range(r+1)]  #dp[i][j] 代表 [:i], [:j], 所以range(c+1), range(r+1), dp[0][0] empty string, 一開始都是true
    for i in range(1, r+1):
        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1] #建立邊界情況
    for j in range(1, c+1):
        dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
    for i in range(1, r+1):
        for j in range(1, c+1):
            dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or \
               (dp[i][j-1] and s2[j-1] == s3[i+j-1])
    return dp[-1][-1]




# BFS 這個方法不錯 跟上面思路差不多
class Solution:
    def isInterleave(self, s1, s2, s3):
        r, c, l= len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        queue, visited = [(0, 0)], set((0, 0))
        while queue:
            x, y = queue.pop(0)  #x, y 皆從0開始, zero based index
            if x+y == l:  #代表 s3[:l]
                return True
            if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:  #x+1 <= r 代表 x < r
                queue.append((x+1, y)); visited.add((x+1, y))  #(x+1, y) means s1[:x+1], s2[:y]
            if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
                queue.append((x, y+1)); visited.add((x, y+1))
        return False

















       


