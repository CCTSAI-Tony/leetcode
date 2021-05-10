'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. 
Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
'''

#自己重寫, time complexity O(n), space complexity O(1)
#思路: bit manipulation xor
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res



# follow up 刷題用這個
# 模板2 自己重寫 time complexity O(logn) space complexity O(1) ex: [1,1,2,2,3,3,4,4,5,5]
# 思路: 若沒有單獨的元素, 偶數index => nums[i] = nums[i+1], 奇數index => nums[i] == nums[i-1] 插入單獨元素才導致以上關係不成立
# 觀察數列, input不會出現ex:[1,1,2,3,2,4,4] 這樣的情形, 都是兩兩一起, 除了單獨元素, 因此單獨元素後面的數列以上關係會不成立, 前面的數列則成立,
# 利用這樣的關係就可以確認單獨元素會在哪一邊
# 因此利用check 先看mid是否偶數還是奇數, 再check 關係是否成立, 若成立代表單獨元素在mid右邊, 不成立則代表單獨元素在mid左邊
# 
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.check(mid, nums): #單獨元素在右邊
                left = mid
            else:
                right = mid
        if left == 0:  #除了left == 0, 其他一律return right, 因為check mid == True, left = mid, left都是符合關係的, 而right都是不符合關係的
            return nums[left]
        return nums[right]
            
            
    def check(self, i, nums):
        if i % 2 == 0: #確認奇偶
            if nums[i] == nums[i+1]:
                return True
            return False
        else:
            if nums[i] == nums[i-1]:
                return True
            return False

#重寫第二次, time complexity O(logn), space complexity O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            m = l + (r - l) // 2
            if self.check(m, nums):
                l = m
            else:
                r = m
        if not self.check(l, nums):
            return nums[l]
        else:
            return nums[r]
        
    def check(self, m, nums):
        if m % 2:
            if nums[m] == nums[m-1]:
                return True
            else:
                return False
        else:
            if nums[m] == nums[m + 1]:
                return True
            else:
                return False

# If every element in the sorted array were to appear exactly twice, they would occur in pairs at indices i, i+1 for all even i.

# Equivalently, nums[i] = nums[i+1] and nums[i+1] != nums[i+2] for all even i.

# When we insert the unique element into this list, the indices of all the pairs following it will be shifted by one, negating the above relationship.

# So, for any even index i, we can compare nums[i] to nums[i+1].

# If they are equal, the unique element must occur somewhere after index i+1
# If they aren't equal, the unique element must occur somewhere before index i+1
# Using this knowledge, we can use binary search to find the unique element.

# We just have to make sure that our pivot index is always even, so we can use mid = 2 * ((lo + hi) // 4) instead of the usual mid = (lo + hi) // 2.

# Solution:

# Time: O(logn)
# Space: O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = 2 * ((lo + hi) // 4)
            if nums[mid] == nums[mid+1]:
                lo = mid+2
            else:
                hi = mid
        return nums[lo]



