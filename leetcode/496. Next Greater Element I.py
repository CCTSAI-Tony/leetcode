'''
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. 
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
'''

#自己想的, time complexity O(n) 32ms 99%
#思路: 利用stack 來存儲遞減序列, 一指針遍歷nums2, 若當前num > stack[-1] 代表 stack[-1] 找到最近比它大的元素, 從stack pop掉 紀錄到dict, 
#持續 pop掉stack[-1] , 直到num < stack[-1], append num to stack, 遍歷完nums2 換遍歷nums1, 若num 出現在dic 代表有找到 next greater element, 若沒有則 return -1
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        stack = []
        ans = []
        for num in nums2:
            while stack and num > stack[-1]:
                pre = stack.pop()
                dic[pre] = num
            stack.append(num)
        for num in nums1:
            if num not in dic:
                ans.append(-1)
            else:
                ans.append(dic[num])
        return ans





