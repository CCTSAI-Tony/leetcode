'''
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
'''




# Explanation: Take the example in the question, where nums is [1, 2, 3] and the target is 4. 
# Here's how you would build the solution bottom up by starting with the ways you can make a total of 1, 
# then the number of ways you can make a total of 2, and so on up to 4:

# 1 -> [1]
# 2 -> [1, 1], [2]
# 3 -> [1, 1, 1], [1, 2], [2, 1], [3]
# 4 -> [1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1]

# Since we just need the counts, not the actual combinations, this can be simplified to the following DP algorithm:

# Pre-Step: Initialize the DP array to be 1 for each number in nums (since you can trivially make that total by just using that number itself) and 0 otherwise.
# DP = [0, 1, 1, 1, 0]

# Now for each number on the way to our target, call that sub-target t_sub. (t_sub must > 0)
# See how many ways we can make t_sub by taking each number n in nums and checking how many ways we were able to make t_sub - n then adding that to the DP entry for t_sub.

# Step 1:
# t_sub = 1 [1]
# t_sub - 1 = 0 so add nothing
# t_sub - 2 < 0 so add nothing
# t_sub - 3 < 0 so add nothing
# DP = [0, 1, 1, 1, 0]

# Step 2:
# t_sub = 2 [2]
# t_sub - 1 = 1 so DP[2] += DP[1] and is now 2, add [1,1]
# t_sub - 2 = 0 so add nothing
# t_sub - 3 < 0 so add nothing
# DP = [0, 1, 2, 1, 0]

# Step 3:
# t_sub = 3 [3]
# t_sub - 1 = 2 so DP[3] += DP[2] and is now 3, add [1,1,1], [2,1]
# t_sub - 2 = 1 so DP[3] += DP[1] and is now 4, add [1,2]
# t_sub - 3 = 0 so add nothing
# DP = [0, 1, 2, 4, 0]

# Step 4:
# t_sub = 4
# t_sub - 1 = 3 so DP[4] += DP[3] and is now 4, add[1,1,1,1],[2,1,1],[1,2,1],[3,1]
# t_sub - 2 = 2 so DP[4] += DP[2] and is now 6, add[1,1,2],[2,2]
# t_sub - 3 = 1 so DP[4] += DP[1] and is now 7, add[1,3]
# DP = [0, 1, 2, 4, 7]

# Now we are finished, so return DP[-1], which is the number of ways we can make t_sub when t_sub is the target.


#此問題只問幾種排列, 不同順序算不同排列
#dp[0] 沒有組合add up =0
#dp[x<0] 沒有組合add up x < 0
#這題很棒 bottom up, loop invariant, 每個dp entry 裡面的排列都不會有重複 所以adds up 起來 後面的dp entry 一樣不會有重複
#Given an integer array with all positive numbers and @@ no duplicates 已經確保每個dp[i]都是沒有重複的排列
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1) #包含0
        for num in nums:
            if num <= target:  #因為 dp array 最多index只到 target
                dp[num] = 1
        for i in range(target+1):  #bottom up
            for num in nums:
                if i - num > 0:
                    dp[i] += dp[i-num]
        return dp[-1]


#自己重寫 time complexity O(n*len(nums)), 不用先對nums做排序, 因為建立dp時是 bottom up
#思路: 因為不同排列順序也算一種加上nums裡沒有duplicates, 所以沒有重複的問題
#dp[i] += dp[i-num] if (i-num) > 0, 代表dp[i-num]裡面所有元素 + num = target, 幾種組合直接繼承dp[i-num]
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1) #non-zero based index 比較好理解
        for i in range(target+1):
            if i in nums:
                dp[i] = 1
        for i in range(target+1):
            for num in nums:
                if i - num > 0:
                    dp[i] += dp[i-num]
        return dp[target]



# time complexity O(n*len(nums))
# This is DFS backtracking + memo
# 思路: 有重複的路徑所以用到memo
class Solution(object):
    def combinationSum4(self, nums, target):
        nums.sort() #優化
        self.memorize = {}
        return self.dfs(target, nums)

    def dfs(self, target, nums):
        if target in self.memorize:
            return self.memorize[target]
        
        cnt = 0
        for num in nums:
            if num > target:
                break  #因為 nums.sort(), 提早結束迴圈, 若沒有sort 就continue, 
            elif num == target:
                cnt += 1
                break #因為 nums.sort(), 提早結束迴圈
            else:
                cnt += self.dfs(target - num, nums)
        
        self.memorize[target] = cnt
        return cnt



# DP finds the solution by starting from the base case(s) and works its way upwards. DP solves all the sub-problems, because it does it bottom-up

# Unlike Memoization, which solves only the needed sub-problems








