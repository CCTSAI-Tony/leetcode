'''
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
Example 2:

Input: nums = [1,10,2,9]
Output: 16
 

Constraints:

n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

'''
Idea:
This problem is deceptive in its simplicity. 
Ultimately, the value to which you want to set each element equal is the median of the sorted nums array. 
To come to this realization, we have to first think about the nature of the problem.

Let's consider a possible scenario in which we've decided that our target value is x which would take ans number of moves to complete. 
What would happen to ans if we increased x by 1? 
If we did, each element that is below the new x would have to spend another move to get up to x, 
but every element that is above the new x would have to spend one less move to get down to x.

This means that x should naturally move up if there are more elements above x than below. 
It also means the inverse, that x should move down if there are more elements below x than above. 
The natural outcome of this is that x will settle at a spot where there are the same number of elements on either side, 
which is the median value of nums.

To find the median value, we'll have to first sort nums. If nums has an even number of elements, 
any value between the two middle elements, inclusive, will work for calculating the answer, 
so we don't have to worry about which of the two elements we use for our solution.

After we have the median value, 
we can just iterate through nums and find the sum of the differences of each number from the median value, which should be our answer.

Time Complexity: O(N * log N) where N is the length of nums, for sorting nums
Space Complexity: O(1)

'''

# 刷題用這個, time complexity O(nlogn), space complexity O(1)
# 思路: greedy, 找中位數 median 得到的moves 會最小
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        ans, median = 0, nums[len(nums) // 2]
        for num in nums: 
            ans += abs(median - num)
        return ans


# 重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums) - 1
        nums.sort()
        median = nums[n//2]
        moves = 0
        for num in nums:
            moves += abs(num - median)
        return moves












