'''
Given an integer array arr and an integer difference, 
return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is [1,2,3,4].
Example 2:

Input: arr = [1,3,5,7], difference = 1
Output: 1
Explanation: The longest arithmetic subsequence is any single element.
Example 3:

Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].
 

Constraints:

1 <= arr.length <= 105
-104 <= arr[i], difference <= 104
'''

'''
This is a little bit different than regular dp problems, we use hash table instead of arrays for dp table.
For given number in the input array x, we want to find if x-d exists before x:
If x-d exists, then it means that x-d can be extended with x, thus the longest subsequence up to x is dp[x-d] + 1, which means dp[x] = dp[x-1] + 1
Else if x-d does not exists before x (never seen before x), x is the first element in potential sequence, so dp[x] = 1
After iterating all elements in input array, we pick the largest value in the hash table.
'''

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
        dp is a hashtable, dp[x] is the longest subsequence ending with number x
        """
        dp = {}
        for x in arr:
            if x - difference in dp:
                dp[x] = dp[x-difference] + 1
            else:
                dp[x] = 1
            
        return max(dp.values())


# 重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = {}
        for num in arr:
            if (num - difference) in memo:
                memo[num] = memo[(num - difference)] + 1
            else:
                memo[num] = 1
        return max(memo.values())

