'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---   see from the ditrction
 /   \
2     3         <---
 \     \
  5     4       <---

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# DFS recursively, time complexity O(n), 刷題用這個
# 思路: 增加level 參數, 使得可以針對每層的nodes看要回報第一個(right side view)還是最後一個(left side view)
class Solution:
    def rightSideView(self, root):
        res = []
        self.dfs(root, 0, res)
        return [x[0] for x in res] #just return the first element of each level, because right first to dfs
    
    def dfs(self, root, level, res):
        if root:
            if len(res) < level+1: #level+1 zero based index issue
                res.append([]) #append blank bracket for each level
            res[level].append(root.val) 
            self.dfs(root.right, level+1, res) #right first 
            self.dfs(root.left, level+1, res)

# DFS + stack
class Solution:
    def rightSideView2(self, root):
        res, stack = [], [(root, 0)]
        while stack:
            curr, level = stack.pop() #pop out the last element
            if curr:
                if len(res) < level+1:
                    res.append([])
                res[level].append(curr.val)
                stack.append((curr.right, level+1))
                stack.append((curr.left, level+1))
        return [x[-1] for x in res] #why here is return x[-1], cause stack append right fist, but pop out right after left

#也可以優先pop() right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root,0)]
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(node.val)
                stack.append((node.left, level+1))
                stack.append((node.right, level+1))
        return [x[0] for x in res]




# BFS + queue
class Solution:
    def rightSideView(self, root):
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)#pop out the first element
            if curr:
                if len(res) < level+1:
                    res.append([])
                res[level].append(curr.val)
                queue.append((curr.left, level+1))
                queue.append((curr.right, level+1))
        return [x[-1] for x in res]


#The solution above is level order traversal indeed,

'''
res = []
res.append([])
res
[[]]
res.append([])
res
[[], []]
res[0].append(1)
res
[[1], []]




















































