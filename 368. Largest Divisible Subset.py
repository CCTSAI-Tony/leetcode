'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0. #注意這個or 滿足其中一個即可

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
'''

# First of all, notice, that if we need to find 3 numbers given properties, than if we put then in decreasing order a > b > c, 
# than it is sufficient and enough that a%b = 0 and b%c=0, then it is automatically a%c=0.

# Let us know sort our number and in sol[i] list keep the best solution, where the biggest number is equal to nums[i]. 
# How can we find it? Look at all smaller numbers and if nums[i] is divisible by this smaller number, we can update solution. 
# Let us go through example: nums = [4,5,8,12,16,20].

# sol[0] = [4], the biggest divisible subset has size 1.
# sol[1] = [5], because 5 % 4 != 0.
# sol[2] = [4,8], because 8 % 4 = 0.
# sol[3] = [4,12], because 12 % 4 = 0.
# sol[4] = [4,8,16], because 16 % 8 = 0 and 16 % 4 = 0 and we choose 8, because it has longer set.
# sol[5] = [4,20] (or [5,20] in fact, but it does not matter). We take [4,20], because it has the biggest length and when we see 5, we do not update it.
# Finally, answer is [4,8,16].
# Complexity: time complexity is O(n^2), because we fist sort our numbers and then we have double loop. Space complexity also potentially O(n^2), 
# but for big n, length of the longest subset will not be more than 32: (each time you new number will be at least twice bigger than previous, 
#     so there will be maximum 32 numbers in our set) so so we can say it is O(32n).

# Possible improvements
# Note similarity of this problem with problem 300 Longest Increasing Subsequence, 
# however it is different, and we can not apply O(n log n) algorighm here directly, when we add new number we can not use binary search.
# There is idea by @yanrucheng with comlexity O(nlogn + n*sqrt(V)), where V is the biggest number. 
# I am interested, if there is O(n log n) solution here? If you know such method please let me know!

# 刷題用這個, time complexity O(n^2), space complexity O(n^2) 因為是subsets
# 思路: 一開始sorted(nums), 再利用i,j指針, i比j大, j指針遍歷比i指針小的值
# 大的值 % 小的值 == 0, 代表 大的值 % 小的值所處的subset的所有值 都是 = 0
# 若len(nums) == 1, ans: [nums[i]]
class Solution:
    def largestDivisibleSubset(self, nums):
        if len(nums) == 0: 
            return []
        nums.sort()
        sol = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(sol[i]) < len(sol[j]) + 1:
                    sol[i] = sol[j] + [nums[i]]
        return max(sol, key=len)

        # max(sol, key=len), 以長度決定最大值

#自己重寫
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        dp = [[nums[i]] for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) >= len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)




# Can any1 tell me why do we need judge 'len(dp[i]) >= len(dp[j])'?

# bcos no need to consider shorter length result compared to the currnet one.

# for i in reversed(range(5)):
#     print(i)

# 4
# 3
# 2
# 1
# 0

# for i in reversed(range(0,5)):
#     print(i)

# 4
# 3
# 2
# 1
# 0



# for i in (range(5,-1,-1)):
#     print(i)
# 5
# 4
# 3
# 2
# 1
# 0

# res = [[1],[1,2],[1,2,3],[1,2,3,4],[0,1,2,3,4,5]]
# max(res, key=len) 

# [0, 1, 2, 3, 4, 5]

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        # (previous divisible index, length of divisible subset)
        dp = [(-1, 1)] * n
        # (last divisible index, maximum length of divisible subsets)
        maxl = (0, 1)
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i][1] < dp[j][1] + 1:
                        dp[i] = (j, dp[j][1] + 1)
                        if maxl[1] < dp[i][1]:
                            maxl = (i, dp[i][1])
        ret = []
        x = maxl[0]
        while x > -1:
            ret.append(nums[x])
            x = dp[x][0]
        return ret[::-1]





