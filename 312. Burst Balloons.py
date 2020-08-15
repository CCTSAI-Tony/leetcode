'''
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. 
You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. 
Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''
ex: dp[3][8] = dp[3][5] + dp[5][8] + 3*5*8 其中 dp[5][8] = 0, dp[3][5] = 15, => nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]
# We need to find a way to divide the problems. If we start from the first balloon, we can't determine the left/right for the number in each sub-problem,
# If we start from the last balloon, we can determine the left/right, dp[left][right]. 
# 這裡指的first balloon 是指第一個順序燒掉的氣球, last balloon 是指最後一個順序燒掉的氣球, 注意是順序不是index
# We can see the transformation equation is very similar to the one for matrix multiplication.

# 思路: dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]) # i < k < j, dp[left][right]
# This is a typical interval DP problem. Because the order of the number extracted matters, we need to do a O(n^3) DP. like matrix multiplication i,j,k
# If we only need to expand the interval to the left or right, we only need to do a O(n^2) DP. 只允許往左or往右照順序爆破, 可以沒有k這個參數

# Top-down: time complexity: O(n^3), 724ms
# 解題用這個 top-down 比較直覺
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]  #前後各加1
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        return self.calculate(0, n-1, dp, nums)

    def calculate(self, i, j, dp, nums):
        if dp[i][j] or j == i + 1: # in memory or gap < 2, if dp[i][j] != 0 or j == i + 1 這個條件很重要, 代表i,j之間沒有氣球可以爆
            return dp[i][j]
        coins = 0 #初始值
        for k in range(i+1, j): # find k, the last balloon to bust between i, j
            coins = max(coins, nums[i] * nums[k] * nums[j] + self.calculate(i, k, dp, nums) + self.calculate(k, j, dp, nums)) #理解為最後一個氣球k在哪爆是最大值, 利用max取得最佳解
        dp[i][j] = coins
        return coins

        #請用最簡單的例子比較好想通 nums[6]>[1,6,1],calculate(0, 1)==0, calculate(1, 2)==0, nums[0] * nums[1] * nums[2] = 6, calculate(0, 2)==6
        #這題精華在於gap < 2 return dp[i][j]==0
        #nums[3,4,5]>[1,3,4,5,1] 假設最後爆破k = 2 產生最大值, 比較好想 3,5爆破 再來4
        #nums[3,4,5,6,7]>[1,3,4,5,6,7,1]>假設最後爆破k = 3 產生最大值
        @@#這種nested function 的寫法, 最主要是利用nested func local variable 不需定義, 自動直接參照上層的local variable
        @@#與非nested func的寫法最大差在local variable 要手動定義在參數上,使其連結特定變數




# bottom-up version with explanation:
# time complexity: O(n^3)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]   # padding, build the complete array 
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for gap in range(2, n): #bottom-up 從小gap到大gap, 但注意跳過gap = 1
            for left in range(n - gap):
                right = left + gap
                for i in range(left+1, right):
                    # dp[left][right] = the maximum coins we get after bursting all the balloons between left and right (excluding left and right themselves)
                    dp[left][right] = max(dp[left][right], dp[left][i] + dp[i][right] + nums[left]*nums[i]*nums[right]) #理解為最後一個氣球i在哪爆是最大值, 利用max取得最佳解
                                        # maximum coins of bursting all the balloon on the left side of i
                                        # maximum coins of bursting all the balloon on the right side of i
                                        # bursting balloon i last when left side and right side are gone
        return dp[0][n-1]   # since we pad nums on both sides with [1], it really covers the entire range of the original nums (remember boundaries are excluded)


#自己重新寫一次
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        for gap in range(2, len(nums)):
            for left in range(len(nums) - gap):
                right = left + gap
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[left]*nums[i]*nums[right] + dp[left][i] + dp[i][right])
        return dp[0][len(nums)-1]











