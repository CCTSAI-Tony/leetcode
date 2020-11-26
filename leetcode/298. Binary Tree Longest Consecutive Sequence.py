'''
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
'''

#自己想的, time complexity O(n, space complexity O(1)
#思路: Use dfs 分治法來解題, 注意consecutive sequence 只能ascending order(from parent to child)
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.len = 0
        self.dfs(root)
        return self.len
    
    def dfs(self, node):
        asc = 1
        if node.left:
            l_asc = self.dfs(node.left)
            if node.val + 1 == node.left.val:
                asc = max(asc, l_asc + 1)
        if node.right:
            r_asc = self.dfs(node.right)
            if node.val + 1 == node.right.val:
                asc = max(asc, r_asc + 1)
        self.len = max(self.len, asc)
        return asc









