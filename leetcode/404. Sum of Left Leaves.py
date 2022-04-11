'''
Given the root of a binary tree, return the sum of all left leaves.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
'''

# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: bfs
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        cur_sum = 0
        queue = deque([(root, None)])
        while queue:
            for _ in range(len(queue)):
                node, part = queue.popleft()
                if not node.left and not node.right and part == "left":
                    cur_sum += node.val
                else:
                    if node.left:
                        queue.append((node.left, "left"))
                    if node.right:
                        queue.append((node.right, "right"))
        return cur_sum