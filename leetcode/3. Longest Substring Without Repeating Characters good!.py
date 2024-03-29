'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

#自己想的, time complexity O(n) 48ms, slinding window
#思路: 利用雙指針, 並使用dict來紀錄右指針指導元素的index, 來確認之後是否遇到重複的元素, 並移動左指針到合適位置
#若右指針指向重複元素, 則左指針往該重複元素紀錄的index移動, 注意的是, 左指針移動的過程要移除經過的元素的key, 代表slinding window, 
#直到移動到重複元素index+1, 這樣新window就不包含舊重複元素的index
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start, end = 0, 0
        temp = {}
        for end in range(len(s)):
            if s[end] not in temp:
                max_length = max(max_length, end - start + 1)
            else:
                pre_index = temp[s[end]]
                while start <= pre_index:
                    del temp[s[start]]
                    start += 1      
            temp[s[end]] = end
        return max_length


#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 0
        stored = set()
        l = 0
        for r in range(len(s)):
            while s[r] in stored:
                stored.remove(s[l])
                l += 1
            stored.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len


#重寫第三次, time complexity O(n), space complexity O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l, r = 0, 0
        max_len = 0
        while r < len(s):
            if s[r] in visited:
                max_len = max(max_len, r - l)
                while r < len(s) and s[r] in visited:
                    visited.remove(s[l])
                    l += 1
            visited.add(s[r])
            r += 1

        max_len = max(max_len, r - l)
        return max_len

#重寫第四次
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = {}
        l = 0
        max_len = 0
        for r in range(len(s)):
            if s[r] not in memo:
                memo[s[r]] = r
                continue
            else:
                idx = memo[s[r]]
                max_len = max(max_len, r - l)
                while l <= idx:
                    del memo[s[l]]
                    l += 1
                memo[s[r]] = r
        max_len = max(max_len, len(s) - l)
        return max_len



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        p1 = p2 = m = 0
        
        while p2 < len(s):
            if s[p2] not in d:
                d[s[p2]] = True
                p2 += 1
                m = max(len(d), m)
            else:
                del d[s[p1]]
                p1 += 1 #直到扣掉自己符號為止
            
        return m

        #abcddefghi
        #abcabcdabcde