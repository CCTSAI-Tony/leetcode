'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. 
A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
 

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''

# First, travel down the bigger tree via standard dfs, if we find node equal to the value of root of the smaller tree, compare the subtrees.

# We travel down both subtrees at the same time and if and only if every node is the same then we know we have found the right subtree.

#time complexity O(s*t)
#思路: 利用dfs 分治法 來解題, 往左右child 找可能的子樹
class Solution(object):
    def isSubtree(self, s, t):
        if not t:  #empty tree is also a subtree of s
            return True
        return self.dfs(s, t)


    def dfs(self, s, t):
            if not s:  #s 已經沒有subtree
                return False
            
            if s.val == t.val and self.checkTree(s, t):
                return True
            
            return self.dfs(s.left, t) or self.dfs(s.right, t)  #往左右child 找可能的子樹

    def checkTree(self, root1, root2):
            if not root1 and not root2:
                return True
            elif root1 and not root2 or root2 and not root1:
                return False
            
            if root1.val != root2.val:
                return False
            
            return self.checkTree(root1.left, root2.left) and self.checkTree(root1.right, root2.right)  #查看child nodes 是否一樣


        
        

#  Given two non-empty binary trees s and t































