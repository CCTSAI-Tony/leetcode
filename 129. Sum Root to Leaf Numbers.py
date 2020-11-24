'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#自己重寫 dfs, time complexity O(n)
#思路: base case 是當node 沒有child 的時候 return
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.dfs(root, 0)
        return self.res
    
    
    def dfs(self, node, num):
        new_num = num*10 + node.val
        if not node.left and not node.right:
            self.res += new_num
        if node.left:
            self.dfs(node.left, new_num)
        if node.right:
            self.dfs(node.right, new_num)

#自己重寫  time complexity O(n)         
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        self.dfs(root, "", res)
        return sum(res)
    
    
    def dfs(self, node, path, res):
        if not node.left and not node.right:
            res.append(int(path + str(node.val)))
        if node.left:
            self.dfs(node.left, path + str(node.val), res)
        if node.right:
            self.dfs(node.right, path + str(node.val), res)


#自己重寫第二次, time complexity O(n), space complexity O(h)
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.dfs(root, 0)
        return self.res
    
    def dfs(self, node, path):
        if not node.left and not node.right:
            temp = path*10 + node.val
            self.res += temp
        if node.left:
            self.dfs(node.left, path*10+node.val)
        if node.right:
            self.dfs(node.right, path*10+node.val)






# dfs + stack top-down
class Solution:
    def sumNumbers1(self, root):
        if not root:
            return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += value #回報給res
                if node.right:
                    stack.append((node.right, value*10+node.right.val))
                if node.left:
                    stack.append((node.left, value*10+node.left.val))
        return res


# recursively 
class Solution:
    def sumNumbers(self, root):
        self.res = 0 #全域變數
        self.dfs(root, 0)
        return self.res
    
    def dfs(self, root, value):
        if root:
            
            self.dfs(root.left, value*10+root.val)
            
            self.dfs(root.right, value*10+root.val)
            if not root.left and not root.right:
                self.res += value*10 + root.val
























