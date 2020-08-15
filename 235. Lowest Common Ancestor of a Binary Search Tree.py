'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#自己想的 time complexity O(n), 解法跟236 一樣
#思路: 利用分治法, 若左邊有p or q and 右邊有p or q 則當前node就是LCA, 若只有一邊有, 則會報那一邊的答案
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None  #return False也可, 但依據題目, return None 比較符合題意
        return self.dfs(root, p, q)
    
    def dfs(self, node, p, q):
        if not node:
            return None
        if node == p or node == q:
            return node
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)
        if left and right:
            return node
        else:
            return left or right



# 235. Lowest Common Ancestor of a Binary Search Tree
# > 类型：DFS分治
# > Time Complexity O(h)
# > Space Complexity O(1)
# 根据BST的特性，如果p和q里面最大的值都比root.val小的话，那证明p和q都在左边，所以往左边递归就行，右边递归道理相同。然后第三种case当root.val等于p和q之间一个的时候，直接返回root即可，因为找到了
# 思路: 依據bst特性 若max(p,q) < root.val 往左邊, min(p,q) > root.val 往右邊, 若root.val 等於p,q 之間(included)則回報root
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root: 
            return None #according to the statement, this line is redundant
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root   #沒有全部在左邊, 沒有全部在右邊, 代表不是一左一右, 就是鑲嵌狀況




















