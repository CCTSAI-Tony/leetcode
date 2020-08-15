'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

#自己想的 time complexity O(n)
#思路: 搭配counter, 最後再取同樣counter.value == 1 的character 中裡面index最小的
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_counter = Counter(s)
        if 1 not in s_counter.values():
            return -1
        return min(s.index(i) for i in s_counter if s_counter[i] == 1) #s.index(i) 回傳第一個index



#自己想的
class Solution:
    def firstUniqChar(self, s: str) -> int:
        temp = {}
        for i in s:
            temp[i] = temp.get(i,0) + 1
            
        for i in range(len(s)):
            if temp[s[i]] == 1:
                return i
        return -1




from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        # counter = Counter()
        # for char in string:
        #     counter[char]+=1
        counter = Counter(s)

        for i in range(len(s)):
            char = string[i]
            if counter[char]==1: return i

        return -1