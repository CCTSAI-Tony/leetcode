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


#自己重寫, time complexity O(n), space complexity O(h) => 93.99%
#思路: 先把right 暫存, node.right = node.left, set left to None => 利用recursion return right 的最底端node, 若temp is no none, 最底端node.right 接回temp
#一樣再對node.right 做recursion來找最底端node, 最後return 最底端node 給上一層接temp
#若 not node.left, 直接搜索node.right 最底層node
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        if not root.left and not root.right:
            return root
        if root.left:
            temp = root.right
            root.right = root.left
            root.left = None #記得這邊要set None
            root = self.flatten(root.right)
            if temp:
                root.right = temp
                root = self.flatten(root.right)
            return root
        else:
            return self.flatten(root.right)


#重寫第二次, time complexity O(n), space complexity O(h)
#注意: node.left 移至node.right 記得set node.left = None
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
        
    def dfs(self, node):
        if not node:
            return
        if not node.left and not node.right:
            return node
        right = node.right
        left_last = self.dfs(node.left)
        right_last = self.dfs(node.right)
        if left_last and right_last:
            node.right = node.left
            node.left = None
            left_last.right = right
            return right_last
        elif not right_last:
            node.right = node.left
            node.left = None
            return left_last
        else:
            return right_last





#自己重寫, 刷題用這個, time complexity O(n^2) => while loop 重複遍歷tree
#思路: pre-order traversal, 若root.left不等於None, 先暫存root.right, 在把root.left調換至root.right(以root.right當作next指針), recursion root.right, 最後再接回temp
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
            self.dfs(root.right) #recursion 整理root.right 下面的分支, 使其都變成linked list
            while root.right: #跑到右邊最底端
                root = root.right
            root.right = temp #接回原右端
            self.dfs(root.right) #整理下面分支 
        else:
            self.dfs(root.right)





#重寫第二次 time complexity O(n^2), space complexity O(h)
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
        
    def dfs(self, node):
        if not node:
            return
        if node.left:
            right = node.right
            node.right = node.left
            node.left = None
            self.dfs(node.right)
            while node.right:
                node = node.right
            node.right = right
            self.dfs(node.right)
        else:
            self.dfs(node.right)


# 重寫第三次, time complexity O(n), space complexity O(h)
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
        
    def dfs(self, node):
        if not node:
            return
        if node.left:
            temp = node.right
            node.right = node.left
            node.left = None
            self.dfs(node.right)
            while node.right:
                node = node.right
            node.right = temp
            self.dfs(node.right)
        else:
            self.dfs(node.right)


