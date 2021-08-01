'''
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

 

Constraints:

1 <= nums.length <= 2000
-106 <= nums[i] <= 106
'''

# 刷題用這個, time complexity O(n^2), space complexity O(n)
# 思路: 使用dp 與 greedy, 永遠只紀錄ending i 的最大長度 與該最大長度 ending i 可能性的count
# 在遍歷j 的同時, length[i] 會不斷更新, 所以可以 if length[i] == length[j]: length[i] = length[j]+1
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dp solution, 2 arrays
        # length[i] stores the longest length ending at nums[i]
        # count[i] counts the number of paths with length length[i]
        if not nums:
            return 0
        n = len(nums)
        length = [1] * n
        count  = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] == length[j]:  # 最大長度一直被更新
                        length[i] = length[j]+1
                        count[i]  = count[j]
                    elif length[i] == length[j]+1: #之前length[i] 已被更新, 此時更新count
                        count[i] += count[j]

        maxLength = max(length)
        return sum([count[i] for i in range(n) if length[i] == maxLength])

#重寫第二次, time complexity O(n^2), space complexity O(n^2)
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n
        count = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] == length[j]:
                        length[i] += 1
                        count[i] = count[j]
                    elif length[i] == length[j] + 1:
                        count[i] += count[j]
        max_len = max(length)
        return sum(count[i] for i in range(n) if length[i] == max_len)
