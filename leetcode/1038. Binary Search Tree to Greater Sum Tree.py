# Given the root of a binary search tree with distinct values, 
# modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

# As a reminder, a binary search tree is a tree that satisfies these constraints:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:



# Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
 

# Constraints:

# The number of nodes in the tree is between 1 and 100.
# Each node will have value between 0 and 100.
# The given tree is a binary search tree.
# Note: This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/

# Given the root of a binary search tree with distinct values, 這句話很重要!!


#自己想的, time complexity O(n), iterative inorder traversal
#思路: binary search tree => inorder traversal, 從最大的遍歷到最小, 遍歷到該node, sumToNode 就加上該node值, 該node的值設為sumToNode
#ex: 最大的node, sumToNode 就是自己 => 次大的node, sumToNode(包含最大node的值) + 次大的值 => assaign to 次大 node.val, 持續到最小node
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        queue = [(root, False)]
        sumToNode = 0
        while queue:
            node, visited = queue.pop()
            if node:
                if not visited:
                    queue.append((node.left, False))
                    queue.append((node, True))
                    queue.append((node.right, False))
                else:
                    sumToNode += node.val
                    node.val = sumToNode
        return root

#自己想的, dfs recusrion inorder traversal, time complexity O(n)
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sumToNode = 0
        self.dfs(root)
        return root
        
    def dfs(self, node):
        if not node:
            return
        self.dfs(node.right)
        self.sumToNode += node.val
        node.val = self.sumToNode
        self.dfs(node.left)








