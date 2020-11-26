'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#dfs
class Solution(object):
	def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder: 
            ind = inorder.index(postorder.pop()) 
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind+1:], postorder)
            root.left = self.buildTree(inorder[0:ind], postorder) 
            return root

'''

               1
             /    \
            2      3
          /  \\      \
         4    5       6
                    /   \
                   7     8
                    \
                     9

post(l,r,root) 45297863 (1)
in(l,root,r)  425 (1) 37968

'''