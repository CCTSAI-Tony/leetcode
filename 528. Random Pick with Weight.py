'''
Given an array w of positive integers, where w[i] describes the weight of index i, 
write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. 
Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
'''

Python binary search solution

Generate a prefix sum of the weights; then generate a random integer; after that, 
search for the indes using binary search, O(nlogn)

# 使用模版2 刷題用這個, time complexity O(nlogn)
# 思路: which randomly picks an index in proportion to its weight. 說明w[i] 較大者 較高機率被pick到 => prefix sum
# 建立完prefix sum, 使用ramdom.randinth從 prefix_Sum中挑一個值, 並用binary search 來判斷值落在哪個w[index], return 該index
import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.n = len(w)
        for i in range(1, self.n):
            w[i] += w[i-1]
        

    def pickIndex(self) -> int:
        seed = random.randint(1, self.w[-1])  #why randint(1, self.w[-1]), 因為w[i] 只能正整數, 最小為1, 因此隨機挑index要從1開始, 要排除0 重要!
        left, right = 0, self.n - 1
        while left + 1 < right:
            mid = left + (right - left)//2
            if self.w[mid] >= seed:
                right = mid
            else:
                left = mid
        if self.w[left] >= seed:
            return left
        else:
            return right



# 使用模版1 
# 思路: which randomly picks an index in proportion to its weight. 說明w[i] 較大者 較高機率被pick到 => prefix sum
import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.n = len(w)
        for i in range(1, self.n):  #prefix sum
            w[i] += w[i-1]
        self.s = self.w[-1]
        
        
    def pickIndex(self) -> int:
        seed = random.randint(1, self.s)  #why randint(1, self.s), 因為w[i] 只能正整數, 最小為1, 因此隨機挑index要從1開始, 要排除0 重要!
        l, r = 0, self.n-1
        while l <= r:
            mid = l + (r-l)//2
            
            if seed == self.w[mid]:
                return mid
            elif seed > self.w[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l   #這題是回覆比target大的最小值, 所以回覆l, 似 Search Insert Position




import random
class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.n = len(w)
        for i in range(1,self.n):
            w[i] += w[i-1]  #sum u
        self.s = self.w[-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        seed = random.randint(1,self.s)  #why randint(1,self.s), 因為array 都是正數, 最小正整數 = 1, 這邊要注意的是random最大值為self.w[-1], 所以l 不會== self.n
        l, r = 0, self.n  #左閉右開
        while l < r:
            mid = l + (r-l)//2
            if seed == self.w[mid]:
                return mid
            elif seed > self.w[mid]:
                l = mid + 1
            else:
                r = mid  
        return l 


import random
random.randint(1, 5)  #包含5
5


import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.n = len(w)
        for i in range(1, self.n):
            w[i] += w[i-1]
        self.s = self.w[-1]
        
        
    def pickIndex(self) -> int:
        seed = random.randint(1, self.s)
        l, r = 0, self.n  #一樣是左閉右開
        while l < r:
            mid = l + (r-l)//2
            if seed > self.w[mid]:  #可以試著想一下為什麼不能>=, 很好懂, 若seed < w[0], l-1 = -1 不合理, 這邊l 是代表插入的位置比較好理解
                l = mid + 1  
            else:
                r = mid  
        return l 







