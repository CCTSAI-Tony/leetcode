'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

#自己想的 time complexity O(n)
#思路: 利用defaultdict 來存儲pattern 的元素, 再利用l, r指針遍歷s, 建立scan dict 來存放遍歷的item, 若r-l + 1 > len(p) => l指針內縮
#r指針往右遍歷的同時, 比較pattern 與scan, 若兩者相同代表找到anagram, res.append l指針位置
#dict compare time complexity O(1) => since there are at most 26 English letters 
from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n = len(p)
        pattern = defaultdict(int)
        for c in p:
            pattern[c] += 1
        scan = defaultdict(int)
        l = 0
        for r in range(len(s)):
            scan[s[r]] += 1
            if (r-l+1) > n:
                scan[s[l]] -= 1
                if not scan[s[l]]:
                    del scan[s[l]]
                l += 1
            if scan == pattern: #python dic check => O(n), but This step is O(1), since there are at most 26 English letters 
                res.append(l)
        return res


