# Given an array nums and a value val, remove all instances of that value in-place and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Clarification:

# Confused why the returned value is an integer but your answer is an array?

# Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

# Internally you can think of this:

# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeElement(nums, val);

# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }
 

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,3,0,0], your answer will be accepted.
# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3]
# Explanation: Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4. 
# Note that the order of those five elements can be arbitrary. It doesn't matter what values are set beyond the returned length.
 

# Constraints:

# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100


#刷題用這個, time complexity O(n), space complexity O(1)
#思路: 使用雙指針來調換 elements => time complexity O(1)
#技巧: 每換一次, end指針要內縮, else start 指針前進
class Solution(object):
    def removeElement(self, nums, val):
        start, end = 0, len(nums) - 1 
        while start <= end:
        	if nums[start] == val:
        	   nums[start], nums[end], end = nums[end], nums[start], end - 1 #似 pop()
        	else: 
        		start +=1 #zero based index issue
        return start

#重寫第二次, time complexity O(n), space complexity O(1), 經典好題
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end-1
            else:
                start += 1
        return start





#刷題不能用這個, 自己想的, time complexity O(n^2), space complexity O(1), remove() => time complexity O(n)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        while val in nums:
            nums.remove(val)
        return len(nums)











        '''
        a = Solution()
        a.removeElement([0,1,2,2,3,0,4,2],2)
        [0, 1, 4, 0, 3, 2, 2, 2]
        start = 5
        
        '''









