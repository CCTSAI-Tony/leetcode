'''
Given the root of a binary tree, return the maximum average value of a subtree of that tree. 
Answers within 10-5 of the actual answer will be accepted.

A subtree of a tree is any node of that tree plus all its descendants.

The average value of a tree is the sum of its values, divided by the number of nodes.

 

Example 1:


Input: root = [5,6,1]
Output: 6.00000
Explanation: 
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.
Example 2:

Input: root = [0,null,1]
Output: 1.00000
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 105
'''

# 刷題用這個, time complexity O(n), space complexity O(h)
# 思路: 分治法
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.max_average = 0
        self.dfs(root)
        return self.max_average
    
    def dfs(self, node):
        if not node:
            return (0, 0)
        l_value, l_count = self.dfs(node.left)
        r_value, r_count = self.dfs(node.right)
        c_value = (l_value*l_count + r_value*r_count + node.val)/(l_count+r_count+1)
        self.max_average = max(self.max_average, c_value)
        return c_value, l_count + r_count + 1


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.res = 0

        def dfs(root: TreeNode) -> (int, int):
            if not root: 
                return (0, 0)
            (lv, lc), (rv, rc) = dfs(root.left), dfs(root.right)
            cval, ccnt = root.val + lv + rv, 1 + lc + rc
            self.res = max(self.res, cval / ccnt)
            return (cval, ccnt)

        dfs(root)
        return self.res





