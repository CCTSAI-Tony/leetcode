'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, 
one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''

# Sliding Window , 刷題用這個, 88ms
# time complexity O(n), n=len(s2)
# 思路: 先利用d1 紀錄s1 每個字母count, 再建立d2紀錄前len(s1)的元素, 維持len(s1)大小的window 來scan s2, 看是否在scan的過程中 d2 得到的結果等於d1的, 若是則return True
# why固定window len, 因為題目要check 是否s2有substring of s1的permutation, 連續的字串都是s1的字母
from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
        d1, d2 = Counter(s1), Counter(s2[:len(s1)])  #Counter(s2[:len(s1)]) => maitain window lenth
        for end in range(len(s1), len(s2)):
            if d1 == d2:  #比對前一round 未加s2[end] 
                return True
            d2[s2[end]] += 1
            d2[s2[end-len(s1)]] -= 1
            if d2[s2[end-len(s1)]] == 0:  #記得del key, 使得Counter 可以比對成功
                del d2[s2[end-len(s1)]]
        return d1 == d2  #比對最後一round


#自己重寫 76ms
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = Counter(s1)
        d2 = Counter(s2[:len(s1)])
        if d1 == d2:
            return True
        for end in range(len(s1), len(s2)):
            d2[s2[end]] += 1
            d2[s2[end-len(s1)]] -= 1
            if d2[s2[end-len(s1)]] == 0:
                del d2[s2[end-len(s1)]]
            if d1 == d2:
                return True
        return False



#  自己想的, time complexity O(n*m), n: len(s1), m: len(s2), 1788ms
#  思路: 先利用counter 紀錄s1 每個字母count, 再遍歷s2, 維持len(s1)大小的window 來scan s2, 看是否在scan的過程中 Counter 得到的結果等於之前Counter s1的, 若是則return True
#  why固定window len, 因為題目要check 是否s2有substring of s1的permutation, 連續的字串都是s1的字母
import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = collections.Counter(s1)
        n = len(s1)
        left = 0
        for i in range(len(s2)):
            if s2[i] not in letters:
                left = i + 1  
            if i - left + 1 == n:
                if collections.Counter(s2[left:i+1]) == letters:
                    return True
                left += 1  #左指針內縮
        return False

#自己想的 1484ms, maitain a fixed window scan s2, time complexity O(n*m), n: len(s1), m: len(s2)
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pattern = Counter(s1)
        start = 0
        for end in range(len(s1),len(s2)+1):
            if Counter(s2[end-len(s1):end]) == pattern:
                return True
        return False








