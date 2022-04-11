'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#刷題用這個, time complexity O(n), space complexity O(h)
#思路: backtracking
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        self.dfs(root, [], 0, sum)
        return self.res
    
    def dfs(self, node, path, curSum, sum):
        curSum += node.val
        path.append(node.val)
        if not node.left and not node.right and curSum == sum:
            self.res.append(path[:])
        else:
            if node.left:
                self.dfs(node.left, path, curSum, sum)
            if node.right:
                self.dfs(node.right, path, curSum, sum)
        path.pop()


# 重寫第二次, time complexity O(n), space complexity O(h)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        path = []
        def dfs(node, prev_sum):
            nonlocal res
            nonlocal path
            path.append(node.val)
            cur_sum = prev_sum + node.val
            if not node.left and not node.right and cur_sum == targetSum:
                res.append(path[:])
            if node.left:
                dfs(node.left, cur_sum)
            if node.right:
                dfs(node.right, cur_sum)
            path.pop()
        
        dfs(root, 0)
        return res



class Solution:
    def pathSum(self, root, sum):
        if not root:
            return [] 
        res = []
        self.dfs(root, sum, [], res)
        return res
    
    def dfs(self, root, sum, ls, res):
        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            res.append(ls)
        if root.left:
            self.dfs(root.left, sum-root.val, ls+[root.val], res)
        if root.right:
            self.dfs(root.right, sum-root.val, ls+[root.val], res)


#  自己重寫, time complexity O(n), space complexity O(n^2)
#  思路: 典型dfs, 要注意的是往下dfs 不能直接在code修改mutable參數, 會影響原始變數, 而是在傳參的時候修改==建立一個新list
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return None
        ans = []
        self.dfs(root, [root.val], ans, root.val, sum)
        return ans
    
    
    def dfs(self, node, path, ans, val, target):
        if not node.left and not node.right:
            if val == target:
                ans.append(path)
            return
        if node.left:       
            self.dfs(node.left, path + [node.left.val], ans, val + node.left.val, target)
        if node.right:
            self.dfs(node.right, path + [node.right.val], ans, val + node.right.val, target)

a = [1,2,3]
b = a + [5] #  建立一個新list
b
[1, 2, 3, 5]
b[0] = 100
b
[100, 2, 3, 5]
a
[1, 2, 3]
c = a  #  reference to a
c[0] = 50
a
[50, 2, 3]
c
[50, 2, 3]



# DFS + stack   
class Solution:
    def pathSum5(self, root, sum): 
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            curr, ls = stack.pop()
            if not curr.left and not curr.right and sum(ls) == s:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, ls+[curr.left.val]))
        return res
'''
a = [1,2,3,4,5]
b = sum(a)
b
15

'''




