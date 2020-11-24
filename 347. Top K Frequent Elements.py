'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Time Complexity of building a heap is O(n) 重要!!
證明: https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/

heapq is a binary heap, with O(log n) push and O(log n) pop

利用Counter + PriorityQueue来做。时间复杂度是O(n)+O(Klogn)
'''


import heapq
from collections import Counter 
class Solution:
    def topKFrequent(self, nums, k):
        res = []
        dic = Counter(nums)
        max_heap = [(-val, key) for key, val in dic.items()]
        heapq.heapify(max_heap)  #O(n)
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])  #pop出來的是tuple
        return res   

#自己重寫, 刷題用這個, time complexity O(klogn)
#思路: 利用counter 與 heap 來pop出 k frequent elements, 
#技巧: 使用heapify 來整理max_heap => O(n)
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = Counter(nums)
        max_heap = [(-v, i) for i, v in freq.items()] #max-heap
        heapq.heapify(max_heap)
        for  _ in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res




#刷題不能用這個
#自己重寫, time complexity(nlogn)
#思路: 利用counter 與 heap 來pop出 k frequent elements
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_nums = Counter(nums) #O(n)
        heap = []
        res = []
        for num in frequent_nums.keys():
            heapq.heappush(heap, (-frequent_nums[num], num))
        
        for _ in range(k):
            temp = heapq.heappop(heap)
            res.append(temp[1])
        return res





# Make Heap
# max_heap = [(-val, key) for key, val in dic.items()]
# 为什么是-val？
# Python里面的heapify是定义的Min-heap，在StackOverFlow里面寻找Max-heap的方法，这个答案比较符合我偷懒的风格: Link, 把Value直接设成 -Value即可。
# https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python/2501527#2501527

# Find K
# 把Heap里面出现最大的几个数pop出来就好，记得这里需要pop出来的是key, 不是val

# for i in range(k):
#     res.append(heapq.heappop(max_heap)[1])
# return res   

# >>> from collections import Counter
# >>> 
# >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# >>> print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>
# >>> print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# >>> 
# >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>> 
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]


#補充知識
Heap elements can be tuples. This is useful for assigning comparison values (such as task priorities) alongside the main record being tracked:

>>> h = []
>>> heappush(h, (5, 'write code'))
>>> heappush(h, (7, 'release product'))
>>> heappush(h, (1, 'write spec'))
>>> heappush(h, (3, 'create tests'))
>>> heappop(h)
(1, 'write spec')

Simply push the tuples to the heap, and pop them off when needed:

>>> from heapq import heappush, heappop
>>> 
>>> heap = []
>>> tuples = [(5,"foo",True),(2,"bar", False),(8,"foobar",True)] 
>>> 
>>> for tup in tuples:
...     heappush(heap, tup)
... 
>>> heappop(heap)
(2, 'bar', False)
heappush

Python sorts tuples element-wise, ensure the objects by which you want the tuples to be sorted come first.


How do I sort a dictionary by value?

Python 3.6+
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
{k: v for k, v in sorted(x.items(), key=lambda item: item[1])}  #lambda expression 學起來!
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}









