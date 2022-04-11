'''
You have n coins and you want to build a staircase with these coins. 
The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
 

Constraints:

1 <= n <= 231 - 1
'''

# 刷題用這個, time complexity O(logn)
# 思路: binary search
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n // 2 + 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.stair_sum(mid) >= n:
                r = mid
            else:
                l = mid
        if self.stair_sum(l) >= n:
            if self.stair_sum(l) == n:
                return l
            else:
                return l - 1
        else:
            if self.stair_sum(r) == n:
                return r
            else:
                return r - 1
        
    def stair_sum(self, m):
        return (1 + m) * m // 2