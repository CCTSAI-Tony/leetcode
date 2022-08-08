'''
Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k, return the kth (1-based) smallest product of nums1[i] * nums2[j] where 0 <= i < nums1.length and 0 <= j < nums2.length.
 

Example 1:

Input: nums1 = [2,5], nums2 = [3,4], k = 2
Output: 8
Explanation: The 2 smallest products are:
- nums1[0] * nums2[0] = 2 * 3 = 6
- nums1[0] * nums2[1] = 2 * 4 = 8
The 2nd smallest product is 8.
Example 2:

Input: nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6
Output: 0
Explanation: The 6 smallest products are:
- nums1[0] * nums2[1] = (-4) * 4 = -16
- nums1[0] * nums2[0] = (-4) * 2 = -8
- nums1[1] * nums2[1] = (-2) * 4 = -8
- nums1[1] * nums2[0] = (-2) * 2 = -4
- nums1[2] * nums2[0] = 0 * 2 = 0
- nums1[2] * nums2[1] = 0 * 4 = 0
The 6th smallest product is 0.
Example 3:

Input: nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3
Output: -6
Explanation: The 3 smallest products are:
- nums1[0] * nums2[4] = (-2) * 5 = -10
- nums1[0] * nums2[3] = (-2) * 4 = -8
- nums1[4] * nums2[0] = 2 * (-3) = -6
The 3rd smallest product is -6.
 

Constraints:

1 <= nums1.length, nums2.length <= 5 * 104
-105 <= nums1[i], nums2[j] <= 105
1 <= k <= nums1.length * nums2.length
nums1 and nums2 are sorted.
'''

'''
The idea of this problem is to use binary search: let check(x) be the answer to the question: how many products are less or equal than x. 
Then we use binary search and find the first moment where we have exactly k such numbers.

If n1 is positive, then values in nums2 * n1 go in increasing order, so we use bisect to find number of values which are <= x//n1.
If n1 is negative, then values in nums2 * n1 going in decreasing order, so we need to take the right part. => ceil(x/n1)
If n1 equal to 0, than all values in nums2 * n1 are equal to 0. 
So, we update total only if x >= 0.
Complexity
Time complexity is O(n*log m* log N), where n = len(nums1), m = len(nums2) and N = 10**10 + 10 is the maximum value of product. Space complexity is O(1)
'''

# 刷題用這個, time complexity O(nlogmlogN), n = len(nums1), m = len(nums2) and N = 10**10 + 10, space complexity O(1)
# 思路: binary search, 但要考慮三種情況, n1 > 0, n1 < 0, and n1 == 0
# 注意: n1 > 0 and n1 < 0 要對應 x // n1 and ceil(x / n1)
from bisect import bisect, bisect_left
class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        def check(x):
            total = 0
            for n1 in nums1:
                if n1 > 0: 
                    total += bisect(nums2, x//n1)  #similar to bisect_right, but actually they are different, just behave the same
                if n1 < 0: 
                    total += len(nums2) - bisect_left(nums2, ceil(x/n1))
                if n1 == 0 and x >= 0: # 若 x >= 0, 那整個nums2 都是比自己小的
                    total += len(nums2)

            return total

        beg, end = -10**10 - 1, 10**10 + 1

        while beg + 1 < end: # 模板2
            mid = (beg + end)//2
            if check(mid) >= k:
                end = mid
            else:
                beg = mid

        if check(beg) >= k:
            return beg
        else:
            return end























