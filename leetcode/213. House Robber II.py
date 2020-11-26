'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, 
adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
'''
# Since House[1] and House[n] are adjacent, they cannot be robbed together. 
# Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money. 
# Now the problem has degenerated to the House Robber, which is already been solved.


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        if n == 3:
            return max(nums[0],nums[1],nums[2]) #只能偷其中一家
        dp1,dp2 = [0]*n,[0]*n
        
        dp1[0],dp1[1] = nums[0], max(nums[0],nums[1])
        for i in range(2,n-1):
            dp1[i] = max(dp1[i-2]+nums[i],dp1[i-1]) #dp1[i-2]+nums[i] 精華所在,偷這家繼承前前家, or 不偷這家繼承前家
        dp2[1],dp2[2] = nums[1], max(nums[1],nums[2])
        for i in range(3,n):
            dp2[i] = max(dp2[i-2]+nums[i],dp2[i-1])
        return max(max(dp1),max(dp2))
'''
check for house 1 to n-1 and then check for 2 to n and maximize over both
'''

#自己重寫, 刷題用這個
#time complexity O(n)
# 思路: dp[i] 代表到ｉ棟房子我們最多可以偷多少錢, dp[i] = max(偷這家與繼承到前前家可以偷的最大值, 不偷這家與繼承到前家可以偷的最大值), optimal subproblem
# 此題特別的是, 第一棟與最後一棟相連, 也就是要偷第一棟就不能偷最後一棟, 因此問題可以切分成 排除第一棟與排除最後一棟的序列, 這樣就能避免相連的問題
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)
        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])  #注意, dp1[1] 代表到index = 1 的房子最多可以偷多少錢, 還要考慮 index= 0 的房子
        dp2[1], dp2[2] = nums[1], max(nums[1], nums[2])  #排除 index = 0 的房子
        
        
        for i in range(2, len(nums)-1):  #排除最後一棟房子
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])
            
        for j in range(3, len(nums)):  #排除 index = 0 的房子
            dp2[j] = max(dp2[j-2] + nums[j], dp2[j-1])
        
        return max(max(dp1), max(dp2))



