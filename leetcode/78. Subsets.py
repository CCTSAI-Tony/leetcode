# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

#刷題用這個 36ms
#Given a set of distinct integers, nums 沒有duplicates
#自己重寫 time complexity O(2^n), backtracking
#思路: 每個元素只考慮兩種情況, 加進path, 不加進path
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, i, path, res):
        if i == len(nums):
            res.append(path)
            return
        self.dfs(nums, i+1, path+[nums[i]], res)
        self.dfs(nums, i+1, path, res)

# 刷題用這個
# 重寫第二次, time complexity O(2^n), time complexity O(2^n)
# 思路: backtracking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        cur = []
        def dfs(idx):
            for i in range(idx, len(nums)):
                cur.append(nums[i])
                ans.append(cur.copy())
                dfs(i+1)
                cur.pop()
        dfs(0)
        return ans

#自己想的 iteration, 比上面快, 28ms
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        stack.append((0, []))
        while stack:
            index, path = stack.pop()
            if index == len(nums):
                res.append(path)
                continue
            stack.append((index+1, path+[nums[index]]))
            stack.append((index+1, path))
        return res


#bit manipulation, 經典! time complexity O(2^n)
#思路: 利用bit 0, 1 代表 要與不要, for i in range(1 << len(nums)) 就能囊括所有可能
#ex: 5, 00000 > 11111, for i in range(1<<5), bin((1<<5)-1) => 11111
#再利用 for j in range(len(nums)), i & 1 << j, 來把是1的bit 收集下來
class Solution:
    def subsets(self, nums):
        res = []
        for i in range(1<<len(nums)): # 1<<5 32, bin(31) => '0b11111'
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:   #ex: i = 10100 有1的bit 就加入元素 0則跳過 >展現2*2*2*2 的組合, 要與不要
                    tmp.append(nums[j])
           
            res.append(tmp)
        return res

#自己重寫, 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(1<<len(nums)):
            temp = []
            for j in range(len(nums)):
                if i & 1 << j:
                    temp.append(nums[j])
            res.append(temp)
        return res
'''
if i & 1 << j:  

If counter is 320, its binary representation is 101000000, 
which means that the 6th bit (the one corresponding to the value of 64) is set;
 let's test for that bit. The bit mask is generated by shifting 1, which has the binary representation 000000001, 
 6 places to the right, which results in the binary value 001000000. The value of counter, namely:

  101000000
& 001000000
  ---------
  001000000
'''

# DFS recursively 

class Solution:
    def subsets1(self, nums):
        res = []
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res) #注意 path+[nums[i]] nums[i] 要list化 , can only concatnate list to list [2]+[3]= [2,3], [] + [1] = [1]

'''
dfs(nums = [1,2,3], index = 0, path = [], res = [])
|
|__ dfs(nums = [1,2,3], index = 1 , path = [1], res = [[]])
|    |__ dfs(nums = [1,2,3], index = 2 , path = [1,2], res = [[],[1]])
|         |__ dfs(nums = [1,2,3], index = 3 , path = [1,2,3], res = [[],[1], [1,2]])
|              # next: res = [[],[1],[1,2],[1,2,3]]
|              # for loop will not be executed
|
|__ dfs(nums = [1,2,3], index = 2, path = [[2]], res = [[],[1],[1,2],[1,2,3]])
|    |__ dfs(nums = [1,2,3], index = 3 , path = [[2,3]], res = [[],[1],[1,2],[1,2,3],[2])
|              # next iteration: res =  [[],[1],[1,2],[1,2,3],[2],[2,3])
|              # for loop will not be executed
|
|__ dfs(nums = [1,2,3], index = 3, path = [[3]], res =  [[],[1],[1,2],[1,2,3],[2],[2,3])
               # next iteration: res =  [[],[1],[1,2],[1,2,3],[2],[2,3],[3])
               # for loop will not be executed


'''



'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''
# Iteratively
class Solution:
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res
'''
class Solution:
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
            print(res)
        return res
a = Solution()
a.subsets([1,2,3])
[[], [1]]
[[], [1], [2], [1, 2]]
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
Out[9]:
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


'''
































