'''
Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. 
If there is a tie, the smaller elements are always preferred.

 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 10^4
Absolute value of elements in the array and x will not exceed 104
'''


#刷題用這個, time complexity O(logn + k)
class Solution:
    def findClosestElements(self, arr, k, x):
        index = self.findIndex(arr, x)
        l, r = index, index

        while r - l < k:
            if l == 0: 
                return arr[:k]
            if r == len(arr): 
                return arr[-k:]
            if x - arr[l-1] <= arr[r] - x: #看誰比較近
                l -= 1
            else: 
                r += 1
        return arr[l:r]
            

    def findIndex(self, arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l


#重寫一次, time complexity O(logn + k), space complexity O(1)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = self.findIndex(arr, x)
        l, r = index, index
        while r - l < k:
            if r == len(arr): #左閉右開
                return arr[-k:]
            elif l == 0:
                return arr[:k]
            else:
                if x - arr[l-1] <= arr[r] - x:
                    l -= 1
                else:
                    r += 1
        return arr[l:r]
                
        
    def findIndex(self, arr, x):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] >= x:
                r -= 1
            else:
                l += 1
        return l








#自己想的, time complexity O(nlogn), space complexity O(n)
#思路: heap
import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            heapq.heappush(heap, (abs(num-x), num))
        res = []
        for _ in range(k):
            temp = heapq.heappop(heap)[1]
            res.append(temp)
        return sorted(res)