'''
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000

'''
'''
scan for all the arith slices (as long as poosible);
let 'x' be the number of arith slice for slice with length 'n',
if n==3: x = 1
if n==4: x = 1+2 # 1 slice with length 4; 2 slices with length 3;
if n==5: x = 1+2+3 # 1 slice with length 5; 2 slices with length 4; 3 slices with length 3
....
if n==m: x = 1+2+...+(m-2) = (m-2)*(m-2+1)/2 = (m-2)*(m-1)/2
'''
# 刷題用這個, time complexity will be O(n), space complexity O(1)
# 思路: 處於同一個arithmetic array, 長度為n 則有 (n-2)*(n-1)//2 個 sub arithmetic array, 起碼要有三個elements 才能算 arithmetic array
# 進入新的arithmetic array, cnt, diff 都要reset
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if not A or len(A) < 3: 
            return 0
        res = 0
        cnt, diff = 2, A[1] - A[0] # cnt 代表目前arithmetic array 有幾個elements
        for i in range(2, len(A)):
            if A[i] - A[i-1] == diff: #處於同一個arithmetic array
                cnt += 1
            else:
                if cnt > 2: 
                    res += ((cnt-1)*(cnt-2))//2
                cnt, diff = 2, A[i] - A[i-1] #進入新的 arithmetic array
        if cnt > 2: # 脫離for loop 的計算
            res += ((cnt-1)*(cnt-2))//2
        return res











