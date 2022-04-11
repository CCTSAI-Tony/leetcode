'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

# 請與53一起服用, 刷題用這個
# 自己重寫, time complexity O(n), 112ms
# 思路: 利用dp[i] = [max_so_far, min_so_far], 下一個 dp[i+1] => 可以從nums[i+1] 開始, 也可以乘上前面數值
# dp[i+1] = [max(nums[i+1], nums[i+1]*dp[i][0], nums[i+1]*dp[i][1]), min(nums[i+1], nums[i+1]*dp[i][0], nums[i+1]*dp[i][1])]
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [[0,0] for _ in range(len(nums))] #不能用(0,0) 因為tuple不能 assaign 值
        dp[0] = [nums[0], nums[0]]
        for i in range(1, len(nums)):
            dp[i][0] = max(nums[i]*dp[i-1][0], nums[i]*dp[i-1][1], nums[i]) #nums[i] 在裡面, 代表subarray可以從自己開始, 不需要前人的數值
            dp[i][1] = min(nums[i]*dp[i-1][0], nums[i]*dp[i-1][1], nums[i])
        return max(dp[i][0] for i in range(len(nums)))


#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [(nums[0], nums[0])]
        for i in range(1, len(nums)):
            temp = [0, 0]
            temp1 = nums[i] * dp[i-1][0]
            temp2 = nums[i] * dp[i-1][1]
            temp[0] = max(temp1, temp2, nums[i])
            temp[1] = min(temp1, temp2, nums[i])
            dp.append(temp)
        return max(i[0] for i in dp)

# 重寫第三次, time complexity O(n), space complexity O(n)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[nums[0], nums[0]]]
        for i in range(1, len(nums)):
            temp = [0, 0]
            temp[0] = min(dp[-1][0] * nums[i], dp[-1][1] * nums[i], nums[i])
            temp[1] = max(dp[-1][0] * nums[i], dp[-1][1] * nums[i], nums[i])
            dp.append(temp)
        return max(x[1] for x in dp)


#dp, bottom up
class Solution:
    def maxProduct(self, nums: List[int]) -> int
        
        ans = max_so_far = min_so_far = nums[0] #第一個值為初始
        
        for i in range(1, len(nums)):
            
            candidates = (nums[i], max_so_far*nums[i], min_so_far*nums[i])
            max_so_far = max(candidates)
            min_so_far = min(candidates)
            ans = max(ans, max_so_far)
        
        return ans

'''
If the array had all positive numbers, then the max product includes all the elements in the array

As we have +ve, -ve integers and 0 in the input array, there are 3 choices at every index i

Max product starts at nums[i]
Max product is obtained by multiplying nums[i] with the minimum product so far
Max product is obtained by mulitiplying nums[i] with the maximum product so far

'''





#這個方法跟上面一樣
from functools import reduce
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
            if min(nums)>0:
                return reduce(lambda x, y: x*y, nums)  #you do not have to use reduce here 若全部都是正就全部乘在一起
            size = len(nums)
            dp = [[1,1]]*size #注意不能用 [1,1] * size 
            dp[0]=[nums[0],nums[0]]#dp[0][0] indicate max and dp[0][1] indicate min
            for i in range(1, size):
                if nums[i]==0:
                    dp[i]=[0,0]
                elif nums[i]>0:
                    cur_max = max(max(dp[i-1])*nums[i], nums[i])
                    cur_min = min(min(dp[i-1])*nums[i], nums[i])
                    dp[i]=[cur_max, cur_min]
                else:
                    cur_max = max(min(dp[i-1])*nums[i], nums[i])
                    cur_min = min(max(dp[i-1])*nums[i], nums[i])
                    dp[i]=[cur_max, cur_min]
            return max([x[0] for x in dp])


'''
There is a better way to solve the question, this is the basic idea of using dynamic programming. You can optimaze this code based on it!

We need to track both maxmium product of subarray and minimum product of subarray. 
The reason of tracking minimun product of subarray is if there are even amount of negative numbers, 
then there is possiblility that the last negative number multiple previous mininum product of subarray (which ic negative) can be the maximum product of subarray.

There are two conditions need to consider:

If all number are positive, the maximum product of subarray is product of all subarray.

If not all numbers are positive, then we need to consider the previous product and current number, 
since we keep tracking the both maximum and minimum product of subarray, so each time you have two selections of subarry product for the current number:

If current number is positive, then the current maximum product of subarray 
is always max(max(max_pre_product, min_pre_product) x number, number) = current_max_product 
and the minimum product of subarray is always min(min(max_pre_product, min_pre_product) x number, number) = current_min_product.

If current number is negative, then the current maximum product of subarray 
should be max(min(max_pre_product, min_pre_product) x number, number) = current_max_product,
the current minimum product of subarray is min(max(max_pre_product, min_pre_product) x number, number) = current_min_product

3.** If current number is 0, then both current maximum product and minimum product will be 0.**

The result will be max of all maximum_subarrays because the 0 is inclusive in this question. 0 will make the subarray discontinue, 
therefore, if 0 exists, there may be more than one maximum_subarray and minimum_subarray. 
If 0 is exclusive, then there is only maximum_subarray and minimum_subarray, therefore we can return max(dp[-1]) as result.

'''

>>>def add(x, y) :            # 两数相加
...     return x + y
... 
>>> reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
15
>>> reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数






















