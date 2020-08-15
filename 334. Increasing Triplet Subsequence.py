'''
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false
'''

# This approach is similar to longest increasing subsequence where you maintain a new list 
# and iterate through the given list and either append the new element to result list or replace it's upper bound with current value
#Algo is called patience sorting, 這個思路很棒!

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        nums1, nums2 = float("inf"), float("inf")
        for n in nums:
            if n <= nums1:  #記得要<=, corner case nums = [1,1,1,1,1,1,1,1,1,]
                nums1 = n
            elif n <= nums2:
                nums2 = n
            else:
                return True  # n > num1 and n > num2 i.e. increasing triplet
        return False