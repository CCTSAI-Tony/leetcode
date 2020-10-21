# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

#自己重寫  time cokplexity O(n^2) 972ms
#思路: 注意此題是求substring, 所以把指針當作是palindrom中心, 向外延展確認就能找到最長的palindrom, 要注意的地方還要考慮palindrom is even or odd, 中心會不太一樣
#若是求 sunsequence, 則暴力解複雜度會大增, 就要使用dp, 就是課本的longest common sequence, 只要把s.reverse()  當作另一比對字串, 就能變成 longest palindrom sequence
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            temp = self.helper(i,i,s)
            if len(temp) > len(res):
                res = temp
            
            temp = self.helper(i,i+1,s)
            if len(temp) > len(res):
                res = temp
        return res
    
    
    def helper(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

#自己重寫 manacher algorithm, time complexity O(n), 108ms
#思路: 參照別人代碼修改, 利用lps 對稱性質, 此算法可以讓新index在計算回文長度時參照對應center另一邊index的lps長度, 減少重複比對回文字串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        manacher_str = "#" + "#".join(s) + "#"
        n = len(manacher_str)
        lps = [0] * n
        r = 0
        c = 0
        for i in range(1, n):
            if r >= i:  #r > i 也可以, 沒差
                lps[i] = min(r-i, lps[c-(i-c)])  #lps[c-(i-c)] 鏡向對面相對應index的lps
            while i - lps[i] - 1 >= 0 and i+ lps[i] + 1 < n and manacher_str[i - lps[i] - 1] == manacher_str[i+ lps[i] + 1]:
                lps[i] += 1
            
            if i + lps[i] > r:
                c = i
                r = i + lps[i]
        max_len, max_center = max((v, i) for i, v in enumerate(lps))
        longest_palindrom = s[(max_center-max_len) //2 : (max_center+max_len) //2 ]  #唯一需要背的地方, 轉化成s原本的index, 不難懂看blog就清楚
        return longest_palindrom

#重寫第二次
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_m = "#" + "#".join(s) + "#"
        lps = [0] * len(s_m)
        c = r = 0
        for i in range(1, len(s_m)):
            if r > i:
                lps[i] = min(lps[c-(i-c)], r-i)
            while i - lps[i] - 1 >= 0 and i + lps[i] + 1 < len(s_m) and s_m[i - lps[i] - 1] == s_m[i + lps[i] + 1]:
                lps[i] += 1
            if i + lps[i] > r:
                c = i
                r = i + lps[i]
        max_center, max_len = max([(i, v) for i, v in enumerate(lps)], key=lambda x: x[1])
        return s[(max_center-max_len)//2:(max_center+max_len)//2]





# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)): #以index i為中心向外確認
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]  #脫離while loop, l已經-=1. r已經+=1, 所以要加回來, r不用因為左閉右開



Manacher algorithm in Python O(n)
class Solution:
    #Manacher algorithm
    #http://en.wikipedia.org/wiki/Longest_palindromic_substring
    
    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^a#b#b#a$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))  #好招
        n = len(T)
        P = [0] * n  #計算每個index當center 的LPS
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]

a = (100,1)
b = (1,100)
max(a,b)
(100, 1)

a = 0
a = 1>3 and 6
a
False
a += 1
a
1

a = 0
a = 1>0 and 6
a
6

a = 100 if 3 > 2 else 0
a
100


# manachert 算法 time complexity O(n)
# https://medium.com/hoskiss-stand/manacher-299cf75db97e
class Solution:
    def longestPalindrome(self, s: str) -> str:
        string_size = len(s)
        if string_size < 3:
            if s==s[::-1]:
                return s
            else:
                return s[0]

        manacher_str = "#"
        for index in range(len(s)):
            manacher_str += s[index]
            manacher_str += "#"

        LPS_table = [0]*len(manacher_str)
        center = 1
        max_right = 2
        max_length = 0
        LPS_center = 0

        total_size = len(manacher_str)
        for index in range(1, len(manacher_str)):
            if index < max_right:
                LPS_table[index] = min(LPS_table[2*center-index], max_right-index)
            else:
                LPS_table[index] = 0

            # when calculating LPS value, self position (index) is not included
            while (index-LPS_table[index]-1 >= 0 and
                   index+LPS_table[index]+1 < total_size and
                   manacher_str[index-LPS_table[index]-1] == manacher_str[index+LPS_table[index]+1]):
                   LPS_table[index] += 1

            if LPS_table[index] > max_length:
                max_length = LPS_table[index]
                LPS_center = index

            if LPS_table[index]+index > max_right:
                max_right = LPS_table[index]+index
                center = index

        start = (LPS_center-max_length)//2
        return s[start: start+max_length]


#code signal

class Solution:
    def cutPalindrom(self, string: str) -> str:
        while self.dfs(string) >= 2:
            string = string[self.dfs(string):]
        return string
    
    def dfs(self, string):
        max_len = 1
        for length in range(1, len(string) + 1):
            l, r = 0, length-1
            while l <= r and string[l] == string[r]:
                l += 1
                r -= 1
            if l > r:
                max_len = max(max_len, length)
        return max_len



