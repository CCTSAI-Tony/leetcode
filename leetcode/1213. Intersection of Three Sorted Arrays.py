'''
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

 

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
 

Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
'''

#自己想的, time complexity O(l1+l2+l3), space complexity O(1)
#思路: 3 pointers
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        l1, l2, l3 = len(arr1), len(arr2), len(arr3)
        i, j, k = 0, 0, 0
        res = []
        while i < l1 and j < l2 and k < l3:
            num1, num2, num3 = arr1[i], arr2[j], arr3[k]
            if num1 == num2 == num3:
                res.append(num1)
                i += 1
                j += 1
                k += 1
            elif num1 == min(num1, num2, num3):
                i += 1
            elif num2 == min(num1, num2, num3):
                j += 1
            elif num3 == min(num1, num2, num3):
                k += 1
        return res