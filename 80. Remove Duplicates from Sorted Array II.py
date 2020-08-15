'''
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

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

'''

# time complexity O(n)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=0
        idx=0
        for i in range(len(nums)):
            if count<2: #(0,1) 超過兩次跳過
                nums[idx] = nums[i]
                idx+=1
            if i < len(nums) - 1 and nums[i]!=nums[i+1]: #預先把count 歸0 注意為何加入i == len(nums)-1 是因為避免 list index out of range
                count=0
            elif i < len(nums) - 1 and nums[i]==nums[i+1]:  #重點在這 i+1
                count+=1
        return idx #zero based index issue, 因為每次完成nums[idx] = nums[i] 都會 idx+=1


#  自己想的 time complexity O(n), 刷題用這個
#  思路: 利用2 pointer and count 來紀錄指針所在元素是否超過重複上限, 若是則跳過直到不是重複元素為止, 並reset count
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        count = 1 #初始條件, 本身元素算一個count
        for i in range(1, len(nums)):  #end指針 總比start指針先往右一格
            if nums[i] == nums[start]:
                count += 1
                if count > 2:
                    continue
                nums[start+1] = nums[i]
                start += 1
                
            if nums[i] != nums[start]:
                nums[start+1] = nums[i]
                count = 1  #reset count
                start += 1     
        return start + 1  #zero based index issue




