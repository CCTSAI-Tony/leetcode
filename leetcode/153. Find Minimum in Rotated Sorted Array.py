'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''
#因為有判斷nums[right], 因此 right 要設在區間內, len(nums) - 1
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:  #左閉右開
            mid = (left + right) // 2
            if nums[mid] > nums[right]: 
                left = mid + 1
            else:
                right = mid
        return nums[right] #return nums[left]也行 意思是最終left = right

'''
Hide Hint 1
Array was originally in ascending order. Now that the array is rotated, 
there would be a point in the array where there is a small deflection from the increasing sequence. 
eg. The array would be something like [4, 5, 6, 7, 0, 1, 2].

Hide Hint 2
You can divide the search space into two and see which direction to go. Can you think of an algorithm which has O(logN) search complexity?

Hide Hint 3
All the elements to the left of inflection point > first element of the array.
All the elements to the right of inflection point < first element of the array.

'''

# 第三类题：没有明确Target的题型，可越界类型
# 这种类型的题目，用 l <= r 的模板可能会越界(or 越過target)，我们可以填写个别的Edge Case处理，或者套用其他比如 l < r 或者 l + 1 < r的模板解决。


# 經典
# You may assume no duplicate exists in the array.
# 模板2 刷題用這個
# 思路: 利用nums[mid] > nums[right] 知道是否右邊出現轉折, 會有最小值
# 為什麼不用模板1 因為當left越界時, 最終返回的nums[left] 有可能會超過index range, 很重要的觀念
# 基本觀念, 何時使用模板2, 當運行過程or return 要 access 數組區間邊界的數 ex: nums[left], nums[right] 時, 避免越界而使用

# time complexity O(logN)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left + 1 < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:  #一樣在模板2, >, or >= 一樣可以work, 因為 left, right 只移動邊界到mid的位置， 不會誤刪除target。
                left = mid  #右區間比較小, 往右區間搜尋
            else:
                right = mid #左區間比較小, 往左區間搜尋
        
        return min(nums[left], nums[right])
       

#重寫第二次, time complexity O(logn), space complexity O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
        if nums[l] < nums[r]:
            return nums[l]
        return nums[r]





#自己想的, time complexity O(logn), space complexity O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[l]:
                if nums[mid] > nums[r]:
                    l = mid
                else:
                    r = mid
            elif nums[mid] < nums[l]:
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid
        if nums[l] < nums[r]:
            return nums[l]
        return nums[r]

Input: [4,5,6,7,0,1,2]


#不同的想法, 也可以, 但還是用上面的想法比較好
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[left] or nums[left] < nums[right]:
                right = mid
            else:
                left = mid
        if nums[left] < nums[right]:
            return nums[left]
        return nums[right]



#若題目換成找最大值, 要變成如何呢?
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left + 1 < right:
            mid = (left + right)//2
            if nums[mid] < nums[right] or nums[right] > nums[left]:  
                left = mid  
            else:
                right = mid 
        
        return max(nums[left], nums[right])

#或是
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid
        if nums[left] > nums[right]:
            return nums[left]
        return nums[right]

