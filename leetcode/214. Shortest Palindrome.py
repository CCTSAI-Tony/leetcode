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
                lps[j] = i + 1
                i, j = i+1, j+1
            elif i != 0:
                i = lps[i - 1]
            else:
                lps[j] = 0
                j += 1
        return lps

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











