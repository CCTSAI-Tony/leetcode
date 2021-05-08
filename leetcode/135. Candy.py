'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
'''

#自己想的, time complexity O(n), space complexity O(n)
#思路: 前後順序遍歷, 看是否在哪一個方向可以形成更長的increasing sequence => 該位置可以拿到該連續sequence長度的糖果
#使用greedy, 每個位置選擇 前遍歷 or 後遍歷 可以得到最多糖果的一方(滿足連續increasing序列=>糖果遞增的狀況)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        n = len(ratings)
        if n == 1:
            return 1
        forward = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                forward[i] = forward[i-1] + 1
        backward = [1] * n
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                backward[i] = backward[i+1] + 1
        candies = [0]*n
        for i in range(n):
            candies[i] = max(forward[i], backward[i])
        return sum(candies)

#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        forward = [1] * n
        backward = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                forward[i] = forward[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                backward[i] = backward[i+1] + 1
        candy = [0] * n
        for i in range(n):
            candy[i] = max(forward[i], backward[i])
        return sum(candy)

