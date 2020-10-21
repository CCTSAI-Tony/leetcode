'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
'''
#自己想的, time complexity O(n), space complexity O(n)
#思路: dfs 遍歷每層node
from statistics import mean
from collections import defaultdict
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        levels = defaultdict(list)
        self.dfs(root, 0, levels)
        res = [mean(levels[d]) for d in levels] #defaultdict 已經算是另類ordered dict了
        return res
        
        
    def dfs(self, node, depth, levels):
        if not node:
            return
        levels[depth].append(node.val)
        self.dfs(node.left, depth+1, levels)
        self.dfs(node.right, depth+1, levels)

#思路: iteration, bfs
class Solution:
    def averageOfLevels(self, root):
        if root is None:
            return []
        
        result = []
        current_level = [root]
        while current_level:
            level_nodes = []
            next_level = []
            
            for node in current_level:
                level_nodes.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            result.append(sum(level_nodes)/len(level_nodes))
            current_level = next_level
        return result 







