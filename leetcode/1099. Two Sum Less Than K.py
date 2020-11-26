'''
Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. 
If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.
 

Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
'''


# 刷題用這個, time complexity O(nlogn)
# 思路: 先對A sort => 再用two pointer
# two pointer => 利用A 頭尾兩端i, j加起來的值看是否 < K, 若是 i += 1, 若不是 j-= 1, 直到 i=j, 若加起來的值< K 則更新 max_s 值, 若組合沒有都是>=K, return -1
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        max_s = -1
        A.sort()
        i, j = 0, len(A)-1
        while i < j:
            if (A[i] + A[j]) < K:
                max_s = max(max_s, A[i] + A[j])
                i += 1
            else:
                j -= 1
        return max_s







#模板2 自己想的, time complexity O(nlogn), 48ms
#思路: (A[i] + A[j]) < K, fix A[i] 利用binary search 找尋最大可能值 A[j], A[j] in A[i+1:]
#若找不到則index in A[i+1:] = -1, 若找到 => max_s = max(max_s, A[i]+ A[i+1:][index])
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        max_s = float("-inf")
        A.sort()
        for i in range(len(A)-1):
            target = K-A[i]
            index = self.binary(A[i+1:], target)
            if index >= 0:
                max_s = max(max_s, A[i]+ A[i+1:][index])
        return max_s if max_s != float("-inf") else -1
                
    def binary(self, nums, target):
        l, r = 0, len(nums)-1
        while l + 1 < r:
            mid = l + (r - l) //2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid
        if nums[l] >= target:
            return l-1
        elif nums[r] >= target:
            return r-1
        return r







