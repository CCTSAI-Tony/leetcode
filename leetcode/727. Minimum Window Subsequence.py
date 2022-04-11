'''
Given strings s1 and s2, return the minimum contiguous substring part of s1, so that s2 is a subsequence of the part.

If there is no such window in s1 that covers all characters in s2, return the empty string "". 
If there are multiple such minimum-length windows, return the one with the left-most starting index.

 

Example 1:

Input: s1 = "abcdebdde", s2 = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of s2 in the window must occur in order.
Example 2:

Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
Output: ""
 

Constraints:

1 <= s1.length <= 2 * 104
1 <= s2.length <= 100
s1 and s2 consist of lowercase English letters.
'''

# 刷題用這個, time complexity O(mn), space complexity O(m)
# 思路: 使用dp 來紀錄s2 包含該字當下subsequence 在s1的起始index, dp[i] = 包含該i 的subsequnce 在s1 的起始index
# 一開始使用defaultdict 來存儲s2 相同字的所有index i, 而後遍歷s1, 遇到相同字便update dp[i] = dp[i - 1], 若dp[i - 1] == -1, 代表包含該i 的subsequnce 暫時不存在
# 遍歷s1的途中若遇到 要update s2 的i == 0, dp[0] = s1當下index => 代表在s1找到新subsequnce 的起始點(注意舊的起始點不會被覆蓋, 利用dp 已經被傳到較後的i)
# 利用不斷更新subsequnce 的起始點 來找出最短的subsequence
# 若遍歷到 i == len(s2) - 1 且 dp[i] != -1 => 代表已有包含s2的subsequnce, 再利用 (index - dp[i] + 1) 是否小於之前的subsequnce's length 來更新最短subsequnce
# 注意: 在更新dp[i]時, 要逆序遍歷相同letter 在s2的所有index => 若正序遍歷則會錯誤更新i較大的 dp[i] => 典型2d dp -> 1d dp 的慣用手法, 確保dp[i-1] 還是在上一輪的狀況
from collections import defaultdict
class Solution(object):
    def minWindow(s1, s2):
        m, n = len(s1), len(s2)
        start, length = -1, float('inf')
        dp = [-1] * n #紀錄s2 包含當下字的subsequence 的起始index
        
        table = defaultdict(list)
        for idx, c in enumerate(s2):
            table[c].append(idx)
            
        for idx, c in enumerate(s1):
            if c not in table: 
                continue  
            # We go from the back idx of character c to front occur of idx c
            for i in table[c][::-1]:
                # When i hits 0, we start a new subseq starting with "idx", which idx we are at in the string s1 right now.
                if i == 0: 
                    dp[0] = idx
                # dp[i] is equal to index of dp[i - 1], as:
                # 1. dp[i - 1] == -1, then dp[i] is also unreachable and is thus -1
                # 2. dp[i - 1] == A, where A is a pos integer.  This means there's a subseq starting with idx A going up to dp[i - 1]
                #    Since we found the next character, we can further extend the subseq with the same starting index.
                else: 
                    dp[i] = dp[i - 1]
                
                # We have found a substring that contains our subseq (i == n - 1 and dp[i] >= 0) and 
                # this substring is shorter than the previous one (idx - dp[i] + 1 < length)
                if i == n - 1 and dp[i] >= 0 and idx - dp[i] + 1 < length:
                    start = dp[i]
                    length = idx - dp[i] + 1
        
        if dp[-1] == -1: 
            return ""
        else: 
            return s1[start : start + length]


#重寫第二次, time complexity O(mn), space complexity O(n)
from collections import defaultdict
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [-1] * n
        s2_index = defaultdict(list)
        length = float("inf")
        start = -1
        for i, c in enumerate(s2):
            s2_index[c].append(i)
        for i1, c in enumerate(s1):
            for i2 in s2_index[c][::-1]:
                if i2 == 0:
                    dp[0] = i1
                else:
                    dp[i2] = dp[i2 - 1]
                if i2 == (n - 1) and dp[i2] != -1 and (i1 - dp[i2] + 1) < length:
                    length = (i1 - dp[i2] + 1)
                    start = dp[i2]
        if length == float("inf"):
            return ""
        return s1[start:(start+length)]

# 重寫第三次, time complexity O(mn), space complexity O(m)
from collections import defaultdict
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n = len(s2)
        dp = [-1] * n
        start, end = -1, -1
        ans_len = float("inf")
        s2_map = defaultdict(list)
        for i, c in enumerate(s2):
            s2_map[c].append(i)
        for i, c in enumerate(s1):
            if c not in s2_map:
                continue
            for idx in s2_map[c][::-1]:
                if idx == 0:
                    dp[0] = i
                else:
                    dp[idx] = dp[idx-1]
                if idx == n-1 and dp[idx] >= 0 and i - dp[idx] + 1 < ans_len:
                    ans_len = i - dp[idx] + 1
                    start = dp[idx]
                    end = i

        if dp[-1] == -1:
            return ""
        return s1[start:end+1]