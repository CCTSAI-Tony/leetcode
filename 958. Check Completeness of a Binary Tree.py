'''
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:



Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:



Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 
Note:

The tree will have between 1 and 100 nodes.
'''

DFS. Time complexity: O(n), space complexity: O(h).

#刷題用這個 time complexity O(n), space complexity O(h)
#思路: 計算tree 的總nodes, 並尋找最深層right_most的編號, 若總nodes = 最深層right_most的編號, 就是complete binary tree, 代表中間都被填滿了
#技巧: 如何對每個node的位置上編號 root: 1, root.left = 2*1, root.right = 2*1+1 ... node: k, node.left: 2*k, node.right: 2*k + 1 以此列推
#額外技巧: 如何對同一個layer的node 上index ex: 0, 1, 2, 3...=> root: 0, root.left = 2*1, root.right = 2*1+1 ... node: k, node.left: 2*k, node.right: 2*k + 1 以此列推
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # number of nodes, right_most_coords
        
        if not root:
            return True
        tot, right_most = self.dfs(root, 1)
        return tot == right_most

    def dfs(self, root, coord):
        if not root:
            return 0, 0
        l = self.dfs(root.left, 2*coord)
        r = self.dfs(root.right, 2*coord+1)
        tot = l[0]+r[0]+1
        right_most = max(coord, l[1], r[1])
        return tot, right_most


#自己重寫, time complexity O(n), space complexity O(h)
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        tot, right_most = self.dfs(root, 1)
        return tot == right_most
    
    
    def dfs(self, node, pos):
        if not node:
            return (0, 0)
        l, l_r = self.dfs(node.left, 2*pos)
        r, r_r = self.dfs(node.right, 2*pos+1)
        tot = l + r + 1
        right_most = max(pos, l_r, r_r)
        return (tot, right_most)



BFS. Time complexity: O(n), space complexity: O(n).

import collections
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        q = collections.deque([(root, 1)])
        res = []
        while q:
            u, coord = q.popleft()
            res.append(coord)
            if u.left:
                q.append((u.left, 2*coord))
            if u.right:
                q.append((u.right, 2*coord+1))
        return len(res) == res[-1]




