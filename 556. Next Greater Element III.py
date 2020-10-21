'''
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. 
If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21
 

Example 2:

Input: 21
Output: -1
'''
# Introducion :

# If all digits sorted in descending order, then output is always -1. For example, 321.
# For other cases, we need to process the number from rightmost side (why? because we need to find the smallest of all greater numbers)
# Algorithm:

# Traverse the given number from rightmost digit, keep traversing till you find a digit which is smaller than the previously traversed digit. 
# For example, if the input number is “534976”, we stop at 4 because 4 is smaller than next digit 9. If we do not find such a digit, then output is “Not Possible”.

# Now search the right side of above found digit ‘d’ for the smallest digit greater than ‘d’. For “534976″, the right side of 4 contains “976”. 
# The smallest digit greater than 4 is 6.

# Swap the above found two digits, we get 536974 in above example.

# Now sort all digits from position next to ‘d’ to the end of number. The number that we get after sorting is the output. Finally, for above example, 
# We get “536479” which is the next greater number for input 534976.

# In last step we should check weather the result is a 32-bit number or not.

#ex: 19876 => 61879
#刷題用這個
#思路: 雙指針, i指針先倒序遍歷是否有nums[i] < nums[i+1], 代表有next的可能, 之後另一指針j倒序遍歷看是否有nums[j] > nums[i], 找尋比nums[i]大的值中的最小值互相調換
#調換後, nums[i+1:] 要倒過來才會形成下一個最小值, 注意 若res > 2**31-1 要return -1
#自己重寫 time complexity O(n)
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        N = len(nums)
        i, j = N-2, N-1
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i < 0:
            return -1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        res = int("".join(nums[:i+1] + nums[i+1:][::-1]))
        return res if res <= 2**31-1 else -1




