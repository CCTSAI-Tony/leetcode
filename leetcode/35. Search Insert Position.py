class Solution(object):
	def searchInsert(self, nums, target):
		left,right = 0, len(nums)-1
		while left<= right:
			mid= (left+right)//2
			if nums[mid] >= target:
				right = mid-1
			else:
				left = mid+1
		return left

'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

a.searchInsert([5,7,7,8,8,10],6)
l=0 r=5
mid=2
l=0 r=1
mid=1
l=0 r=0
mid=0
l=1 r=0
return l =1

'''