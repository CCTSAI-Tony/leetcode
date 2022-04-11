'''
The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

Each element of nums is in exactly one pair, and
The maximum pair sum is minimized.
Return the minimized maximum pair sum after optimally pairing up the elements.

 

Example 1:

Input: nums = [3,5,2,3]
Output: 7
Explanation: The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
Example 2:

Input: nums = [3,5,4,2,4,6]
Output: 8
Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.
 

Constraints:

n == nums.length
2 <= n <= 105
n is even.
1 <= nums[i] <= 105
'''

'''
A = sorted(nums)

Assume there is an optimal solution S composed by pairs P1, P2, P3, P4...
Without generality assuming that A[0], A[-1] reside in pairs P1, P2 respectively.
P1 = (A[0], A[i]), P2 = (A[j], A[-1]) where A[0] <= A[i], A[j] <= A[-1]

Replace P1, P2 with P1' = (A[0], A[-1]), P2' = (A[i], A[j]) and I have S' = P1', P2', P3, P4...... which doesn't generate a worse solution

Proof:
Sum(P2) >= Sum(P1) , A[-1] >= A[i] and A[j] >= A[0] => A[-1] + A[j] >= A[i] + A[0]
Sum(P2) >= Sum(P1'), A[j] >= A[0] => A[j] + A[-1] >= A[0] + A[-1]
Sum(P2) >= Sum(P2'), A[-1] >= A[i] => A[j] + A[-1] >= A[i] + A[j]
=> Sum(P1) <= Sum(P2) and P1' and P2' make no bigger sum than P2, such adjustment doesn't generate a worse solution

Follow the procedure, we can adjust the optimal solution S to greedy solution G where G is composed by (A[0], A[-1]), (A[1], A[-2]), (A[2], A[-3])..... And G should be no worse than S.

Since S is the optimal solution and G is no worse than it, G should be one of the optimal solution, too.
'''


# 刷題用這個, time complexity O(nlogn), space complexity O(n)
# 思路: 證明請看上面, 有點技巧
class Solution(object):
    def minPairSum(self, nums):
        """ 
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[i] + nums[-(i + 1)] for i in range(len(nums) // 2))



# 重寫第二次, time complexity O(nlogn), space complexity O(n)
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[i] + nums[-(i+1)] for i in range(len(nums) // 2))











