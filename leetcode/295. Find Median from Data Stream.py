'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. 
So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
'''

# The invariant of the algorithm is two heaps, small and large, each represent half of the current list. 
# The length of smaller half is kept to be n / 2 at all time and the length of the larger half is either n // 2 or n // 2 + 1 depend on n's parity.

# This way we only need to peek the two heaps' top number to calculate median.

# Any time before we add a new number, there are two scenarios, (total n numbers, k = n // 2):

# (1) length of (small, large) == (k, k)
# (2) length of (small, large) == (k, k + 1)
# After adding the number, total (n + 1) numbers, they will become:

# (1) length of (small, large) == (k, k + 1)
# (2) length of (small, large) == (k + 1, k + 1)
# Here we take the first scenario for example, we know the large will gain one more item and small will remain the same size, 
# but we cannot just push the item into large. What we should do is we push the new number into small and pop the maximum item 
# from small then push it into large (all the pop and push here are heappop and heappush). By doing this kind of operations 
# for the two scenarios we can keep our invariant.

# Therefore to add a number, we have 3 O(log n) heap operations. Luckily the heapq provided us a function "heappushpop" 
# which saves some time by combine two into one. The document says:

# Push item on the heap, then pop and return the smallest item from the heap. 
# The combined action runs more efficiently than heappush() followed by a separate call to heappop().
# Alltogether, the add operation is O(logn), The findMedian operation is O(1).

# Note that the heapq in python is a min heap, thus we need to invert the values in the smaller half to mimic a "max heap".

# A further observation is that the two scenarios take turns when adding numbers, 
# thus it is possible to combine the two into one. For this please see stefan's post

#好題!
#addNum time complexity O(lgn), findMedian time complexity O(1)
#思路: 利用兩個heap 分別對應小的一半, 大的一半, 我們設計當大小一半的數量一樣時, 下次加item 會使大的多一個, 此時find min 就是pop大的[0], min heap
#小比大少1時, 下次加item 會使小與大相等
#可以自己思考一下, 大小一樣時 heappush(self.large, -heappushpop(self.small, -num)), 小比大少1 heappush(self.small, -heappushpop(self.large, num)) 
#小的最大值給大的, 大的最小值給小的, 維持小的元素都比大的元素小, 要注意的技巧, minq 如何變成 maxq, 值乘一個負號就行, 與heappushpop
from heapq import *
class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):  #相等時, 我們要add  一個item 給large
            heappush(self.large, -heappushpop(self.small, -num)) #-heappushpop(self.small, -num) 把num變負pushpop後才乘負變正
        else:
            heappush(self.small, -heappushpop(self.large, num)) #push a number to large, then, pop the smallest one from large and make it negative and push it to small

    def findMedian(self): #這裡千萬不能 heappop, 因為之後可能還有很多 findMedian 指令, 要保持數據完整性
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0 #self.small 裡面的數據是-num 所以才要乘負變正
        else:
            return float(self.large[0]) #設計large 多一個

# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 388 ms

#自己重寫, time complexity addNum log(n), findMedian O(1), space complexity O(n)
from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.big = []
        

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.big):
            heappush(self.big, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.big, num))
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.big):
            return (self.big[0] - self.small[0]) / 2
        else:
            return self.big[0]

#重寫第二次, time complexity addNum log(n), findMedian O(1), space complexity O(n)
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        else:
            return self.large[0]


# 1. If all integer numbers from the stream are between 0 and 100, how would you optimize it?

# We can maintain an integer array of length 100 to store the count of each number along with a total count. 
# Then, we can iterate over the array to find the middle value to get our median.

# Time and space complexity would be O(100) = O(1).

# 2. If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

# In this case, we need an integer array of length 100 and a hashmap for these numbers that are not in [0,100].
















