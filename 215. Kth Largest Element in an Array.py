'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

# O(k+(n-k)lgk) time, min-heap
import heapq 
class Solution:
    def findKthLargest4(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums)-k): #保留k個元素
            heapq.heappop(heap) #從小到大pop
        return heapq.heappop(heap)

'''
https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

import heapq
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))] list comprehension

values= [5,3,7,4,6,1,9,8,2]
heapsort(values)
=>[1, 2, 3, 4, 5, 6, 7, 8, 9]

这类似于 sorted(iterable)，但与 sorted() 不同的是这个实现是不稳定的
'''
#刷題用這個 time complexity O(klogn), min-heap
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        for i in range(k):
            ans = heapq.heappop(heap)
        return -ans

# O(nk) time, selection sort idea
# 思路: 先找到整段區間最大的擺到最後一個位置, 縮小區間找到次大的放到倒數第二個位置....
class Solution:
    def findKthLargest3(self, nums, k):
        for i in range(len(nums), len(nums)-k, -1): #range(9,5,-1)> i = 9,8,7,6, 這邊len(nums)-k 實際為 len(nums)-k + 1
            tmp = 0
            for j in range(i):
                if nums[j] > nums[tmp]:
                    tmp = j
            nums[tmp], nums[i-1] = nums[i-1], nums[tmp] #最大到最小從右到左排序, nums[i-1] for index issue
        return nums[len(nums)-k]  #倒數第k的元素
#



