'''
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
 

Example 1:


Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers 
since per each level it does not matter the order on which elements are returned.
Example 2:

Input: root = [1]
Output: [[1]]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
'''

# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: dfs, 左右分治法, depth, 在dfs 回報值給上層途中, 也順便做了一些事
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []
        self.dfs(root)
        return self.ans
    
    def dfs(self, node):
        if not node:
            return 0
        depth = max(self.dfs(node.left), self.dfs(node.right)) + 1
        if len(self.ans) < depth:
            self.ans.append([])
        self.ans[depth-1].append(node.val)
        return depth


