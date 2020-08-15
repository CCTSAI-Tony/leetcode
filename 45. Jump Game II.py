'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
'''

# The basic thoughts underline is a greedy style. Every one more jump, you want to jump as far as possible.
# In Jump Game I, when you at position i, you care about what is the furthest position could be reached from i th position. 
# but here in Jump Game II, instead you care about what would be the next furthest jump could be made when you could reach as far as ith position from last jump. 
# So you iterate all positions could be reached from last jump till i th position to find it out.

#time complexity O(n), 經典greedy
#思路: greedy, 每一步只考慮最大的步數, 到下一步 => 依照前一步jump到達最遠的index, 遍歷前一步到達的地方與最遠的index 之間的index, 更新下一步jump最遠index
#直到超越n-1
class Solution:
    def jump(self, A):
        last_max_reach, current_max_reach = 0 , 0
        njump , i = 0 , 0
        while current_max_reach < len(A)-1:
            while i <= last_max_reach:
                current_max_reach = max(i+A[i],current_max_reach)
                i+=1
            if last_max_reach == current_max_reach: #無法到達終點, 因為nums[i] 有可能 = 0, 不過此題掛保證一定會走到終點, 所以此行可以不用
                return -1
            last_max_reach = current_max_reach
            njump+=1
        return njump


#自己重寫, time complexity O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        pre_max = 0
        cur_max = 0
        i = 0
        n = len(nums)
        jumps = 0
        while cur_max < n-1:
            pre_max = cur_max
            while i <= pre_max:
                cur_max = max(cur_max, i + nums[i])
                i += 1
            if cur_max == pre_max:
                return -1
            jumps += 1
        return jumps


#自己想的 naive bfs time complexity O(sum(nums)), TLE => 遍歷每個num in nums, 每個num 有 nums[i] 選擇
#思路: 每一步都考慮所有可能, 導致TLE
from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        visited = set([0])
        n = len(nums)
        queue = deque([0])
        jumps = 0
        while queue:
            for _ in range(len(queue)):
                idx = queue.popleft()
                if idx == n-1:
                    return jumps
                for i in range(1, nums[idx]+1):
                    new_idx = idx + i
                    if new_idx < n and new_idx not in visited:
                        queue.append(new_idx)
                        visited.add(new_idx)
            jumps += 1
        return -1