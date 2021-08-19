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


# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: bfs
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            layer = []
            for _ in range(len(queue)):
                node = queue.popleft()
                layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(layer[-1])
        return res




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


#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        dic = {}
        self.dfs(root, 0, dic)
        return dic.values()
    
    def dfs(self, node, level, dic):
        if not node:
            return
        dic[level] = node.val
        self.dfs(node.left, level + 1, dic)
        self.dfs(node.right, level + 1, dic)



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




















































