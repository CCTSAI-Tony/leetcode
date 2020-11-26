'''
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
'''

#自己想的 time complexity O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return None
        res = []
        self.dfs(root, L, R, res)
        if res:
            return sum(res)
        return None
       
            
    #in-order traversal, 其他traversal 也行, 只要遍歷到全部就行
    def dfs(self, node, L, R, res):
        if not node:
            return 
        self.dfs(node.left, L, R, res)    
        if L <= node.val<= R:
            res.append(node.val)
        self.dfs(node.right, L, R, res)


 # InOrder Traversal, 參考別人的, 跟上面效率差不多, 但這是用傳參的方式直接累加
 # 思路: 利用inorder recursion traverse, 收集在區間的值
 # bottom up
 class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return self.dfs(root, L, R, 0)
    
    def dfs(self, node, L, R, value):
        if not node:
            return value
        value = self.dfs(node.left, L, R, value) # self.inorder(root.left, value, L, R) 改變value
        if L <= node.val <= R:
            value += node.val
        value = self.dfs(node.right, L, R, value)
        return value













