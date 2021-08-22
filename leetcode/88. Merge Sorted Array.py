'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]


nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

nums1 = [1,2,3,0,0,6]
nums1 = [1,2,3,0,5,6]
nums1 = [1,2,3,3,5,6]
nums1 = [1,2,2,3,5,6]
nums1 = [1,2,2,3,5,6]

'''

# 思路: 兩個序列依序從右邊開始比, 比完放在m+n-1的位置, 關注在nums1[m-1] 與 nums2[n-1] 的比較, 比較完後改變的位置不影響剩下要比較的元素
# 不要被nums1 後面的0搞混, 專注在m,n就可以
class Solution:
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:  #從最大開始比 右邊位置先決定 這邊注意  >= or > 都可以, 不影響結果
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0: # 此時 m = 0, nums2 剩餘較小值原封不動搬到nums1, 若n = 0, 則剩餘nums1保持原樣就可以了
            nums1[:n] = nums2[:n]


#重寫一遍
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m and n:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            elif nums1[m-1] <= nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n-=1
        if not m:
            nums1[:n] = nums2[:n]


# 重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]















