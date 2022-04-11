'''
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], 
where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.

 

Example 1:

Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.
Example 2:

Input: n = 6, k = 1, maxPts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.
Example 3:

Input: n = 21, k = 17, maxPts = 10
Output: 0.73278
 

Constraints:

0 <= k <= n <= 104
1 <= maxPts <= 104
'''

# The question ask us to play a game:

# let X = 0
# while X <= K:
#     X += draw a sample from W, where W = [1, 10]
# and figure out that, at the end of the game, what's the probability

# P( X ≤ N | X ≥ K) ？
# For each probablity X = i, it is the relation:

# P( X = i ) = (P( X = i - 1) + P ( X = i - 2 ) + .... P ( X = i - W )) / W, where i > W
# For example,

# P( X = 0 ) = 1                           # Initial state, no need to draw cards
# P( X = 1 ) = 1/W                         # Only 1 out of W chance in getting X = 1
# P( X = 2 ) = 1/W + 1/W^2                 # We can draw a 2 or two 1s.
# P( X = 3 ) = 1/W + 1/W^2 + 1/W^2 + 1/W^3 # We can draw a 3, a (2,1), a (1,2), and three 1s. 
# P (X = 4 ) = ( P( X = 3 ) + P( X = 2 ) ) / W
# .etc
# The above sequence is similar to climbing stairs or Fibo series, except, this time, we would be updating probabilities.

# Thus, we can represent the above probabilities with an array of length N + 1 and add up the probabilities between [K, N]. ==> >=k 停止, 求 <= n的機率

# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: 機率問題, 解法請看上面
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:  # n >= k + maxPts 代表不管怎麼抽, 就算抽到k + maxPts 停止抽了, 也是<= n
            return 1
        dp = [1] + [0] * n
        res = 0
        wsum = 1.0
        for i in range(1, n+1):
            dp[i] = wsum / maxPts
            if i < k:  # 小於k, 機率還能再加
                wsum += dp[i]
            else:
                res += dp[i]
            if i - maxPts >= 0:  # 這裡重要, 去除離超過maxPts機率, 因為抽牌最多增加 maxPts 分數
                wsum -= dp[i-maxPts]
        return res


