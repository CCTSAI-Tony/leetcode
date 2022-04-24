'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Follow up: Can you solve it with time complexity O(height of tree)?

 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
'''

# 刷題用這個, time complexity O(n)
# 思路: 建立successor and predecessor, 再利用recursion 來delete node
class Solution:
    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val
        
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root) #不改變其結構, 只移轉delete node
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child    
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root

#重寫第二次, time complexity O(logn), space complexity O(h), h = logn for the balanced tree
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = self.succesoor(root)
                root.right = self.deleteNode(root.right, root.val)
            elif root.left:
                root.val = self.predeccessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root
        
    def succesoor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predeccessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

# 重寫第三次, time complexity O(logn), space complexity O(h), h = logn for the balanced tree
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def successor(node):
            if not node.right:
                return None
            node = node.right
            while node.left:
                node = node.left
            return node
        
        def predecessor(node):
            if not node.left:
                return None
            node = node.left
            while node.right:
                node = node.right
            return node
        
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            if root.left:
                predecessor = predecessor(root)
                root.val = predecessor.val
                root.left = self.deleteNode(root.left, root.val)
            elif root.right:
                successor = successor(root)
                root.val = successor.val
                root.right = self.deleteNode(root.right, root.val)
        return root

