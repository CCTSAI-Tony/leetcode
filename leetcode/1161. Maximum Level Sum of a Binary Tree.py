'''
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

 

Example 1:



Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
 

Note:

The number of nodes in the given tree is between 1 and 10^4.
-10^5 <= node.val <= 10^5
'''

#自己想的, dfs, time complexity O(n), 620ms, 刷題用這個
#思路: 利用dfs 遍歷每層node, 並把node.val 加到特定level
#python3.7 的 dict, 已經預設按建立順序ordered了, 也就是可以取代OrderedDict
import collections
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return None
        levels = collections.defaultdict(int)
        self.dfs(root, 1, levels)
        max_sum = max(levels.values())
        for i in levels.keys():
            if levels[i] == max_sum:
                return i
        
        
    def dfs(self, node, level, levels):
        if not node:
            return
        levels[level] += node.val
        self.dfs(node.left, level+1, levels)
        self.dfs(node.right, level+1, levels)













