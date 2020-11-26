'''
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. 
Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
'''

# Let's first consider the limiting behaviour of the solution.

# For large n, our "integer break" will consist of splitting up n into b groups of x. So n = bx, where rearranging yields b = n⁄x.

# Our goal is to maximize the product of these fragments, so we want to maximize f(x) = x^(n⁄x).

# Using implicit differentiation, we find f'(x) = n·x^(n⁄x - 2)·(1 - logx). Setting f'(x) = 0 gives x = e, so our objective function f(x) is maximized at x = e.

# 微積分請看https://www.youtube.com/watch?v=QQWDpBfWhp8

# Obviously, e is not an integer, so we cannot split n into groups of e for the purposes of this question. However, 
# this result gives us the intuition that n should be split into 2's and 3's, wherever possible, since 2 < e < 3.

# We begin by working through the first several cases of n and try to identify a pattern:

# n	Maximum Product	                  # of 2's         	   # of 3's
# 2	     1 x 1 = 1	                      0	                   0
# 3	     1 x 2 = 2	                      1                    0
# 4	     2 x 2 = 4	                      2	                   0
# 5	     2 x 3 = 6	                      1	                   1
# 6	     3 x 3 = 9	                      0	                   2
# 7	     2 x 2 x 3 = 12	                  2	                   1
# 8	     2 x 3 x 3 = 18	                  1	                   2
# 9	     3 x 3 x 3 = 27	                  0	                   3
# 10	 2 x 2 x 3 x 3 = 36	              2	                   2
# 11	 2 x 3 x 3 x 3 = 54	              1	                   3
# 12	 3 x 3 x 3 x 3 = 81	              0	                   4
# 13	 2 x 2 x 3 x 3 x 3 = 108	      2	                   3
# 14	 2 x 3 x 3 x 3 x 3 = 162	      1	                   4
# 15	 3 x 3 x 3 x 3 x 3 = 243	      0	                   5
# We can deduce a number of things from this table. First, a DP solution jumps out at us. Let dp[n] be the maximum possible product for integer n. 
# Starting at n=7, we notice that dp[n] = 3*dp[n-3]. We obtain the following O(n) solution:


# 刷題用這個, DP Implementation, time complexity O(n)
# 思路: 利用微積分 n = bx, where rearranging yields b = n⁄x. => f(x) = x^(n⁄x) => f'(x) = n·x^(n⁄x - 2)·(1 - logx) => f'(x) = 0 gives x = e
# 可以得知 x 在 2 or 3 其中一個, 因為 2 < e < 3
# 所以 n 希望全都由 2 or 3 組成, 並發現一個規律, n >= 7, dp[n] = 3 * dp[n-3]
class Solution:
    def integerBreak(self, n: int) -> int:
        case = [0,0,1,2,4,6,9] #n = 0, n = 1, no maximum product
        if n < 7:
            return case[n]
        dp = case + [0] * (n-6) #總共有n+1 個
        for i in range(7, n+1):
            dp[i] = 3*dp[i-3]
        return dp[-1]

#自己重寫
class Solution:
    def integerBreak(self, n: int) -> int:
        case = [0,1,1,2,4,6,9]
        dp = case + [0]*(n-6)
        for i in range(n+1):
            if i >= 7:
                dp[i] = dp[i-3] * 3
        return dp[n]




# (Note: we include the base cases for the invalid inputs of n=0 and n=1 to maintain alignment of the indexes of dp, avoiding the need for an offset.)



# However, we aren't done yet. If we look a little more carefully at the above table, we see that the powers of 2 and 3 follow a pattern.

# The "power of 2" pattern is fairly easy to spot. Starting at n=4, the number of 2's repeats the cycle of 2,1,0. So the "2 exponent" 
# in the maximum product can be expressed as (-n)%3.

# The "power of 3" pattern is similar, but slightly harder to express. Again, the pattern starts at n=4 and has a period of length 3. 
# This time, the numbers in each cycle are all one more than the numbers in the previous cycle. 0,1,2 , 1,2,3 , 2,3,4 , ... . 
# We figure out that we can express this "3 exponent" as ((n-1)%3) + (n-4)//3. The first term handles the periodic behavior and 
# the second term captures the perpetual increases between cycles.

# We now have an explicit formula to solve the problem, solving in O(1) time. Since the only special cases of n=2 and n=3 
# have maximum products of 1 and 2 respectively, we can handle everything in one line:

# Explicit Formula Implementation:

def integerBreak(self, n: int) -> int:
    return int(math.pow(2, (-n)%3) * math.pow(3, (n-1)%3 + (n-4)//3)) if n > 3 else n-1


# (Credit to totsubo for correcting my initial error of using ** instead of math.pow() - we cannot use ** if we want to preserve constant time complexitcomplex

















