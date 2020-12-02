'''
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. 
Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
'''

#刷題用這個, 經典kmp, time complexity O(n), space complexity O(n)
#思路: 先針對原字串後面加上* and reverse 字串, 利用kmp 建立lps table, 查看lps[-1] 是多少 => 代表身為reverse 的suffix與原字串prefix有多少字是一樣的
#針對剩下不匹配的reverse字串, 直接加回原字串前面就能保證其為palindrom =>  最小其操作長度 palindrom
#關鍵: 加多長反字串於前面使得整體字串是palindrom, 所以一開始要用lps 來與原字串比對, 最壞情況就是加入整個反字串於前面, 
#比對成功字串就是最終palindrom prefix 與 suffux 的中間重合字串(本身就是palindrom) => aacfaa*aafcaa => aafc aa cfaa, abacfaba*abafcaba => abafc aba cfaba
# s = "abca"
# a = "abca*acba"
# lps(a) => [0,0,0,1,0,1,0,0,1]
# the only longest-prefix for last element in s is the first element.
# In order to make s a pallindrome, we have to repeat everything else than the longest-prefix for the last element in s.
# answer => lps[-1] is 1, so s[1:] is bca, repeat this in reverse for s (as a prefix) to make it a pallindrome.
# s[1:] = 'bca'
# s[1:][::-1] = 'acb'
# s[1:][::-1] + s = 'acb' + 'abca' = 'acbabca'
# 重要: getLPS("AAAAB") => [0, 1, 2, 3, 0] => 前綴與後綴要間隔一格, 所以lps[0] = 0
# lps 精髓: 運用之前比對的資料, 來避掉不必要的重複比對
# abc a bcab a => 比對 c vs a => 失敗 => i = lps[i-1] = i = lps[4] = 2 => 比對 c vs a => 失敗 => i = lps[i-1] = i = lps[1] = 0 => 比對 a vs a => 成功, lps[j] = i + 1 => 0 + 1 = 1
class Solution(object):
    def shortestPalindrome(self, s):
        a = s+"*"+s[::-1] #加*變奇數 avoid overlap
        lps = self.getLPS(a)
        return s[lps[-1]:][::-1] + s

    def getLPS(self, pattern): #這題重點尋找最長prefix
        m = len(pattern)
        lps = [0] * m
        i, j = 0, 1 #j是指針

        while j < m: 
            if pattern[i] == pattern[j]: 
                lps[j] = i + 1 #zero base index issue
                i, j = i+1, j+1
            elif i != 0:
                i = lps[i - 1] #避掉重複比對的關鍵
            else:
                lps[j] = 0
                j += 1
        return lps

#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        a = s + "#" + s[::-1]
        lps = self.lps(a)
        return s[lps[-1]:][::-1] + s
        
    def lps(self, a):
        n = len(a)
        lps = [0] * n
        i, j = 0, 1
        while j < n:
            if a[i] == a[j]:
                lps[j] = i+1
                i += 1
                j += 1
            elif i != 0:
                i = lps[i-1]
            else:
                lps[j] = 0
                j += 1
        return lps

#重寫第三次, 刷題用這個, time complexity O(n), space complexity O(n)
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        a = s + "#" + s[::-1]
        lps = self.getLps(a)
        return s[lps[-1]:][::-1] + s

        
    def getLps(self, p):
        lps = [0, 0]
        j = 0
        n = len(p)
        for i in range(1, n):
            while j > 0 and p[i] != p[j]:
                j = lps[j] 
            if p[i] == p[j]:
                j += 1
            lps.append(j)
        return lps



#面試也要懂這個
#naive solution, time complexity O(n^2), space complexity O(1)
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i = len(s)
        while s[:i] != s[:i][::-1]:
            i -= 1
        return s[i:][::-1] + s






# You must first understand how KMP algorithm works.

# In KMP, we build an auxillary list called as longestPrefixes list (say lps).
# This list will have information about the longest Prefixes.
# lps[i] will have the value where the earlier prefix was seen.

# When we concatenate a string with it's reverse, 
# the last element of the lps list will have the information about the largest prefix for this combined string that was seen for the last element.

# For example:
# s = "abca"
# a = "abca*acba"
# lps(a) => [0,0,0,1,0,1,0,0,1]
# the only longest-prefix for last element in s is the first element.
# In order to make s a pallindrome, we have to repeat everything else than the longest-prefix for the last element in s.
# answer => lps[-1] is 1, so s[1:] is bca, repeat this in reverse for s (as a prefix) to make it a pallindrome.
# s[1:] = 'bca'
# s[1:][::-1] = 'acb'
# s[1:][::-1] + s = 'acb' + 'abca' = 'acbabca'

# 上面解釋看不懂直接看影片
# 影片詳解
# https://www.youtube.com/watch?v=GTJr8OvyEVQ&t=17s
# https://www.youtube.com/watch?v=c4akpqTwE5g











