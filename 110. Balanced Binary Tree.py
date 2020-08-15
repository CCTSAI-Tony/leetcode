'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

'''

# Definition for a binary tree node.     
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if not root:
            return  True                                               #左右子樹也要遞迴 防止左右子樹不為balaced
        return abs(self.dfs(root.left) - self.dfs(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
        
    def dfs(self, root):
        if not root:
            return 0
        return 1 + max(self.dfs(root.left), self.dfs(root.right)) #記得當層加一

#maybe to use a memory is better, as you don't need to calculate the depth of same node again, it is 84ms
class Solution(object):
    def __init__(self): #這個init不能打錯！
        self.d = {}
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: 
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def depth(self,root):
            if not root: return 0
            if root in self.d: 
                return self.d[root]
            self.d[root] = 1 + max(self.depth(root.left), self.depth(root.right))
            return self.d[root]

'''
       1
      / \
     2   4     none balanced
    / \   \
   3   3   6
  /        /
 1        5
 










