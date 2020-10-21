# Given a string, find the length of the longest substring T that contains at most k distinct characters.

# Example 1:

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# Example 2:

# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.

# What is the time complexity of dict.keys() in Python? => In Python 3, it's O(1), but it doesn't return a list. 
# To draw a random element from a dict's keys, you'd need to convert it to a list.

#自己重寫 time complexity O(n)
#思路: sliding window, 利用dict 來紀錄區間內的元素, 利用l, r 指針來組成sliding window
#r指針遍歷整個s, 遍歷到的元素紀錄在dict裡, 一但dict裡的key 超過k個, 利用l指針往右內縮來去除多餘的元素, 直到dic.key == k個
#完成條件後, 紀錄l與r之間的元素長度, update max_len
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_len = 0
        dic = defaultdict(int)
        l, r = 0, 0
        for r in range(len(s)):
            dic[s[r]] += 1
            while len(dic.keys()) > k:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len


#其他人的解
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans=0
        start=0
        dic={}
        for i in range(len(s)):
            dic[s[i]]=i #更新該字的最大index
            if len(dic)>k:
                start=min(dic.values())+1 #跑到目前在dict裡面index最小的元素的右一格(縮小window)
                del dic[s[start-1]] #delete 該元素
            ans=max(ans,i-start+1)
        return ans




