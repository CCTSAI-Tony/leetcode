'''
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

 

Example 1:

Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
Example 2:

Input: values = [1,2]
Output: 2
 

Constraints:

2 <= values.length <= 5 * 104
1 <= values[i] <= 1000
'''

The goal is to keep track of:

Maximum So far and add it to the cur_cell and maintain maximum result
Here, max_so_far contains : A[i] + i
Original Given Formula : A[i] + A[j] + i - j

Break in two parts : A[i] + i and A[j] -j
Keep MAX_VALUE of first part among the elements seen so far
Add the current element to max_so_far and check the result is changing or not
Also, keep updating the max_so_far at each step


#刷題用這個, time complexity O(n), space complexity O(1)
#思路: a[i] + a[j] + i - j => 看成 a[i] + i and a[j] - j, 使用one pass 遍歷, 保持最大的第一部分, 遍歷的途中加入第二部分, 並保存最大可能值
class Solution:
    def maxScoreSightseeingPair(self, a: List[int]) -> int:
        max_so_far,result = a[0],0
        
        for i in range(1,len(a)):
            result = max(result, max_so_far + a[i] - i)
            max_so_far = max(max_so_far, a[i] + i)
            
        return result

#重寫第一次, time complexity O(n), space complexity O(1)
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_first_part = 0
        res = 0
        for i, v in enumerate(values):
            res = max(res, max_first_part + v - i)
            max_first_part = max(max_first_part, v + i)
        return res




