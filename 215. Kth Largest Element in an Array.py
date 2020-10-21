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

#quick select, 刷題最佳解, time complexity O(n) in the average case, O(n^2) in the worst case, space complexity O(1)
#思路: quick sort 的變形
import random
class Solution:
    def findKthLargest(self, nums, k):

        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element
            
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest index
        return select(0, len(nums) - 1, len(nums) - k)


#自己重寫, time complexity O(n) in average, worst case O(n^2)
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.select(0, len(nums)-1, nums, len(nums)-k)
     
    
    def select(self, left, right, nums, k):
        pivot = random.randint(left, right)
        pivot_final = self.partition(left, right, k, nums)
        if pivot_final > k:
            return self.select(left, pivot_final-1, nums, k)
        elif pivot_final < k:
            return self.select(pivot_final+1, right, nums, k)
        else:
            return nums[pivot_final]
        
        
    def partition(self, left, right, pivot, nums):
        pivot_num = nums[pivot]
        nums[pivot], nums[right] = nums[right], nums[pivot]
        store_idx = left
        for i in range(left, right):
            if nums[i] < pivot_num:
                nums[i], nums[store_idx] = nums[store_idx], nums[i]
                store_idx += 1
        nums[right], nums[store_idx] = nums[store_idx], nums[right]
        return store_idx






#quick sort
import random
class Solution:
    def quicksort(self, nums):

        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def sort(left, right):
            if left == right:       
                return
            
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            if pivot_index > left:
                sort(left, pivot_index-1)
            if pivot_index < right:
                sort(pivot_index+1, right)

        return sort(0, len(nums) - 1)



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
#思路: heap
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



