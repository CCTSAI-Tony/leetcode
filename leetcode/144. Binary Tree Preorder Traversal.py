'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#自己重寫, iterative, time complexity O(n)
#思路: preorder: root => left => right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        res = []
        self.dfs(root, res)
        return res
    
    def dfs(self, node, res):
        if not node:
            return
        res.append(node.val)
        self.dfs(node.left, res)
        self.dfs(node.right, res)

#自己重寫, iterative, time complexity O(n)
#思路: 利用queue 來模仿dfs
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        res = []
        queue = [root]
        while queue:
            node = queue.pop()
            res.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return res






# iteratively 
class Solution:
    def preorderTraversal(self, root):
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res


# recursively
class Solution:
    def preorderTraversal1(self, root):
        res = []
        self.dfs(root, res)
        return res
    
    def dfs(self, root, res):
        if root:
            res.append(root.val)
            self.dfs(root.left, res) #先遍歷左再右
            self.dfs(root.right, res)









