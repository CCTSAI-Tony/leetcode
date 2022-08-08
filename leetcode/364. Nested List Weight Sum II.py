'''
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, 
now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 8 
Explanation: Four 1's at depth 1, one 2 at depth 2.
Example 2:

Input: [1,[4,[6]]]
Output: 17 
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.
'''

#自己想的, time complexity O(n), space complexity O(n)
#思路: dfs遍歷 搭配defaultdict, 最後要轉換一下key to depth
from collections import defaultdict
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.maxDepth = 1
        dic = defaultdict(int)
        for n in nestedList:
            self.dfs(n, 1, dic)
        res = 0
        for k, v in dic.items():
            key = self.maxDepth - k + 1  #ex: maxDepth = 6, 原本 depth = 1 => 6, 原本depth = 6 => 1
            res += key * v
        return res
        
    def dfs(self, n, depth, dic):
        if n.isInteger():
            self.maxDepth = max(self.maxDepth, depth)
            dic[depth] += n.getInteger()
            return
        for nxt in n.getList():
            self.dfs(nxt, depth + 1, dic)


# 重寫第二次, time complexity O(n), space complexity O(n)
from collections import defaultdict
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        depth_map = defaultdict(int)
        max_depth = 1
        def dfs(item, depth):
            nonlocal max_depth
            if item.isInteger():
                max_depth = max(max_depth, depth)
                depth_map[depth] += item.getInteger()
            else:
                for nxt in item.getList():
                    dfs(nxt, depth + 1)
                
        for item in nestedList:
            dfs(item, 1)
            
        ans = 0
        for k, v in depth_map.items():
            ans += (max_depth - k + 1) * v
        return ans



# 別人想的, bfs solution, time complexity O(n), space complexity O(n)
# 技巧: Now we only initilaize level_sum once. And successive level's integers are added to it. 
# Once a level finishes, we add to total_sum. This naturally implements the multiplication logic - lower level sums are added multiple times to total sum.
class Solution(object):
    def depthSumInverse(self, nestedList):
        total_sum, level_sum = 0, 0
        while len(nestedList):
            next_level_list = []
            for x in nestedList:
                if x.isInteger():
                    level_sum += x.getInteger()
                else:
                    for y in x.getList():
                        next_level_list.append(y)
            total_sum += level_sum
            nestedList = next_level_list
        return total_sum


#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        total, level = 0, 0
        while len(nestedList):
            nextList = []
            for nxt in nestedList:
                if nxt.isInteger():
                    level += nxt.getInteger()
                else:
                    for n in nxt.getList():
                        nextList.append(n)
            total += level
            nestedList = nextList
        return total

