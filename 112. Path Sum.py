'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#自己想的 time complexity O(n), 52ms
#思路: 經典dfs 遍歷issue, base case, if not node.left and node.right => 回傳此path + node.val == sum
#並利用分治法 回傳left, right 子樹結果
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        return self.dfs(root, sum, 0)
    
    def dfs(self, node, sum, path):
        if not node.left and not node.right:
            return path + node.val == sum
        left, right = False, False
        if node.left:
            left = self.dfs(node.left, sum, path + node.val)
        if node.right:
            right = self.dfs(node.right, sum, path + node.val)
        return left or right




# DFS Recursively 
class Solution:
    def hasPathSum1(self, root, sum):
        res = []
        self.dfs(root, sum, res)
        return any(res)
    
    def dfs(self, root, target, res):
        if root:
            if not root.left and not root.right:
                if root.val == target:
                    res.append(True)
            if root.left:
                self.dfs(root.left, target-root.val, res)
            if root.right:
                self.dfs(root.right, target-root.val, res)
'''
any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
元素除了是 0、空、FALSE 外都算 TRUE。

any(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0
True

any((0, '', False))        # 元组tuple，元素全为0,'',false
False

any([]) # 空列表
False

'''


# DFS + stack   
class Solution:
    def hasPathSum2(self, root, sum):
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right:
                if val == sum:
                    return True
            if curr.right:
                stack.append((curr.right, val+curr.right.val))
            if curr.left:
                stack.append((curr.left, val+curr.left.val))
        return False





