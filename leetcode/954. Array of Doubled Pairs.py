'''
Given an integer array of even length arr, 
return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.

 

Example 1:

Input: arr = [3,1,3,6]
Output: false
Example 2:

Input: arr = [2,1,2,6]
Output: false
Example 3:

Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
 

Constraints:

2 <= arr.length <= 3 * 104
arr.length is even.
-105 <= arr[i] <= 105
'''

# 刷題用這個, time complexity O(nlogn), space complexity O(n)
# 思路: 使用sort 與 dict
class Solution(object):
    def canReorderDoubled(self, A):
        count = collections.Counter(A)
        for x in sorted(A, key = abs):
            if count[x] == 0: 
                continue
            if count[2*x] == 0: 
                return False
            count[x] -= 1
            count[2*x] -= 1

        return True

# 重寫第二次, time complexity O(nlogn), space complexity O(n)
from collections import Counter
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr_count = Counter(arr)
        for num in sorted(arr, key=abs):
            if arr_count[num] == 0:
                continue
            elif arr_count[2*num] <= 0:
                return False
            else:
                arr_count[num] -= 1
                arr_count[2*num] -= 1
        return True