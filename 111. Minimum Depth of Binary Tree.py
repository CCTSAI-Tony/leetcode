'''
111. Minimum Depth of Binary Tree
Easy

1054

595

Add to List

Share
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
# DFS
class Solution:
    def minDepth1(self, root):
        if not root:
            return 0
        if None in [root.left, root.right]: # if the node's one side has a none, so we choose the other side to find the shortest leaf
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1  #choose the smaller path

#刷題用這個
#自己重寫, time complexity O(n), space complexity O(h)
#思路: dfs 分治, 這裏要求最短leaf的距離, leaf的定義是沒children, 所以只有一邊為none不算leaf node
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root, 1)
    
    def dfs(self, node, depth):
        if not node.left and not node.right:
            return depth
        left, right = float("inf"), float("inf")
        if node.left:
            left = self.dfs(node.left, depth+1)
        if node.right:
            right = self.dfs(node.right, depth+1)
        return min(left, right)



