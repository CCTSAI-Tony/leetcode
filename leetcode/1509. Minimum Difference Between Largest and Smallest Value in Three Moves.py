'''
You are given an integer array nums. In one move, you can choose one element of nums and change it by any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.

 

Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.
Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
The difference between the maximum and minimum is 1-0 = 1.
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

'''
Intuition
If we can do 0 move, return max(A) - min(A)
If we can do 1 move, return min(the second max(A) - min(A), the max(A) - second min(A))
and so on.


Explanation
We have 4 plans:

kill 3 biggest elements
kill 2 biggest elements + 1 smallest elements
kill 1 biggest elements + 2 smallest elements
kill 3 smallest elements

Example from @himanshusingh11:

A = [1,5,6,13,14,15,16,17]
n = 8

Case 1: kill 3 biggest elements

All three biggest elements can be replaced with 14
[1,5,6,13,14,15,16,17] -> [1,5,6,13,14,14,14,14] == can be written as A[n-4] - A[0] == (14-1 = 13)

Case 2: kill 2 biggest elements + 1 smallest elements

[1,5,6,13,14,15,16,17] -> [5,5,6,13,14,15,15,15] == can be written as A[n-3] - A[1] == (15-5 = 10)

Case 3: kill 1 biggest elements + 2 smallest elements

[1,5,6,13,14,15,16,17] -> [6,6,6,13,14,15,16,16] == can be written as A[n-2] - A[2] == (16-6 = 10)

Case 4: kill 3 smallest elements

[1,5,6,13,14,15,16,17] -> [13,13,13,13,14,15,16,17] == can be written as A[n-1] - A[3] == (17-13 = 4)

Answer is minimum of all these cases!


Solution 1: Quick Sort
I used quick sort to find out the biggest and smallest
So time and space are O(quick sort)
'''

# 刷題用這個, time complexity O(nlogn), space complexity O(1)
# 思路: 先排序, 因為只能改變三個, 有幾種可能 1, 把前三大變成第四大 2, 把前兩大變成第三大, 把第一小變成第二小 .....
class Solution:
    def minDifference(self, nums: List[int]) -> int:
    	nums.sort()
    	return min(b - a for a, b in zip(nums[:4], nums[-4:]))

# 重寫第二次, time complexity O(nlogn), space complexity O(1)
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        return min([b - a for a, b in zip(nums[:4], nums[-4:])])
















