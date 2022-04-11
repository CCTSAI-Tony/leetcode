'''
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 刷題用這個m bfs, time complexity O(n), space complexity O(n)
from collections import deque
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        queue = deque([root])
        res = []
        while queue:
            max_value = float("-inf")
            for _ in range(len(queue)):
                node = queue.popleft()
                max_value = max(max_value, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(max_value)
        return res



#刷題用這個
#重寫第二次, time complexity O(n), space complexity O(n)
from collections import defaultdict
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        levels = defaultdict(int)
        self.dfs(root, 0, levels)
        return levels.values()
        
    def dfs(self, node, level, levels):
        if level not in levels or node.val > levels[level]:
            levels[level] = node.val
        if node.left:
            self.dfs(node.left, level+1, levels)
        if node.right:
            self.dfs(node.right, level+1, levels)




#自己想的, time complexity O(hlogh, n), 因為有sort
#思路: 利用defaultdict(list), 與dfs遍歷 來紀錄不同level的值, 
from collections import defaultdict
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        levels = defaultdict(list)
        self.dfs(root, 0, levels)
        return [max(v) for i, v in sorted(levels.items(), key=lambda item: item[0])] #若root 是None, levels 是empty, return []
        
        
    def dfs(self, root, level, levels):
        if not root:
            return 
        levels[level].append(root.val)
        self.dfs(root.left, level+1, levels)
        self.dfs(root.right, level+1, levels)


# [i for i in []]
# []

#自己想的, bfs
from collections import defaultdict,deque
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        levels = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if not node:
                continue
            levels[level].append(node.val)
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
        return [max(v) for i, v in sorted(levels.items(), key=lambda item: item[0])]






