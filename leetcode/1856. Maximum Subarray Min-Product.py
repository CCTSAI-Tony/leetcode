'''
The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.

For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.
Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. Since the answer may be large, return it modulo 109 + 7.

Note that the min-product should be maximized before performing the modulo operation. 
Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.
Example 2:

Input: nums = [2,3,3,1,2]
Output: 18
Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
3 * (3+3) = 3 * 6 = 18.
Example 3:

Input: nums = [3,1,5,6,4,2]
Output: 60
Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
4 * (5+6+4) = 4 * 15 = 60.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 107
'''

# time complexity O(n), space complexity O(n)
# 思路: 靜態數組 + monotonic queue, why n + 2, 建立哨兵來避免邊界判斷問題 => 好技巧!
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0] * (n + 2)
        q = [0] * (n + 2)
        h = [0] * (n + 2)
        l = [0] * (n + 2)
        r = [0] * (n + 2)
        for i in range(1, n + 1):
            h[i] = nums[i - 1]
            s[i] = s[i - 1] + h[i]
        q = [0]
        for i in range(1, n + 1):
            while h[i] <= h[q[-1]]: #若當前數值 <= 前一個數值, 之前元素 >= 前一個數值都可以直接跳過
                q.pop()
            l[i] = q[-1]
            q.append(i)
        q = [n+1]
        for i in range(n, 0, -1):
            while h[i] <= h[q[-1]]:
                q.pop()
            r[i] = q[-1]
            q.append(i)
        res = 0
        for i in range(1, n + 1):
            res = max(res, h[i] * (s[r[i] - 1] - s[l[i]]))
        return res % (10** 9 + 7)
