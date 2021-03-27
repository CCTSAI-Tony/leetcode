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


#maybe to use a memory is better, as you don't need to calculate the depth of same node again, it is 84ms
#刷題用這個, time complexity O(n), space complexity O(n)
#思路: 利用depth 來計算subtree depth, 利用hash table 存node:depth, 這樣就不用重複dfs遍歷相同node,
#preorder 遍歷每個node 來check 是否符合balanced tree
class Solution(object):
    def __init__(self): #這個init不能打錯！
        self.d = {}
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: 
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def depth(self,root):
            if not root: 
              return 0
            if root in self.d: 
                return self.d[root]
            self.d[root] = 1 + max(self.depth(root.left), self.depth(root.right))
            return self.d[root]


#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def __init__(self):
        self.dic = {}
        
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def depth(self, node):
        if not node:
            return 0
        if node in self.dic:
            return self.dic[node]
        d = max(self.depth(node.left), self.depth(node.right)) + 1
        self.dic[node] = d
        return self.dic[node]

#刷題用這個
#重寫第三次, time complexity O(n), space complexity O(h)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        memo = dict()
        self.dfs(root, memo)
        if False in memo:
            return False
        return True
    
    def dfs(self, node, memo):
        left, right = 0, 0
        if node.left:
            left = self.dfs(node.left, memo)
        if node.right:
            right = self.dfs(node.right, memo)
        if abs(left - right) > 1:
            memo[False] = 1
        memo[True] = 1
        return max(left, right) + 1





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

'''
       1
      / \
     2   4     none balanced
    / \   \
   3   3   6
  /        /
 1        5
 










