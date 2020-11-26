
# backtrackong 面試用這個

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        self.dfs(nums, [], res)
        return res                
    def dfs(self, nums, path, res): #Depth-First Search
        if not nums: # nums is none
            res.add(tuple(path))    #list tuple化 才能加進set
                    # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)                   
            
                   
'''
without using set()
'''

class Solution():
    def permuteUnique(self, nums):
        if not nums:
            return []
        nums.sort()
        ret = [[]] #len(ret)=1
        for n in nums:
            new_ret = []
            l = len(ret[-1])
            for seq in ret:
                for i in range(l, -1, -1):  # l>>>0
                    if i < l and seq[i] == n: #just insert only after the same element.
                        break
                    new_ret.append(seq[:i] + [n] + seq[i:])
            ret = new_ret
        return ret

        '''
        Duplication happens when we insert the duplicated element before and after the same element, 
        to eliminate duplicates, just insert only after the same element.

        ret = [[]]

        l = len(ret[-1]) = 0

        a = []
        a.append([3])
        print(a)

        a = []
        a.append(3)
        print(a)
        
        input: [1,1,3]
        第一輪
        new_ret: [[1]]
        ret: [[1]]
        第2輪
        new_ret: [[1,1]] 
        ret: [[1,1]] ,for seq in ret [1,1] 在第3輪是唯一的seq
        第3輪
        new_ret: [[1,1,3],[1,3,1],[3,1,1]]
        ret: [[1,1,3],[1,3,1],[3,1,1]] return

        a = Solution()
        a.permuteUnique([1,2,3])
        [[1]]
        [[1, 2], [2, 1]]
        [[1, 2, 3], [1, 3, 2], [3, 1, 2]]
        [[1, 2, 3], [1, 3, 2], [3, 1, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1]]

        a = Solution()
        a.permuteUnique([1,1,3])
        [[1]]
        [[1, 1]]
        [[1, 1, 3], [1, 3, 1], [3, 1, 1]]


    
        '''