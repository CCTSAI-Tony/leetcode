'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#自己重寫, time complexity O(n), 刷題用這個
#思路: dfs, 分治法, return max(left, right) + 1
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root)
        
    
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return max(left, right) + 1



#dfs
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return self.dfs(root)
    def dfs(self,root):
        if not root:
            return 0
        return 1 +max(self.dfs(root.left), self.dfs(root.right))


#DFS遍历 top>down
#储存全局变量，在每层DFS进行对全局变量的比对。
class Solution(object):
    def maxDepth(self, root):
        self.max_depth = 0 #這個變數很重要 全局变量(嚴格來說是class valuable) 可以避免local valuable 衝突 @@因為int 不像list 可以經由dfs改變內容
        self.dfs(root, 1)
        return self.max_depth

    def dfs(self, root, depth):
        if not root: 
            return #回上層
        self.max_depth = max(depth, self.max_depth)
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)

'''
DFS分制 bottom>up

left和right用post-order的方法，先遍历到树的最底层(leaf)，然后从底层开始返回报告，这种思路一定要记得写好Base Case，也就是递归终止的条件：
if not root: return 0

Base Case写完要思考最终希望返回的定义，这道题求得是最长的高度，那么在返回至上一层的时候，当前层数需要对之前返回上来的高度进行比对，因此有了
max(left, right)

然后结束比对以后，还需要向上返回前加上当前的这一层的高度，所以之后要+1

'''
#DFS分制 最簡潔
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1 #向上返回前加上当前的这一层的高度，所以之后要+1
