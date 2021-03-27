# Given an array nums of integers, you can perform operations on the array.

# In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

# You start with 0 points. Return the maximum number of points you can earn by applying such operations.

# Example 1:

# Input: nums = [3, 4, 2]
# Output: 6
# Explanation: 
# Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points. 6 total points are earned.
 

# Example 2:

# Input: nums = [2, 2, 3, 3, 3, 4]
# Output: 9
# Explanation: 
# Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.
 

# Note:

# The length of nums is at most 20000.
# Each element nums[i] is an integer in the range [1, 10000].


Once you store the frequency of each number, you can easily see that it is like the House Robber problem:
#刷題用這個, time complexity O(max(nums) + 1), space complexity O(max(nums) + 1)
#思路: bottom up dp, 建立 freq數組 from 0 到 max(nums), 遍歷nums 使得freq[num] = 同一個num 的sum, 建立dp => dp[i] = max(dp[i] + dp[i-2], dp[i-1]) => house rubber 問題一樣
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        freq = [0] * (max(nums)+1)
        for n in nums:
            freq[n] += n

        dp = [0] * len(freq)
        dp[1] = freq[1] #因為nums[i] in range(1, 10000), 所以dp[0] = 0, dp[1] = freq[1]
        for i in range(2, len(freq)):
            dp[i] = max(freq[i] + dp[i-2], dp[i-1])  # 判斷delete自己 賺自己與i-2的dp, 還是delete 前一個 只賺前一個的dp

        return dp[-1]


#重寫第二次, time complexity O(max(nums) + 1), space complexity O(max(nums) + 1)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        freq = [0] * (max(nums) + 1)
        for num in nums:
            freq[num] += num
        dp = [0] * (max(nums) + 1)
        dp[1] = freq[1]
        for i in range(2, max(nums) + 1):
            dp[i] = max(freq[i] + dp[i - 2], dp[i - 1])
        return dp[-1]


#重寫第三次, time complexity O(max(nums) + 1), space complexity O(max(nums) + 1)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = [0] * (max(nums) + 1)
        for num in nums:
            freq[num] += num
        dp = [0] * len(freq)
        dp[1] = freq[1]
        for i in range(2, len(dp)):
            dp[i] = max(freq[i] + dp[i-2], dp[i-1])
        return dp[-1]



