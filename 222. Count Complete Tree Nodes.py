'''
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''
# binary tree types
# https://cs.stackexchange.com/questions/32397/is-there-a-difference-between-perfect-full-and-complete-tree

# time complexity O(lgn * lgn) recursion
# 思路: 利用get depth 來找出左右 subtree depth, 來判斷左右子樹誰是complete binary tree, 再進行進算, get dpeth要不斷往左子樹探詢, 因為最先被填滿
class Solution:
        # @param {TreeNode} root
        # @return {integer}
        def countNodes(self, root):
            if not root:
                return 0
            leftDepth = self.getDepth(root.left) #左邊子樹深度
            rightDepth = self.getDepth(root.right)#右邊子樹身度
            if leftDepth == rightDepth:
                return pow(2, leftDepth) + self.countNodes(root.right) #2的leftDepth 次方
            else:
                return pow(2, rightDepth) + self.countNodes(root.left)
    
        def getDepth(self, root): #求深度, 因為是complete binary tree, 最底層左邊先填滿,所以一律求左
            if not root:
                return 0
            return 1 + self.getDepth(root.left)

# compare the depth between left sub tree and right sub tree.
# A, If it is equal, it means the left sub tree is a full binary tree
# B, It it is not , it means the right sub tree is a full binary tree

# Nice solution, add a word, comparing the depth between left sub tree and right sub tree, 
# If it is equal, it means the left sub tree is a perfect binary tree, not only a full binary tree. 
# If it is not , it means the right sub tree is a perfect binary tree.