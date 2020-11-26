# Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.

# Recall that:

# The node of a binary tree is a leaf if and only if it has no children
# The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of its children is d+1.
# The lowest common ancestor of a set S of nodes is the node A with the largest depth such that every node in S is in the subtree with root A.
 

# Example 1:

# Input: root = [1,2,3]
# Output: [1,2,3]
# Explanation: 
# The deepest leaves are the nodes with values 2 and 3.
# The lowest common ancestor of these leaves is the node with value 1.
# The answer returned is a TreeNode object (not an array) with serialization "[1,2,3]".
# Example 2:

# Input: root = [1,2,3,4]
# Output: [4]
# Example 3:

# Input: root = [1,2,3,4,5]
# Output: [2,4,5]
 

# Constraints:

# The given tree will have between 1 and 1000 nodes.
# Each node of the tree will have a distinct value between 1 and 1000.

#自己想的, time complexity O(n), space complexty O(h)
#思路: dfs 分治法, return (node, depth), 若其中一邊較深, 回報該邊的(node, depth) 至上一層
#若兩邊深度一樣, 回報(當層node, 下層最深的深度), 若兩邊下層最深的深度都是0 代表當層node是該分支最深的node, 自己成為自己的ancestor => return (當層node, 當層depth)
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        return self.dfs(root, 0)[0]
    
    def dfs(self, node, depth):
        if not node:
            return (None, 0)
        left, left_dpt = self.dfs(node.left, depth + 1)
        right, right_dpt = self.dfs(node.right, depth + 1)
        if left_dpt > right_dpt:
            return (left, left_dpt)
        elif left_dpt < right_dpt:
            return (right, right_dpt)
        else:
            if not left_dpt:
                return (node, depth)
            return (node, left_dpt)





