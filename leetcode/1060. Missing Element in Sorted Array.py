'''
1060. Missing Element in Sorted Array
Medium

623

30

Add to List

Share
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

 

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
 

Note:

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8
'''

#刷題用這個, 模板2 time complexity O(logn), 重要! list[i] time complexity => O(1), but list.index(x) => time complexity O(n)
#思路: 先計算整個array missing 的 counts, 若k > counts, 則return nums[-1] + k - counts
#若k <= counts, 則使用binary search 來找出 k missing item, 如何計算該區間的missing count => nums[mid] - nums[left] - (mid - left)
#從實際長度推導: nums[mid] - nums[left] +1 - (mid - left + 1) => nums[mid] - nums[left] - (mid - left)
#若missing < k, left = mid => k -= missing (先把左半邊填滿), 若missing >= k, right = mid
#最後return nums[left] + k, 因為nums[left], nums[right] 中間沒元素了
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if not nums or k == 0:
            return 0
        
        diff = nums[-1] - nums[0] + 1 # complete length
        missing = diff - len(nums) # complete length - real length
        if k > missing: # if k is larger than the number of mssing words in sequence
            return nums[-1] + k - missing
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            missing = nums[mid] - nums[left] - (mid - left)
            if missing < k:
                left = mid
                k -= missing # KEY: move left forward, we need to minus the missing words of this range
            else:
                right = mid
                
        return nums[left] + k # k should be between left and right index in the end


#自己重寫, time complexity O(logn)
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        complete = nums[-1] - nums[0] + 1
        missing = complete - len(nums)
        if k > missing:
            return nums[-1] + (k-missing)
        l, r = 0, len(nums)-1
        while l + 1 < r:
            mid = l + (r-l)//2
            missing = (nums[mid] - nums[l]) - (mid - l)
            if k > missing:
                l = mid
                k = k - missing
            else:
                r = mid
        return nums[l] + k



