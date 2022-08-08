'''
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n 
from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5 @@題目會給你限定長度
Output:
[9, 8, 6, 5, 3]
Example 2:

Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]
Example 3:

Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]
'''

# To create the max number from num1 and nums2 with k elements, we assume the final result combined by i numbers 
# (denotes as left) from num1 and j numbers (denotes as right) from nums2, where i+j==k.

# Obviously, left and right must be the maximum possible number in num1 and num2 respectively. i.e. num1 = [6,5,7,1] and i == 2, then left must be [7,1].

# The final result is the maximum possible merge of all left and right.

# So there're 3 steps:

# iterate i from 0 to k.
# find max number from num1, num2 by select i , k-i numbers, denotes as left, right
# find max merge of left, right
# function maxSingleNumber select i elements from num1 that is maximum. The idea find the max number one by one. 
# i.e. assume nums [6,5,7,1,4,2], selects = 3.
# 1st digit: find max digit in [6,5,7,1], the last two digits [4, 2] can not be selected at this moment.
# 2nd digits: find max digit in [1,4], since we have already selects 7, we should consider elements after it, also, 
# we should leave one element out.
# 3rd digits: only one left [2], we select it. and function output [7,4,2]

# function mergeMax find the maximum combination of left, and right.



# 刷題用這個, time complexity O(n^2), space complexity O(n)
# 思路: Greedy Search + Dynamic Programming
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:        
        def merge(n1, n2):
            res = []
            while (n1 or n2) :
                if n1>n2:
                    res.append(n1[0])
                    n1 = n1[1:]
                else:
                    res.append(n2[0])
                    n2 = n2[1:]
            return res
        
        def findmax(nums, length):
            l = []
            maxpop = len(nums)-length
            for i in range(len(nums)):
                while maxpop>0 and len(l) and nums[i]>l[-1]:
                    l.pop()
                    maxpop -= 1
                l.append(nums[i])
            return l[:length]
        
        n1 = len(nums1)
        n2 = len(nums2)
        res = [0]*k
        for i in range(k+1):
            j = k-i
            if i>n1 or j>n2:    continue
            l1 = findmax(nums1, i)
            l2 = findmax(nums2, j)
            res = max(res, merge(l1,l2))
        return res









class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        n, m= len(nums1),len(nums2)
        ret = [0] * k
        for i in range(0, k+1):
            j = k - i
            if i > n or j > m: 
                continue #跳下一個
            left = self.maxSingleNumber(nums1, i)
            right = self.maxSingleNumber(nums2, j)
            num = self.mergeMax(left, right)
            ret = max(num, ret)
        return ret


    def mergeMax(self, nums1, nums2):
        ans = []
        while nums1 or nums2:
            if nums1 > nums2: #比較第一個元素
                ans += nums1[0],  #技巧!! nums1[0], 加一個逗號差很多 這樣就可以直接被list加
                nums1 = nums1[1:]
            else:
                ans += nums2[0],
                nums2 = nums2[1:]
        return ans

    def maxSingleNumber(self, nums, selects):
        n = len(nums)
        ret = [-1]
        while selects > 0:
            start = ret[-1] + 1 #search start
            end = n-selects + 1 #search end, n-selects + 1 確保第一輪select後面的字元加上select == selects總共的字元, 可以從總共只選1個字元想 end = n
            ret.append( max(range(start, end), key = nums.__getitem__))
            selects -= 1
        ret = [nums[item] for item in ret[1:]]
        return ret


# a = [3,4,5,6,100,8,9,10]
# ret = []
# ret.append( max(range(0, 8),key = a.__getitem__)) a.__getitem__  @@range(0,8) 裡面每個都是一個key, key = a.__getitem__ , 代表key的value與a序列聯通, 好招學起來
# ret
# [4]

# a = [3,4,5,6,100,8,9,10]
# ret = []
# ret.append( max(range(1, 9)))
# ret
# [8] 跟a序列沒關係了

# a= [2,3,4]
# b=[3,4]
# a>b
# False

# b>a
# True

# a= [2,3,4]
# b=[]
# a>b
# True

# a= [2,3,4]
# ans = []
# a[0],
# (2,)
# ans += a[0],
# [2]











