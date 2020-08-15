'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#自己想的 recursive, time complexity O(n), 似分治法
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        res = []
        self.dfs(root, res)
        return res
        
    def dfs(self, node, res):
        if not node:
            return
        self.dfs(node.left, res)
        self.dfs(node.right, res)
        res.append(node.val)

#自己重寫, iterative, time complexity O(n)
#思路: postorder traversal, 利用visited來紀錄是否該chile nodes已經遍歷過了, 輪到root turn
#新 pop node visited => False => True 重新放入queue來實現 post order traversal
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        res = []
        queue = [(root, False)]
        while queue:
            node, visited = queue.pop()
            if not node:
                continue
            if visited:
                res.append(node.val)
            else:
                queue.append((node, True))
                queue.append((node.right, False))
                queue.append((node.left, False))
        return res


class Solution:
    def postorderTraversal(self, root):
        traversal, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    traversal.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return traversal


#summary Python iterative method for post/in/preorder traversal  以後照這樣解

I add isinstance method to judge what type the value popup from stack. By adding the judge, we can easily simulate system stack and get right order. Hope it is helpful

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]: #subtree.left>root>subtree.right
        stack = [root]
        res = []
        while stack:
            temp = stack.pop()
            if temp:
                if isinstance(temp, TreeNode):
                    stack.append(temp.right)
                    stack.append(temp.val)
                    stack.append(temp.left)
                else:
                    res.append(temp)
        return res

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]: #subtree.left>subtree.right>root
        stack = [root]
        res = []
        while stack:
            temp = stack.pop()
            if temp:
                if isinstance(temp, TreeNode):
                    stack.append(temp.val)
                    stack.append(temp.right)
                    stack.append(temp.left)
                else:
                    res.append(temp)
        return res

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]: #root>subtree.left>subtree.right
        stack = [root]
        res = []
        while stack:
            temp = stack.pop()
            if temp:
                if isinstance(temp, TreeNode):
                    stack.append(temp.right)
                    stack.append(temp.left)
                    stack.append(temp.val)
                else:
                    res.append(temp)
        return res

'''
The isinstance() function returns True if the specified object is of the specified type, otherwise False.

If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.

x = isinstance("Hello", (float, int, str, list, dict, tuple))

True


class myObj:
  name = "John"

y = myObj()

x = isinstance(y, myObj)

True
'''

































