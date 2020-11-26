'''
Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, 
please find out a way you can make one square by using up all those matchsticks. You should not break any stick, 
but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, 
to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.
'''

#自己想的 TLE, backtracking 若完全沒重複的話 time complexity O(4^n), 但對nums.sorted(reverse=True) 2224ms
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums or sum(nums) % 4 != 0:
            return False
        n = len(nums)
        target = sum(nums)//4
        nums.sort(reverse=True) #重點, 提早讓不適合的route return
        visited = []
        sides = [nums[0],0,0,0]
        if self.dfs(0,nums,visited, sides, n-1, target):
            return True
        return False
    
    def dfs(self, i, nums, visited, sides, k, target):
        sides.sort()
        if sides in visited:
            return
        if max(sides) > target: #重點, 提早讓不適合的route return
            return False
        visited.append(sides)
        if i == k:
            if sides[0] == sides[1] == sides[2] == sides[3]:
                return True
            return False
        
        n,w,e,s = sides
        
        if self.dfs(i+1,nums,visited,[n+nums[i+1],w,e,s],k,target):
            return True
        elif self.dfs(i+1,nums,visited,[n,w+nums[i+1],e,s],k,target):
            return True
        elif self.dfs(i+1,nums,visited,[n,w,e+nums[i+1],s],k,target):
            return True
        elif self.dfs(i+1,nums,visited,[n,w,e,s+nums[i+1]],k,target):
            return True


# 刷題用這個, time complexity O(4^n), 若沒nums.sort(reverse=True) TLE, 有則1596ms
# 思路: 想成 partitioning problem, 一開始四個邊都是sum(nums)//4, 每個元素可以自由選擇任何一邊, 若加入 該邊減少那個元素的值, 若該邊的值 < 元素值, 怎不允許其加入
# 最終確認是否有特定partition 可以讓每個元素都加入其中一邊, 這邊注意的是我們先對nums.sort(reverse=True) 是優化, 讓不適合的candidte 提早return, 很關鍵!!
# 還有backtracking 精神, 若candidate fail, 回到上層記得恢復更改過的內容
class Solution(object):
    def makesquare(self, nums):
        if len(nums) < 4 : 
        	return False
        numSum = sum(nums)
        nums.sort(reverse=True)  #大的排前面
        if numSum % 4 != 0: 
        	return False
        target = [numSum/4] * 4;  #切割相等的4等分 block
        return self.dfs(nums,0, target)

    def dfs(self, nums, pos, target):
            if pos == len(nums): 
            	return True
            for i in range(4):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if self.dfs(nums, pos+1, target): 
                    	return True
                    target[i] += nums[pos]  #backtracking 回到上層回復原狀
            return False


# As others pointed out, after proper preprocessing, this problem boiled down to a number partitioning problem which is NP-hard. Nevertheless, 
# if the total number of elements is small, a naive DFS solution is possible.

#自己重寫, 若partition 不對, 會發生四個邊都無法容下自己的狀況
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if len(nums) < 4 or sum(nums) % 4 != 0:
            return False
        target = sum(nums) // 4
        nums.sort(reverse=True)
        sides = [target] * 4
        if self.dfs(0, nums, sides):
            return True
        return False
    
    
    def dfs(self, index, nums, sides):
        if index == len(nums):
            return True
        
        for i in range(4):
            if nums[index] <= sides[i]:
                sides[i] -= nums[index]
                if self.dfs(index+1,nums, sides):
                    return True
                sides[i] += nums[index] 
        return False

# I -- Naive DFS

# For better description of the problem, let's reformulate it in the following symbolic way:

# Given an array nums with n elements, let T(i, s1, s2, s3, s4) denote whether we can partition the subarray nums[0, i](both inclusive) 
# into four disjoint groups such that the sum of elements in the j-th group is sj, with j = 1, 2, 3, 4.

# With this definition, our original problem will be T(n - 1, side, side, side, side) where side is the side length of the square.

# To solve for T(i, s1, s2, s3, s4), note that the last element of the subarray nums[0, i] (which is nums[i]) must belong to one of the disjoint groups, 
# therefore we have the following recurrence relation:

# T(i, s1, s2, s3, s4) = T(i - 1, s1 - nums[i], s2, s3, s4) ||
#                        T(i - 1, s1, s2 - nums[i], s3, s4) ||
#                        T(i - 1, s1, s2, s3 - nums[i], s4) ||
#                        T(i - 1, s1, s2, s3, s4 - nums[i])

# The interpretation is as follows: if nums[i] belongs to the j-th group, we subtract it from sj, 
# then recursively solve for the subproblem with reduced array size and modified group sum. 
# However, we do not know which group it belongs to beforehand, 
# therefore each of the groups will be examined until we either hit the right group or determine that no partition is possible. 
# Also note that if all elements in the input array are positive, 
# an element cannot fall into a group with a group sum smaller than the element itself, i.e., nums[i] cannot belong to the j-th group if nums[i] > sj.

# The termination condition for the recursion is when the subarray is empty, i.e., i = -1, 
# at which time we will check whether the sum of each group is zero. If so, a partition is found and return true; otherwise no partition is possible and return false.


# II -- DFS with sorting

# In the recurrence relation above, we concluded that if nums[i] > sj, it cannot belong to the j-th group, 
# which implies we needn't even bother to try that case. This condition is most likely to be met if we always choose the maximum element 
# that is currently available in the subarray. Also note that the order of elements does not matter in the partition of the array. 
# Therefore we can sort the input array in ascending order before rushing into DFS. This reduced the running time sharply to ~40ms.







