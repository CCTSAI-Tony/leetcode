'''
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. 
If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

 

Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
All Nodes will have unique values.
'''

#刷題用這個, time complexity O(n), space complexity O(1)
class Solution:
    
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        successor = None
        
        while root:
            
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
                
        return successor


#典型inorder 算法, time complexity O(n), space complexity O(n)
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root)
            root = root.right
        for i in range(len(res)):
            if i != 0 and res[i-1] == p:
                return res[i]
        return None


#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor
