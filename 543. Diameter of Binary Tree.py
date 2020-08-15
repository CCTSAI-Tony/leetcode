'''
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''

Simple Python

Just go through the tree. recursive, time complexity O(n)

Analysis:
Time complexity O(N)
Space complexity O(1)

# time complexity O(n)
# 思路: 分治法
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0  #全域變數
        self.depth(root)  #雖然他雖然有值, 因為有return 但我們一點也不關心
        return self.ans
        
    def depth(self, p):
        if not p: 
            return 0
        left, right = self.depth(p.left), self.depth(p.right)
        self.ans = max(self.ans, left + right)  #把自己當root 計算左+右 path
        return max(left, right) + 1 #回報上給一層多一個edge, 此時最長path 則是加上左或右比較多的一方
            
        














