'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

#time complexity O(nlogn), n: max(len(nums1), len(nums2))
#思路: 先對兩組數列sort, 各設一指針同步遍歷兩個序列, 兩者指針互相比較, 若指到相同元素則丟到res, 兩指針同步往後
#若兩個序列皆以sort, time complexity O(n+m)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()  #重點在這裡
        nums2.sort()
        res = []
        m, n = 0, 0
        while m < len(nums1) and n < len(nums2):
            if nums1[m] == nums2[n]:
                res.append(nums1[m])
                m += 1
                n += 1
            elif nums1[m] > nums2[n]:
                n += 1
            else:
                m += 1
        return res

# 刷題用這個 模板2, follow up
# 若nums1, nums2 都已經sort, 此algorithm => O(nlogm) n:len(nums1), m: len(nums2), 若nums2遠大於nums1, 則此algorithm 比上面線性好
# 思路: 這是follow up, 若數列都已經sort, 則使用binary search 搜尋短序列的元素是否在長序列裡, 找得到對應的index的話, 加入對應index元素於res
# 記得搜索到後, 長序列的left指針移到 index + 1, 因為原index已被登錄進 res裡
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        res = []
        left, right = 0, len(nums2)-1
        
        for num in nums1:
            index = self.binary(nums2, left, right, num)
            if index == -1:
                continue
            res.append(nums2[index])
            left = index + 1
            if left >= len(nums2): #代表nums2 遍歷完了
                break
        return res
        
        
    def binary(self, nums, left, right, target):
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        return -1

#自己想的, 沒有拆分func 的版本
#若nums1, nums2 都已經sort, 此algorithm => O(nlogm) n:len(nums1), m: len(nums2)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        res = []
        temp = 0
        for num in nums1:
            left, right = temp, len(nums2)-1
            if left > len(nums2) -1:
                break
            while left + 1 < right:
                mid = left + (right-left)//2
                if nums2[mid] >= num:
                    right = mid
                else:
                    left = mid
            if nums2[left] == num:
                temp = left
            elif nums2[right] == num:
                temp = right
            else:
                continue
            res.append(nums2[temp])
            temp += 1
        return res




# [Facebook] Python Binary Search Approach w/ Explanation O(nlogm)

# Context:
# A very frequent Facebook follow up: what if only one of the inputs are super large? e.g. len(nums1) = 3, len(nums2) = 1000. 
# Can we do better than 2-pointers which run in O(n+m) time? Answer is yes: we achieve O(nlogm) in this case, n < m.

# Assumption:
# nums1 and nums2 are already sorted.

# Explanation:
# This approach is efficient when only one of the input is really large. Therefore, 
# we first figure out which is the shorter array and loop through it, for every element, we binary search it on the other array. 
# One thing to note is that the question asks to include duplicates, therefore when we binary search, 
# we need to find the left-most matching number. Since the inputs are sorted, next time we perform a binary search, the low should start the previously found index+1.

# Code:  This is so cool!


#思路: 這是follow up, 若數列都已經sort, 則使用binary search 搜尋短序列的元素是否在長序列裡, 找得到對應的index的話, 長序列的left指針 = index + 1
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        if len(nums1) > len(nums2): 
            nums1, nums2 = nums2, nums1 
        res = [] 
        low, high = 0, len(nums2)  #high = len(nums2) 即右指针永远指向搜索区间外, 若left = len(nums2) 代表沒搜到
        for x in nums1:
            index = self.binarySearch(nums2, low, high, x)
            if index != -1: 
                low = index+1 
                res.append(nums2[index]) 
        return res

    def binarySearch(self, nums, low, high, target): 
            while low < high: 
                mid = (low+high)//2 
                if nums[mid] == target:  #為何不直接return mid, 這是為了最終return left 來記錄下一個二元搜索位置
                    high = mid  
                elif nums[mid] > target: 
                    high = mid 
                else: 
                    low = mid+1 
                
            if 0 <= low < len(nums) and nums[low] == target:  #若left = len(nums2) 代表沒搜到
                return low 
            else: 
                return -1


# 例如区间[2,6),他是一个左闭右开的区间，那么在这2~6之间的数字我都可以取到，而且可以取到2，但不可以取到6.

#左閉又開 右开区间，即右指针永远指向搜索区间外 

