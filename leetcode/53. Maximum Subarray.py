# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

#請與53一起服用
#自己想的, time complexity O(n) 84ms
#思路: 利用dp, dp[i] 是當下最佳情況, 若dp[i-1] + nums[i] > nums[i], dp[i] 就加入前面的序列, 再從dp 選最大的
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [float(-inf)] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)

#修改代碼, 利用tp, print 出最佳方案
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [float(-inf)] * len(nums)
        dp[0] = nums[0]
        tp=[[] for _ in range(len(nums))] #重要, 不能 [[]]*len(nums), 複製出來的東西都是指向同一個記憶體位置
        tp[0] = [nums[0]]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            if dp[i] == dp[i-1]+nums[i]:
                tp[i] = tp[i-1] + [nums[i]] #不能 tp[i] = tp[i-1].append(nums[i]), tp[i-1].append(nums[i]) => None
            else:
                tp[i] += [nums[i]]
        max_index = dp.index(max(dp))
        print(tp[max_index])
        return max(dp)

[-2,1,-3,4,-1,2,1,-5,4] => nums
[4, -1, 2, 1] => 最佳方案
6 => sum最大

#自己想的, time complexity O(n), space complexity O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s, e = 0, 0
        cur_sum = nums[0]
        max_sum = nums[0]
        for e in range(1, len(nums)):
            if nums[e] > cur_sum + nums[e]:
                cur_sum = nums[e]
            else:
                cur_sum += nums[e]
            max_sum = max(max_sum, cur_sum)
        return max_sum


#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)










# Divide conquer easy to understand, 316ms
# time complexity O(nlogn)
# 思路: 模板2思想, 選定一個中間值=> 中間值+左右連續區間最大subarray的值 vs 不包含中間值的max(左,右)
class Solution:
    def maxSubArray(self, nums):
        return self.maxSubArrayHelper(nums, 0, len(nums) - 1)

    def maxSubArrayHelper(self,nums, l, r):
        if l > r:
            return float(-inf) #無效序列, 所以return 最小值
        m = (l+r) // 2
        
        leftMax = sumNum = 0
        for i in range(m - 1, l - 1, -1):
            sumNum += nums[i]
            leftMax = max(leftMax, sumNum)
        
        rightMax = sumNum = 0
        for i in range(m + 1, r + 1):
            sumNum += nums[i]
            rightMax = max(rightMax, sumNum)
            
        leftAns = self.maxSubArrayHelper(nums, l, m - 1)
        rightAns = self.maxSubArrayHelper(nums, m + 1, r)
            
        return max(leftMax + nums[m] + rightMax, max(leftAns, rightAns))

#自己重寫, time complexity O(nlogn), space complexity O(logn)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        return self.helper(l, r, nums)
    
    def helper(self, l, r, nums):
        if l > r:
            return float("-inf")
        m = l + (r-l) // 2
        left_max, sum_l = 0, 0
        for i in range(m-1, l-1, -1):
            sum_l += nums[i]
            left_max = max(left_max, sum_l)
        right_max, sum_r = 0, 0
        for i in range(m+1, r+1):
            sum_r += nums[i]
            right_max = max(right_max, sum_r)
        return max(left_max + nums[m] + right_max, max(self.helper(l, m-1, nums), self.helper(m+1, r, nums)))
            



#重寫第二次, time complexity O(nlogn), space complexity O(logn)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums) - 1)
    
    def helper(self, nums, l, r):
        if l > r:
            return float("-inf")
        mid = l + (r - l) // 2
        leftSum = 0
        curSum = 0
        for i in range(mid - 1, l - 1, -1):
            curSum += nums[i]
            leftSum = max(leftSum, curSum)
        rightSum = 0
        curSum = 0
        for i in range(mid + 1, r + 1):
            curSum += nums[i]
            rightSum = max(rightSum, curSum)
        left = self.helper(nums, l, mid - 1)
        right = self.helper(nums, mid + 1, r)
        return max(leftSum + rightSum + nums[mid], left, right)








class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

    '''
    个人理解：每一个nums[i]的值都表示，截止到目前为止，前面所有可能的countinuous array的最大的和。ps向能想出这个算法的人致敬！太厉害了！

    这就是动态规划的基本思想啊，nums 里面存储的就是子问题的最优解。


    '''

class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum    
'''
這也是dynamic programming 且 memory usage 比上個好
'''