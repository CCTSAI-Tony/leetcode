'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, 
which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note:
You may assume that nums' length ≥ k-1 and k ≥ 1. # add 後 剛好len(nums) == k

2,3,4,5,6
2,3,4,5,5,8
2,3,4,5,5,8,10
2,3,4,5,5,8,9,10
2,3,4,4,5,5,8,9,10
'''




#刷題用這個, time complexity, init=> O(n), add=> O(lgk), 雖然time complexity 不變, 但有優化
#思路: 若add 的值 大於heap 的最小值, 才heapreplace heap裡最小值, 並再執行一次heap堆疊
#若使用heappushpop, 則不管如何 把val 加到heap, 再pop heap裡的最小值, 這樣比上面多了許多不必要的heap堆疊
import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > self.k:
            heapq.heappop(self.pool)  #只留前k大的, 這裡使用的是 min heap

            
    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)  #heapreplace 先pop最小的, 再把新的元素放進去(放進去一樣會執行 heap堆疊排序)
        return self.pool[0]  #pop出來的一定就是 kth largest element, 因為 nums' length ≥ k-1, 第一次add 元素剛好達成k個

#重寫第二次, time complexity init O(n) add O(logn), space complexity O(n)
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        

    def add(self, val: int) -> int:
        if len(self.nums) >= self.k:
            if val > self.nums[0]:
                heapq.heapreplace(self.nums, val)
        else:
            heapq.heappush(self.nums, val)
        return self.nums[0]





#自己重寫 time complexity, init=> O(n), add=> O(lgk)
#思路: 維持一個長度為k的 heap, 該heap[0] 就是第k大的值
from heapq import *
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapify(self.nums)
        self.k = k
        

    def add(self, val: int) -> int:
        heappush(self.nums, val)
        while len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0] #回傳最小值




from heapq import *
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapify(self.nums)
        self.k = k
        while len(self.nums) > self.k:
            heappop(self.nums)
        
        

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heappush(self.nums, val)
        else:
            heappushpop(self.nums, val)
        return self.nums[0]

heapq.heapreplace(heap, item)
從 heap 取出並回傳最小的元素，接著將新的 item 放進heap。heap 的大小不會改變。如果 heap 是空的會產生 IndexError 錯誤。

這個一次完成的操作會比呼叫 heappop() 之後呼叫 heappush() 更有效率，並在維護 heap 的大小不變時更為適當，取出/放入的組合函式一定會從 heap 回傳一個元素並用 item 取代他。

函式的回傳值可能會大於被加入的 item 。如果這不是你期望發生的，可以考慮使用 heappushpop() 替代，他會回傳 heap 的最小值和 item 兩個當中比較小的那個，並將大的留在 heap 內。