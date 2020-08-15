'''
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.
'''

why use binary search
'''We can do simple binary search that check [mid] point and [mid+1] point and take half which has higher value, i.e. take left half if nums[mid]>nums[mid+1].
It is not easy to show or proof why this works.
The simple proof is that we take part of numbers that boundary condition holds true.
That is, we only take search range (l, r) if nums[l-1]<nums[l] and num[r]>num[r+1]. 
Note that initial search range (l,r) where l=0 and r=len(nums)-1 holds true. 
Then, each step we reduce the search range half making sure the boundary condition holds true. Note that the other half the condition does not hold true.
Therefore, when it finally is reduced to a single number, 
it is the local maximum since the boundary condition for a single number is same as the condition for local maximum.





It's not hard to show the correctness, just visualize the trend. If the next number is larger than current, 
it show an increasing curve, then the peak must in the right half, else in the left half. Since we know there's a local peak for sure.

Thanks for the explanation. Binary search only works when the nums[-1] = nums[n] = -∞ holds true when it is looking for a peak.
'''


# Basic Idea: Binary search

# Elaboration: 
#  if an element(not the right-most one) is smaller than its right neighbor, then there must be a peak element on its right, 
#  because the elements on its right is either 
#    1. always increasing  -> the right-most element is the peak
#    2. always decreasing  -> the left-most element is the peak
#    3. first increasing then decreasing -> the pivot point is the peak
#    4. first decreasing then increasing -> the left-most element is the peak  

#    Therefore, we can find the peak only on its right elements( cut the array to half)

#    The same idea applies to that an element(not the left-most one) is smaller than its left neighbor.



# Conditions:
#      1. array length is 1  -> return the only index 
#      2. array length is 2  -> return the bigger number index                     
#      3. array length is bigger than 2 -> 
#            (1) find mid, compare it with its left and right neighbors  
#            (2) return mid if nums[mid] greater than both neighbors
#            (3) take the right half array if nums[mid] smaller than right neighbor
#            (4) otherwise, take the left half

# Run time: O(logn)
# Memory: constant
# Test cases: 
#      [1]
#      [1,2]
#      [2,1]
#      [1,2,3]
#      [3,2,1]
#      [2,1,3]



# Given an input array nums, where nums[i] ≠ nums[i+1], 題目給的條件, 所以不會出現[2,2,3,4,5,5] 的序列
#模板2, 思路: 與mid 的右邊比較, 若右邊比較大, 則往右邊一半搜索, 若左邊比較大則往左邊一半搜索
#脫離while loop時, left, right 是相鄰在一起的時候
#為什麼不用模板1: mid比对的区间是 nums[mid + 1]，这种情况当left 越界 left = mid + 1, 此時left = right都在最右邊, nums[mid + 1]就会报错, 
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left + 1 < right:
            mid = (left + right)//2
            if nums[mid] <= nums[mid + 1]:  #模板2 裡面是否 <, or <= 都可以work, left, right 因為只移動邊界到mid的位置， 不會誤刪除target。
                left = mid
            else:
                right = mid
        if nums[left] > nums[right]:
            return left
        else:
            return right





#左閉右開
class Solution:
    def findPeakElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid

            elif nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1

        return left #最終 left = right



















