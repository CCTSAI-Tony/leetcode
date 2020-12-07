'''
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''

#刷題用這個, 自己想的, time complexity O(n), space complexity O(1)
#思路: position sort
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first, second, third = float("-inf"), float("-inf"), float("-inf")
        for num in nums:
            if num == first or num == second or num == third:
                continue
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
        if third != float("-inf"):
            return third
        else:
            return first








            