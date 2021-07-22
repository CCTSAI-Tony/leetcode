'''
Given a node in a binary search tree, return the in-order successor of that node in the BST. If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
 

Example 1:


Input: tree = [2,1,3], node = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both the node and the return value is of Node type.
Example 2:


Input: tree = [5,3,6,2,4,null,null,1], node = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
Example 3:


Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 15
Output: 17
Example 4:


Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 13
Output: 15
Example 5:

Input: tree = [0], node = 0
Output: null
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
All Nodes will have unique values.
 

Follow up: Could you solve it without looking up any of the node's values?
'''

#自己想的, time complexity O(n), space complexity O(h)
#思路: 分治法, 利用preorser 順序 來找出下一個點, 從parent.left == node 知道下一點有可能是parent
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        right, top = None, None
        if node.right:
            right = self.get_right(node.right)
        elif node.parent:
            top = self.get_top(node)
        
        if right:
            return right
        elif top:
            return top
        else:
            return None
        
    def get_right(self, node):
        if not node.left:
            return node
        return self.get_right(node.left)
    
    def get_top(self, node):
        parent = node.parent
        if not parent:
            return None
        elif parent.left == node:
            return parent
        elif parent.right == node:
            return self.get_top(parent)


#別人的解法, 刷題用這個
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            node = node.right
            while node.left: 
                node = node.left
            return node

        while node.parent: 
            if node.parent.left == node:
                return node.parent
            node = node.parent
        return None




