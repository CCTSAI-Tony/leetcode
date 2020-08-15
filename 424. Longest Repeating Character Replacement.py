'''
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''





# sliding window method (2 pointer)
# For a window s[l:r+1], if r - l + 1 - max_freq of s[l:r+1] <= k, we can perform
# at most k operation and change it to a string with repeating characters.
# Keep a moving window expand while r - l + 1 - max_freq of s[l:r+1] <= k ,
# then shrink while r - l + 1 - max_freq of s[l:r+1] > k.
#time complexity O(n)

#  思路:  利用dict來存取 slinding window 每個letter 的count, 並動態check window裡面的元素是否大於k個與最大count letter 不同的元素, 若是就要從左邊縮小window,
#  直到 window裡面的元素不同最大count的letter 小於等於k個, 這樣才能把他們通通變成 最大count letter
import collections
class Solution:
    def characterReplacement(self, s, k):        
        longest_window = 0
        window_counts = collections.defaultdict(int)
        l = 0
        for r in range(len(s)):
            window_counts[s[r]] += 1 #右指針所在的字母, 建立letter:count pair, 紀錄這個window 每個letter 的count
            while r - l + 1 - max(window_counts.values()) > k: #加入r指針的letter後, 若這個wondow 有大於 k個 與最大count letter 不同的字母時, 代表不能把他們通通變成最大count的letter
                                                               #若> k, 縮小window, 直到left指針越過一個不是最大count的字母
                window_counts[s[l]] -= 1 #l往右移
                l += 1
            longest_window = max(longest_window, r - l + 1)
        return longest_window

# window 最大count的letter 是會動態改變的, 這也是使用slinding window 的原因, 左右指針可以依情況調整
# sliding window, 常見手法, window吸收一個新元素, 看是否對window造成影響並直接調整window 左右指針是否變大或縮小

#自己重寫
import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = collections.defaultdict(int)
        max_len = 0
        l = 0
        for r in range(len(s)):
            dic[s[r]] += 1
            while (r - l + 1) - max(dic.values()) > k:
                dic[s[l]] -= 1
                l+=1
            max_len = max(max_len, r-l+1)
        return max_len









"ABBB" 2 => 4
#自己想的 TLE, brute force, time complexity O(n^2), multipass, start指針每前進一格, end指針又得回到start指針地方, 雙指針來回建立太多不必要的區間
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        for i in range(len(s)):
            count = 0
            start, end = i, i
            check = s[start]
            if end + 2 < len(s) and s[end+1] != s[start]:
                if s[end+1] == s[end+2] and k > 0:
                    check = s[start+1]
                    count += 1 
                    end += 1
            while end < len(s):
                if s[end] != check:
                    if count >= k:
                        break
                    count += 1
                max_len = max(max_len, end - start + 1)
                end += 1
        
        return max_len







