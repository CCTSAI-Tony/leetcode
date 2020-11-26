'''
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
'''

# Downside is it is O(n*logn) and O(N) space but it is the simplest solution.

# Just put sorted numbers in array
# Put largest numbers in odd indexes first
# Then put remaining numbers in even indexes
# So even < odd > even

class Solution:
    def wiggleSort(self, nums):
        arr = sorted(nums)
        for i in range(1, len(nums), 2): nums[i] = arr.pop() 
        for i in range(0, len(nums), 2): nums[i] = arr.pop() 


# 實際上此題不需考慮以下問題 意思就是情況1-4都對
    # nums[0] < nums[1] > nums[2] < nums[3]
    # equals to

    # 1,nums[1] >= nums[3] >= nums[0] >= nums[2] ok 奇數愈左愈大 偶數愈右愈小
    # 2,nums[3] >= nums[1] >= nums[0] >= nums[2] wrong
    # 3,nums[1] >= nums[3] >= nums[2] >= nums[0] wrong
    # 4,nums[3] >= nums[1] >= nums[2] >= nums[0] wrong

    # e.g. nums = [1,2,2,3]
    # cut into half => [1,2] [2,3]

    # 1,both reverse => [2,3,1,2] #這邊講的reverse是指奇數之間 偶數之間的順序 nums[0] < nums[1] > nums[2] < nums[3]
    # 2,fir no reverse => [2,2,1,3]
    # 3,sec no reverse => [1,3,2,2]
    # 4,no reverse => [1,2,2,3]
    #    because of repeated nums, so they are wrong, 因為出現連續重複digit 所以是錯的


# build the mapping relationship from index to virtual index
# 1,3,5,7,...,n,0,2,4,6,...n-1
# e.g. 1,3,5,7,0,2,4,6 -> 0,1,2,3,4,5,6,7 這裡n=8 n|1 =9
# n|1 sets the last bit of n to 1

# so k - (n|1), it will become the smallest even num (not smaller than n) 指的是不會小超過n, 這句話很難懂直接看code

# def virtualIndex(i):
#     k = 2*i+1
#     if k <= n:
#         return k
#     else:
#         return k - (n|1)
# do three-way partition in On,O1
# 1,3,5,7,..,n,0,2,4,6,......n-1. 奇數愈左愈大 偶數愈右愈小
# | >medium | =medium | <medium |
# ..........i........jk.........

# https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/ono1-after-median-virtual-indexing 參考資料
import numpy
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        
        def A(i):
            return (2*i+1) % (n|1)  #virtual index 本題精華, 實現小的偶數index 大的其數index

            
        # find the medium
        # quick select On
        key = numpy.median(nums) #直接回報排序後的中位數
        # i is the start of 1st part
        # j is the end of 2nd part
        # k is the end of 3rd part
        i,j,k=0,0,n-1
        
        
        while j <= k: #j為指針, 遍歷原序列1,3,5,7,0,2,4,6 此順序, 比key大放左 比key小放右
            if nums[A(j)] > key:
                nums[A(j)],nums[A(i)]=nums[A(i)],nums[A(j)]
                i,j = i+1,j+1
            elif nums[A(j)] < key:
                nums[A(j)],nums[A(k)]=nums[A(k)],nums[A(j)]
                k -= 1
            else:  #nums[A(j)] = key
                j += 1
            

# import numpy
# nums = [1,5,1,1,6,4]
# key = numpy.median(nums)
# print(key)
# 2.5
# nums.sort()
# print(nums)
# [1, 1, 1, 4, 5, 6]



# | >medium | =medium | <medium |
# ..........i........jk.........

# 完整版 TLE
import numpy
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        
        def A(i):
            return (2*i+1) % (n|1)

            
        # find the medium
        # quick select On
        midIndex = int(n/2)
        # key = numpy.median(nums)
        # i is the start of 2st part
        # j is the end of 2nd part
        # k is the end of 2rd part
        i,j,k=0,0,n-1
        
        while True:
            pivot = random.randint(i,k)
            nums[A(pivot)],nums[A(k)] = nums[A(k)],nums[A(pivot)]
            key = nums[A(pivot)]
            while j <= k:
                if nums[A(j)] > key:
                    nums[A(j)],nums[A(i)]=nums[A(i)],nums[A(j)]
                    i,j = i+1,j+1
                elif nums[A(j)] < key:
                    nums[A(j)],nums[A(k)]=nums[A(k)],nums[A(j)]
                    k -= 1
                else:
                    j += 1
            if midIndex < i:
                i,j,k = 0,0,i-1 #此時i-n-1 已排序完成
            elif midIndex > k:
                i,j,k = k+1,k+1,n-1  #此時0-k 已排序完成
            else:
                return
            





















