'''
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)



Example 1:

Input: "banana"
Output: "ana"
Example 2:

Input: "abcd"
Output: ""


Note:

2 <= S.length <= 10^5
S consists of lowercase English letters.
'''

# Intuition
# Suffix array is typical solution for this problem.
# The fastest way is to copy a template form the Internet.
# The code will be quite long.
# Here I want to share a binary search solution.


# Explanation
# Binary search the length of longest duplicate substring and call the help function test(L).
# test(L) slide a window of length L,
# rolling hash the string in this window,
# record the seen string in a hashset,
# and try to find duplicated string.

# I give it a big mod for rolling hash and it should be enough for this problem.
# Actually there could be hash collision.
# One solution is to have two different mod for hash.
# Or we can use a hashmap to record the index of string.


# Complexity
# Binary Search in range 1 and N, so it's O(logN)
# Rolling hash O(N)
# Overall O(NlogN)
# SpaceO(N)


# [Python] Binary Search

import functools
class Solution:
    def longestDupSubstring(self, S):
        A = [ord(c) - ord('a') for c in S]  # 轉換成數字 ord("a") => 97
        mod = 2**63 - 1

        def test(L):
            p = pow(26, L, mod)
            cur = functools.reduce(lambda x, y: (x * 26 + y) % mod, A[:L])
            seen = {cur}  # set
            for i in range(L, len(S)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen:
                    return i - L + 1  # 第二個duplicate string 開頭的index, 跟 A[i - L] 有關
                seen.add(cur)

        res, lo, hi = 0, 0, len(S)
        while lo < hi:  # 左閉右開
            mi = (lo + hi + 1) // 2
            pos = test(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return S[res:res + lo]


# 2. float pow(x,y,mod) : This function computes (x**y) % mod. This function first converts its arguments into float and then computes the power.

# print (pow(3,4,10))

# The value of (3**4) % 10 is : 1


@@
# Why use binary search
# Since the length of the answer must between 0 to the length of string minus 1, In the example one "banana",
# the answer must between 0 to 5, we can guess 3 at the first time. We will check every possible substring with length 3 to see if we can find any duplicate.
# - ban
# - ana
# - nan
# - ana
# If we are lucky enough, like this case, 'ana' is what we want. since we want to get the longest one,
# so we guess 4 (middle of 3 and 5) in the next time, if we found any valid answer, we can update the old one.
# How to check duplicate substring
# The easiest way would be to use a hashmap or dictionary to store the substring (or the hash value of the substring).
# If the current string not in the hashmap, we put it in the hashmap, if it already existed, we return the string.
# hashmap = {}
# ban -> not in the hashmap -> hashmap = {ban}
# ana -> not in the hashmap -> hashmap = {ban, ana}
# nan -> not in the hashmap -> hashmap = {ban, ana, nan}
# ana -> in the hashmap -> return 'ana'
# But we will get Memory Limit Exceeded in leetcode if we did this.
# So we have to implement our own hash function by calculated a unique number for every substring then compare between them.
# This is kinda hacking, In the answer from @lee215,
#    def test(L):
#            p = pow(26, L, mod)
#            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L])
#            seen = {cur}
#            for i in range(L, len(S)):
#                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
#                if cur in seen: return i - L + 1
#                seen.add(cur)
# banana_val -> [b,a,n,a,n,a] -> [1, 0, 13, 0, 13, 0] (we give every char a number)
# ban -> ((1 * 26 + 0) * 26) + 13 = 689
# ana -> ban + a - b = (689 * 26) + 0 - 26 * 26 * 26 * 1 = 338 ( the current b had been multiple by 26 three times)
# ...
# Any finally we get 338 again, so we return 'ana'.
# reduce() in Python
# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned
# in the sequence passed along.This function is defined in “functools” module.
# import functools
# # initializing list
# lis = [ 1 , 3, 5, 6, 2, ]
# # using reduce to compute sum of list
# print ("The sum of the list elements is : ",end="")
# print (functools.reduce(lambda a,b : a+b,lis))
# # using reduce to compute maximum element from list
# print ("The maximum element of the list is : ",end="")
# print (functools.reduce(lambda a,b : a if a > b else b,lis))
# The sum of the list elements is : 17
# The maximum element of the list is : 6
# Complexity
# Binary Search in range 1 and N, so it's O(logN)
# Rolling hash O(N)
# Overall O(NlogN)
# SpaceO(N)


# 模板2, 刷題用這個 time complexity O(nlogn), space complexity O(n), Binary Search in range 1 and N, so it's O(logN), Rolling hash(test) O(N)
# 思路: 先把所有字母轉化成ord(c), 建立test helper, 功用為確認是有input(l) 長度的重複字串, 1 <= l <= len(S)
# 如何實現, 因為字串順序也要考慮, ex:abc => a*26^3 + b*26^2 + c*26 得到的值只有同樣順序的字串才能一樣 => fix l 長度的wondow 得到每個一樣長度連續字串的值
# 把值存進dict裡, 若之後有一樣值的字串代表這個長度的字串有duplicated, 回傳duplicated 字串的起點index
# 利用helper 搭配 binary search 就能確認最大長度的substring
# 因為文字轉化的數字有可能很大, 所以使用mod 來減少數值大小, 通常長度過長的字串才會超過mod, 被mod過後的值不用怕覆蓋沒mod但一樣的值, 
# 因為mod取很大 沒mod但一樣的值的狀況不會出現, 若mod取比較小就有可能發生覆蓋的狀況
import functools
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1  # 這裡mode的功用是讓cur 不要過於龐大, 不然會TLE
        # why len(S), 而不是 len(S)-1, 注意這裡不是string index, 而且長度且len(S) 是被included
        lo, hi = 1, len(S)
        while lo + 1 < hi:
            mi = (lo + hi) // 2
            pos = self.test(mi, A, S, mod)
            if pos:
                lo = mi
            else:
                hi = mi
        pos_hi, pos_lo = self.test(hi, A, S, mod), self.test(lo, A, S, mod)
        if pos_hi:
            return S[pos_hi:pos_hi + hi]
        elif pos_lo:
            return S[pos_lo:pos_lo + lo]
        return ""

    def test(self, L, A, S, mod):
        p = pow(26, L, mod) #最左邊的值需要乘上的數
        cur = functools.reduce(lambda x, y: (x * 26 + y), A[:L])  # 這邊把文字轉化成數字的技巧真是太厲害了
        seen = {cur % mod} #set
        for i in range(L, len(S)):
            # trick point, -1 % 1000=> 999, mod太難了這行背起來
            cur = (cur * 26 + A[i] - A[i - L] * p) % mod
            if cur in seen:
                return i - L + 1
            seen.add(cur)

# 也可以 cur = ((cur * 26) % mod + A[i] - A[i - L] * p)  % mod

# float pow(x,y,mod) : This function computes (x**y) % mod.
# 一開始cur 有被mod, 那麼 p 也有被mod, 但p 沒被mod,update的 cur 有可能超過mod
# 若一開始 p 有被mod 但 cur 沒被mod, 那麼update的 cur 也要被mod
