'''
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, 
and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, 
then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.

'''


#自己想的, time complexity O(n), space complexity O(n)
#思路: 重建 binary search tree 就要用到 lower, upper 技巧, 搭配deque 從左pop到右
from collections import deque
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        preorder = deque(preorder)
        return self.dfs(preorder, float("inf"), float("-inf"))
    
    def dfs(self, preorder, upper, lower):
        if not preorder:
            return
        if not lower < preorder[0] < upper:
            return
        num = preorder.popleft()
        node = TreeNode(num)
        node.left = self.dfs(preorder, num, lower)
        node.right = self.dfs(preorder, upper, num)
        return node


#iterative solution, use stack
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value: #這句重要, 回朔到該右支樹的parent node
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        return root

