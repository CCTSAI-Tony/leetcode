'''
Given a string S, return the number of substrings of length K with no repeated characters.

 

Example 1:

Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation: 
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: S = "home", K = 5
Output: 0
Explanation: 
Notice K can be larger than the length of S. In this case is not possible to find any substring.
 

Note:

1 <= S.length <= 10^4
All characters of S are lowercase English letters.
1 <= K <= 10^4
'''


#刷題用這個, time complexity O(n), sliding window
#思路: 建立l, r 指針, 設一個dict, 紀錄r指針所指到的ch, 指到的ch d[ch] += 1 => 若指到的ch d[ch] > 1 代表有重複元素, 右移l指針, 每右移l指針就d[ch] -= 1, 直到r指針的d[ch] = 1
#當 r - l + 1 == K, 代表找到一個valid substring, 右移l指針一格, 找下一個valid string, 記得l指針右移 d[ch] -= 1
#這個方式, l, r指針最多各經過每個元素一次
from collections import defaultdict
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        count = 0
        d = defaultdict(int)
        l, r = 0, 0
        for r in range(len(S)):
            d[S[r]] += 1
            while d[S[r]] > 1:
                d[S[l]] -= 1
                l += 1
            if r - l + 1 == K:
                count += 1
                d[S[l]] -= 1
                l += 1
        return count







#自己想的 naive fixted window 
#time complexity O((len(S)-K+1)*K)
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        count = 0
        n = len(S)
        for i in range(n-K+1):
            temp = len(set(S[i:i+K]))
            if temp == K:
                count += 1
        return count






