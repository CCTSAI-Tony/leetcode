# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:

# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

#自己重寫, time complexity O(n), space complexity O(1)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.invert(root)
        return root
    
    def invert(self, node):
        left, right = node.left, node.right
        node.left = right
        node.right = left
        if node.left:
            self.invert(node.left)
        if node.right:
            self.invert(node.right)
        return node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
from collections import deque
class Solution:
    def invertTree2(self, root):
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left #exchange right to left
                queue.append(node.left) #it doesn't matter if append left first or right first, but keep left first cause BFS spirit
                queue.append(node.right)
        return root

# DFS
class Solution:
    def invertTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left]) #extend method just accepts iterable item
        return root


# recursively, good method, plz think it twice!
class Solution: 
    def invertTree1(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root












