'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''

# 刷題用這個, time complexity O(n), space complexity O(1)
# 思路: 利用2 pointer, end指針若與start指針元素一樣的話, end指針往下走(避掉重複), 直到不一樣時, start指針的下一個元素就是end指針目前元素
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0 #zero based position
        for i in range(len(nums)):  #模仿end 指針
            if nums[i] != nums[start]:
                start += 1
                nums[start] = nums[i] #變成i指針的數字, 當作visited 
        return start + 1  #length






#自己想的 time complexity O(n)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start, end = 0, 0
        lenth = 1  #初始條件
        while end < len(nums):
            while end < len(nums) and nums[end] == nums[start]:
                end += 1
            if end < len(nums):
                nums[start+1] = nums[end]
                start += 1
                lenth += 1
        return lenth   












