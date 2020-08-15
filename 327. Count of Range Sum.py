'''
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.

'''

# The problem is similiar to 315. Count of Smaller Numbers After Self, yoc can click here to check how to slolve it.
# The difference between two probles is that you need compute the prefix sums, cumsum[i] means nums[:i]'s prefix sums :

# nums = [1,3,4]
# cumsum = [0,1,4,8]
# cumcum[1] means nums[:1]'s prefix sums

# We just need to count those where cumsum[j] - cumsum[i] is in [lower,upper].

# Approach 1 : Prefix-sum + Hashmap
# Naturally, utilize hashmap to reduce time  complexity

# prefix-sum + hashmap | time complexity: O(n+(upper-lower+1)*n)
class Solution(object):
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        cumsum = [0]  #初始值給個0
        for n in nums:
            cumsum.append(cumsum[-1]+n)
        
        import collections
        record = collections.defaultdict(int)  #defaultdict(int), int初始值為0
        
        res = 0
        for csum in cumsum:
            for target in range(lower,upper+1):  #prefix sum[2,2] = prefix sum[0.2] - prefix sum[0,1]
                if csum - target in record:  #可以這樣想 csum - record = target 在target區間內=> csum - target = record, record 紀錄目前csum之前的每個prefix sum
                    res += record[csum - target]
            record[csum] +=1
        return res






# Binary Indexed Tree
# The purpose of binary indexed tree is to enhance the speed updating an array. So the concept of tree's underlying array is important:

# Sum[k] is the sum of first k numbers. O(N^2) solution is

# 重要!!
# for j in range(n + 1):
#     for i in range(j):
#         if lower <= Sum[j] - Sum[i] <= upper: res += 1
# This is equal to:

# collection = empty
# for sum_j in Sum:
#     sum_i_count = how many sum_i in this collection that sum_j - upper <= sum_i <= sum_j - lower
#     res += sum_i_count
#     put sum_j into this collection

#終於看懂了, 看不懂請看https://leetcode.com/problems/count-of-range-sum/discuss/77986/O(NlogN)-Python-solution-binary-indexed-tree-268-ms
#此題關鍵 sum_i_count = how many sum_i in this collection that sum_j - upper <= sum_i <= sum_j - lower
#此題sums_sorted 若有重複元素會什麼不用set, 原因很簡單, 看似重複但卻代表不同index之間的sum
import bisect
class Solution:
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sums = [0] 
        for n in nums:
            sums.append(sums[-1] + n)
        
        sums_sorted = sorted(sums)  #重要, 要先排序以利之後的bit index
        count = 0
        
        self.len = len(sums) + 1
        self.BIT = [0] * self.len  #self.BIT[0] 代表root 不放元素的, 對應的原序列是sums_sorted array
        
        for pre_sum in sums:
            right = bisect.bisect_right(sums_sorted, pre_sum - lower)  #得到index
            left = bisect.bisect_left(sums_sorted, pre_sum - upper) 
            count += self.getCount(right) - self.getCount(left)  #(pre_sum - lower) - (pre_sum - upper) = (upeer - lower), 看不懂請看上面解釋
            self.update(bisect.bisect_right(sums_sorted, pre_sum))  #因為self.BIT[0] 代表root 不放元素的 所以bisect.bisect_right
        return count
    
    def getCount(self, i):
        count = 0
        while i > 0:
            count += self.BIT[i]
            i -= i & -i
        return count
    
    def update(self, i):
        while i < self.len:
            self.BIT[i] += 1
            i += i & -i

# lower = -2, upper = 2
# nums = [-2,5,-1]
# sums = [0,-2,3,2]
# sums_sorted = [-2,0,2,3]
# bit = [0,0,0,0,0]=> pre_sum = 0, bisect_right(sums_sorted, pre_sum) = 2 => [0,0,1,0,1]
# pre_sum = -2 right = bisect_right(sums_sorted ,-2-(-2)) = 2, left = bisect.bisect_lef(sums_sorted ,-2-(2))=0 count=1  => [0,1,2,0,2]
# pre_sum = 3 right = bisect_right(sums_sorted ,3-(-2)) = 4, left = bisect.bisect_lef(sums_sorted ,3-(2))=2 count=1  => [0,1,2,0,3]
# pre_sum = 2 right = bisect_right(sums_sorted ,2-(-2)) = 2, left = bisect.bisect_lef(sums_sorted ,2-(2))=0 count=3  => [0,1,2,1,4]

# bisect.bisect_left(a,x, lo=0, hi=len(a)) :
# 查找在有序列表 a 中插入 x 的index。lo 和 hi 用于指定列表的区间，默认是使用整个列表。如果 x 已经存在，在其左边插入。返回值为 index。

# bisect.bisect_right(a,x, lo=0, hi=len(a))
# 和 bisect_left 类似，但如果 x 已经存在，在其右边插入


# Bisect 模块提供的函数可以分两类： bisect* 只用于查找 index， 不进行实际的插入；而 insort* 则用于实际插入。该模块比较典型的应用是计算分数等级：

# def grade(score,breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#     i = bisect.bisect(breakpoints, score)
#     return grades[i]

# print [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
# 执行结果：

# ['F', 'A', 'C', 'C', 'B', 'A', 'A']


import bisect
a = [1,2,3,4,5,6,7]

bisect.bisect_right(a,0)
0

bisect.bisect_left(a,6)
5

bisect.bisect_right(a,6)
6















