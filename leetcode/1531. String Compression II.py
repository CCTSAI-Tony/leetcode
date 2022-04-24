'''
Run-length encoding is a string compression method that works by replacing consecutive identical characters 
(repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). 
For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. 
You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting at most k characters.

 

Example 1:

Input: s = "aaabcccd", k = 2
Output: 4
Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. 
Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, 
for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, 
the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.
Example 2:

Input: s = "aabbaa", k = 2
Output: 2
Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
Example 3:

Input: s = "aaaaaaaaaaa", k = 0
Output: 3
Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.
 

Constraints:

1 <= s.length <= 100
0 <= k <= s.length
s contains only lowercase English letters.
'''


# 刷題用這個, time complexity O(2^n), space complexity O(2^n)
# 思路: memo, last 是上一個連續的字, last count 是上一個字的連續 count數, left 剩餘的k數
# 連續相同的字 不會delete, 因為delete 這字的狀況早在是否要接這個字的一開始就考慮過了
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # this decorator automatically use memo with key = (start, last, last_count, left)
        @lru_cache(None)
        def counter(start, last, last_count, left): #count the cost of compressing from the start
            if left < 0:
                return float('inf') # this is impossible
            if start >= len(s):
                return 0
            if s[start] == last:
                # we have a stretch of the last_count of the same chars, what is the cost of adding one more? 
                incr = 1 if last_count == 1 or last_count == 9 or last_count == 99 else 0 # 最多100 個
                # no need to delete here, if we have a stretch of chars like 'aaaaa' - we delete it from the beginning in the else delete section
                return incr + counter(start+1, last, last_count+1, left) # we keep this char for compression
            else:
                # keep this char for compression - it will increase the result length by 1 plus the cost of compressing the rest of the string 
                keep_counter = 1 + counter(start+1, s[start], 1, left)
                # delete this char
                del_counter =  counter(start + 1, last, last_count, left - 1)
                return min(keep_counter, del_counter)
            
        return counter(0, "", 0, k)


# 重寫第二次, time complexity O(2^n), space complexity O(2^n)
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        memo = {}
        def dfs(start, last, last_count, k_count):
            if (start, last, last_count, k_count) in memo:
                return memo[(start, last, last_count, k_count)]
            memo[(start, last, last_count, k_count)] = None
            if k_count < 0:
                memo[(start, last, last_count, k_count)] = float("inf")
                return memo[(start, last, last_count, k_count)]
            if start >= len(s):
                memo[(start, last, last_count, k_count)] = 0
                return memo[(start, last, last_count, k_count)]
            if s[start] == last:
                incr = 1 if last_count in [1, 9, 99] else 0
                memo[(start, last, last_count, k_count)] = incr + dfs(start+1, last, last_count+1, k_count)
            else:
                keep = 1 + dfs(start+1, s[start], 1, k_count)
                delete = dfs(start+1, last, last_count, k_count-1)
                memo[(start, last, last_count, k_count)] = min(keep, delete)
            return memo[(start, last, last_count, k_count)]
        return dfs(0, "", 0, k)


# 重寫第三次, 這個考慮所有狀況, 比較直白, time complexity O(2^n), space complexity O(2^n)
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        memo = {}
        def dfs(start, last, last_count, k_count):
            if (start, last, last_count, k_count) in memo:
                return memo[(start, last, last_count, k_count)]
            memo[(start, last, last_count, k_count)] = None
            if k_count < 0:
                memo[(start, last, last_count, k_count)] = float("inf")
                return memo[(start, last, last_count, k_count)]
            if start >= len(s):
                memo[(start, last, last_count, k_count)] = 0
                return memo[(start, last, last_count, k_count)]
            if s[start] == last:
                incr = (1 if last_count in [1, 9, 99] else 0) + dfs(start+1, last, last_count+1, k_count)
                no_incr = dfs(start+1, last, last_count, k_count-1)
                memo[(start, last, last_count, k_count)] = min(incr, no_incr)
            else:
                keep = 1 + dfs(start+1, s[start], 1, k_count)
                delete = dfs(start+1, last, last_count, k_count-1)
                memo[(start, last, last_count, k_count)] = min(keep, delete)
            return memo[(start, last, last_count, k_count)]
        return dfs(0, "", 0, k)






