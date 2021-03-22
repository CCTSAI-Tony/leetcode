'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

'''

#自己重寫第二次, time complexity O(n), space complexity O(n)
#思路: bfs
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        flag = 0
        res = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not flag:
                res.append(level)
            else:
                res.append(level[::-1])
            flag = -flag + 1
        return res


# time complexity O(n), bfs iterative
# 思路: Simple straightforward solution using flag to decide whether from left to right or from right to left
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: 
            return []
        res, queue, flag = [], deque([root]), 1
        while queue:
            cur_level=[] #當層node
            for i in range(len(queue)):
                node = queue.popleft()
                cur_level += [node.val]
                if node.left: 
                    queue += [node.left]
                if node.right: 
                    queue += [node.right]
            res += [cur_level[::flag]] #這裡cur_level 要list化 以利區隔 若用 res.append(cur_level[::flag]) 就不用
            flag *= -1 #順序切換
        return res

'''
queue = [2,3,4,5,6,7]
print(queue[::1])  step size 預設就是1 [::]
print(queue[::-1])

[2, 3, 4, 5, 6, 7]
[7, 6, 5, 4, 3, 2]
'''
