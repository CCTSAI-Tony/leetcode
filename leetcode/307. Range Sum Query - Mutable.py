'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
'''

# Use self.c to represent Binary Indexed Tree. Section sums are stored in self.c[1..len(nums)]. x & -x is lowbit function, which will 
# return x's rightmost bit 1, e.g. lowbit(7) = 1, lowbit(20) = 4.

# self.c[1] = nums[0]

# self.c[2] = nums[0] + nums[1]

# self.c[3] = nums[2]

# self.c[4] = nums[0] + nums[1] + nums[2] + nums[3]

# self.c[5] = nums[4]

# self.c[6] = nums[4] + nums[5]

# self.c[7] = nums[6]

# self.c[8] = nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6] + nums[7]

# https://www.acwing.com/blog/content/80/  這個網址解釋很清楚

# query: time complexity O(logn), update: time complexuty O(logn), init: time complexity O(nlogn)
# 思路: binary index tree, 建立index 數組, bst數組 比原數組多了一格, 第一格只是佔位子用
# init 先update初始數組值, 之後update nums[i] 計算更改後與更改前的差值, 並update binary tree
class NumArray(object):
    def __init__(self, nums):
        self.n = len(nums)
        self.a = nums
        self.c = [0] * (self.n + 1) #建立 bst 數組
        for i in range(self.n): #update 初始值
            k = i + 1 #bst index
            while k <= self.n:
                self.c[k] += nums[i] #初始化 Binary Indexed Tree
                k += (k & -k)

    def update(self, i, val):
        diff = val - self.a[i]
        self.a[i] = val
        i += 1 #index issue, ex: self.c[1] = nums[0]
        while i <= self.n:
            self.c[i] += diff
            i += (i & -i)

    def sumRange(self, i, j):
        res = 0
        j = j + 1 #j+1, index issue, why i 不用+1, 因為要扣掉的是self.c[i]的前綴和, self.c[i+1] 包含在sumRange區間裡
        while j:
            res += self.c[j]
            j -= (j & -j)
        while i:
            res -= self.c[i]
            i -= (i & -i)
        return res

#“区间 [3, 7] 的和” = “前缀和(7)” - “前缀和(2)” 。

#自己重寫
class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.a = nums
        self.c = [0] * (self.n + 1)
        for i in range(self.n):
            k = i+1
            while k < self.n + 1:
                self.c[k] += self.a[i]
                k += (k & -k)
            

    def update(self, i: int, val: int) -> None:
        diff = val - self.a[i]
        self.a[i] = val
        k = i + 1
        while k < self.n + 1:
            self.c[k] += diff
            k += (k & -k)
            
        

    def sumRange(self, i: int, j: int) -> int:
        j = j + 1
        res = 0
        while j > 0:
            res += self.c[j]
            j -= (j & -j)
        while i > 0:
            res -= self.c[i]
            i -= (i & -i)
        return res



#重寫第二次, time complexity update, sumRange: O(logn), init: O(nlogn), space complexity O(n)
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bits = [0] * (len(nums) + 1)
        self.m = len(nums)
        for i in range(len(nums)):
            k = i + 1
            while k <= self.m:
                self.bits[k] += nums[i]
                k += (k & -k)
        
        

    def update(self, i: int, val: int) -> None:
        diff = val - self.nums[i]
        self.nums[i] = val
        i = i + 1
        while i <= self.m:
            self.bits[i] += diff
            i += (i & -i)
            
        

    def sumRange(self, i: int, j: int) -> int:
        res = 0
        j = j + 1
        while j > 0:
            res += self.bits[j]
            j -= (j & -j)
        while i > 0:
            res -= self.bits[i]
            i -= (i & -i)
        return res





#naive approach, 差分法, time complexity update O(n), sumRange O(1) => total O(n^2)
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [0] + nums
        self.s = [0] * (len(nums) + 1)
        for k in range(1, len(self.nums)):
            self.s[k] = self.s[k-1] + self.nums[k]
        

    def update(self, i: int, val: int) -> None:
        i = i + 1
        self.nums[i] = val
        for k in range(1, len(self.nums)):
            self.s[k] = self.s[k-1] + self.nums[k]

    def sumRange(self, i: int, j: int) -> int:
        j = j + 1
        return self.s[j] - self.s[i]