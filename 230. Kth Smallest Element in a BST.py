'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#自己重寫 O(n), 刷題用這個, recursive
#思路: binary search tree 就要想到in order traversal, 使用全域變數來確認目前node是第幾小
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.level = 0
        self.ans = 0
        self.dfs(root, k)
        return self.ans
        
        
    def dfs(self, root, k):
        if not root:
            return
        self.dfs(root.left, k)
        self.level += 1
        if self.level == k:
            self.ans = root.val
            return   #提早結束
        self.dfs(root.right, k)

#自己重寫 in order traversal, iterative, 要多練習
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        level = 0
        while stack or root:
            while root:
                stack.append(root)
                root = root.left  
            root = stack.pop()  #root 切換成左分支最底層的node
            level += 1
            if level == k:
                return root.val
            root = root.right

# Recursive:
class Solution:
    def kthSmallest(self, root, k):
        self.k = k #class variable
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        self.helper(node.left) #go all the way down to the bottom node.left
        self.k -= 1 #trace back to the root, 回到上一層代表地位增加 k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)

# Iterative: plz know how the binary search tree works
class Solution:
    def kthSmallest(root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left #go all the way down to the bottom node.left the smallest
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right #go the node.right to find out the bigger one

















