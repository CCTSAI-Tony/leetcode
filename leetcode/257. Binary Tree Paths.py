# Given a binary tree, return all root-to-leaf paths.

# Note: A leaf is a node with no children.

# Example:

# Input:

#    1
#  /   \
# 2     3
#  \
#   5

# Output: ["1->2->5", "1->3"]

# Explanation: All root-to-leaf paths are: 1->2->5, 1->

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#自己想的, dfs, time complexity O(n)
#思路: 此題要注意的就是path 字與字之間要 "->", 還有此題的root to leaf 定義要看清楚
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return None
        res = []
        self.dfs(root, [], res)
        return res
    
    
    def dfs(self, node, path, res):
        if not node.left and not node.right:
            path.append(node.val)
            ans = "->".join(map(str, path)) #join 是迭代器, map 是生成器
            res.append(ans)  
            return
        if node.left:
            self.dfs(node.left, path+[node.val], res)
        if node.right:
            self.dfs(node.right, path+[node.val], res)

# 刷題用這個, backtracking
# 重寫第二次, time complexity O(n), space complexity O(h)
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        path = [str(root.val)]
        self.dfs(root, path, res)
        return res
    
    def dfs(self, node, path, res):
        if not node.left and not node.right:
            res.append("->".join(path))
            return
        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, res)
            path.pop()
        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, res)
            path.pop()

# dfs + stack
class Solution:
    def binaryTreePaths1(self, root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop() #pop() dfs
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, ls+str(node.val)+"->"))
        return res

# bfs + queue
import collections
class Solution:
    def binaryTreePaths2(self, root):
        if not root:
            return []
        res, queue = [], collections.deque([(root, "")])
        while queue:
            node, ls = queue.popleft()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.left:
                queue.append((node.left, ls+str(node.val)+"->"))
            if node.right:
                queue.append((node.right, ls+str(node.val)+"->"))
        return res


# dfs recursively
class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res


    def dfs(self, root, ls, res):
        if not root.left and not root.right:
            res.append(ls+str(root.val))
        if root.left:
            self.dfs(root.left, ls+str(root.val)+"->", res)
        if root.right:
            self.dfs(root.right, ls+str(root.val)+"->", res)



















