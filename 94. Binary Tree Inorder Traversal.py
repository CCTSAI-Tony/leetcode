# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?


中序遍歷(In-Order Traversal)
指先存取左（右）子樹，然後存取根，最後存取右（左）子樹的遍歷方式
'''


# recursively

class Solution:
    def inorderTraversal1(self, root):
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

# iteratively
class Solution:
    def inorderTraversal(self, root):
        res, stack = [], []
        while True: # 持續迴圈
            while root:
                stack.append(root) 
                root = root.left 
            if not stack:
                return res
            node = stack.pop() 
            res.append(node.val)
            root = node.right #根節點右邊

'''
                         G
                      /     \
                    D         M
                   /  \\     / \
                  A    F    H   Z
                      /
                     E
  
l  根结点G入栈，若入栈的结点存在左子树，则依次入栈G/D/A，直至A发现其左子树为空，停止入栈，此时栈stack = [G,D,A]。

l  A出栈，并对A进行遍历，发现A没有右子树，根据中序遍历，需要遍历A的根节点D，D出栈，D存在右孩子，将其右孩子F入栈，F有左子树E，E入栈，此时stack = [G,F,E]，res=[A,D]

l  E出栈，并对E进行遍历，发现没有右子树，根据中序遍历，需要遍历E的根结点F，F出栈，此时栈为stack = [G],res = [A,D, E, F]

l  G出栈，并遍历G，G有右子树，将右子树M入栈，此时栈为stack = [M],res = [A,D, E, F,G]

l  右子树根结点M，按照中序遍历规则重复以上步骤：

         M存在左子树H入栈，stack = [M,H],res= [A,D, E, F,G]

         H出栈，遍历H，发现H没有右子树，根据中序遍历，需要遍历H的根结点M，M有右子树Z，Z入栈，此时stack = [Z],res = [A,D, E, F,G,H,M]

         Z出栈，遍历Z，发现Z没有右子树，此时stack= [],res = [A,D, E, F,G,H,M,Z]



'''




















'''