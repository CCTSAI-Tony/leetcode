'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#自己重寫, 刷題用這個, time complexity O(n)
#思路: pre-order traversal, 若root.left不等於None, 先暫存root.right, 在把root.left調換至root.right, recursion root.right, 最後再接回temp
#若root.left = None, 直接recursion root.right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
        
    def dfs(self, root):
        if not root:
            return 
        if root.left:  #若root.left = None, 直接處理root.right就行
            temp = root.right
            root.right = root.left
            root.left = None
            self.dfs(root.right)
            while root.right:
                root = root.right
            root.right = temp
            self.dfs(root.right)
        else:
            self.dfs(root.right)


 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#if a node has a left subtree, we will move it to the right , at the end, we will append the right tree!
class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        if root.left:
            temp = root.right #隔離原右支線
            root.right = root.left #同步左右支線
            root.left = None #把左支線封住只留右支線
            self.flatten(root.right) #從右支線往下走
            while root.right:
                root = root.right #先往目前右支線盡頭走
            root.right = temp #把temp(原右支線)接續回去
        self.flatten(root.right) #往原右支線走








