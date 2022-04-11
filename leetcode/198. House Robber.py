'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them 
is that adjacent houses have security system connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''
# 直接 in-place modified, time complexity O(n)
# 思路:就是类似动态规划的思想，对于第i间房子，每次都是考虑在从0间抢到第i间房子的情况下，所能抢到的最大值。这样走到最后一间房子，就是能抢到的最大值。
# 第一个 if i==1 是对于第 1 间，由于此时只有0 和 1 两间，选最大的作为 i=1 时，所能抢的最大值。
# 后面对于第i间，有两个选择： a) 抢这一间，即前一家不能抢 nums[i] + nums[i-2]. b) 不抢这一间，那么必然会抢前一间，用来保证最大nums[i-1]。 
# 至于a), b)情况为什么抢前一间或者前两间就会保证最大，
# 这就是动态规划的作用了，前一间是从0到前一间最大值。对于第n间和第m间，如果n<m, 不会出现 我们计算的n的值比m值大的情况。
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        for i in range(len(nums)):
            if i ==1:
                nums[i] = max(nums[0],nums[1])
            elif i >1:
                nums[i] = max(nums[i]+nums[i-2],nums[i-1])
        return nums[-1]


# 重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 1:
                nums[i] = max(nums[0], nums[1])
            if i > 1:
                nums[i] = max((nums[i] + nums[i-2], nums[i-1]))
        return nums[-1]


