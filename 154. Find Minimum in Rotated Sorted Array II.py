'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
'''

class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums)-1
        while left < right:
            while left < right and nums[left] == nums[left + 1]: #while left < right 再打一次 double confirm
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            if left == right:
                return nums[left]
            
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
            
                
        return nums[left] #return nums[right]也行 意思是最終left = right


'''
double while loop 記得condition 要手動繼承 不然會被打破
a = 2
b = 10
c = 20
while a < b:
    while a <c:
        a +=1
        print(a)

3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20






'''