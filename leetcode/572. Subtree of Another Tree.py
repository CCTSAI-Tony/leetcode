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


#重寫第二次, time complexity O(s*t), space complexity O(1)
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        return self.dfs(s, t)
    
    def dfs(self, s, t):
        if not s:
            return False
        if s.val == t.val:
            if self.check(s, t):
                return True
        return self.dfs(s.left, t) or self.dfs(s.right, t)
    
    def check(self, s, t):
        if not s and not t:
            return True
        if (not s and t) or (not t and s) or s.val != t.val:
            return False
        return self.check(s.left, t.left) and self.check(s.right, t.right)

#重寫第二次, time complexity O(t*s), space complexity O(max(t, s.h))
from collections import deque
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not subRoot:
            return True
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
                if self.check(node, subRoot):
                    return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
        
    def check(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2 or node1.val != node2.val:
            return False
        return self.check(node1.left, node2.left) and self.check(node1.right, node2.right)


# 重寫第三次, time complexity O(r*s), space complexity O(logr + logs)
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        return self.dfs(root, subRoot)
    
    def dfs(self, node, subRoot):
        if not self.checkIsSame(node, subRoot):
            left, right = False, False
            if node.left:
                left = self.dfs(node.left, subRoot)
            if node.right:
                right = self.dfs(node.right, subRoot)
            return left or right
        return True
    
    def checkIsSame(self, node1, node2):
        if not node1 and not node2:
            return True
        if None in [node1, node2]:
            return False
        if node1.val != node2.val:
            return False
        left = self.checkIsSame(node1.left, node2.left)
        right = self.checkIsSame(node1.right, node2.right)
        return left and right























