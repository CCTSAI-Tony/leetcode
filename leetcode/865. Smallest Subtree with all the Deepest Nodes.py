'''
Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is tree consisting of that node, plus the set of all descendants of that node.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
Example 2:

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.
Example 3:

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
 

Constraints:

The number of nodes in the tree will be between in the range [1, 500].
The values of the nodes in the tree are unique.
'''

#刷題用這個, time complexity O(n), space complexity O(h)
#思路: 分治法, dfs 左右子樹, 若左子樹的depth > 右子樹的depth => node.left 有可能為smallest subtree with all the deepest nodes' root => return left, leftDepth
#這裡的left 不是指node.left, 而是左分支 smallest subtree with all the deepest nodes' root
#若左子樹的depth > 右子樹的depth => return node, leftDepth => 此時node已成為該分支的 smallest subtree with all the deepest nodes' root
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.deepestDepth(root, 0)[0]


    def deepestDepth(self, node, depth):
        if not node.left and not node.right:
            return node, depth

        leftDepth, rightDepth = 0, 0
        if node.left:
            left, leftDepth = self.deepestDepth(node.left, depth + 1)
        if node.right:
            right, rightDepth = self.deepestDepth(node.right, depth + 1)    

        # If the deepest node on the left subtree is deeper than the deepest node 
        # on the right subtree return the left subtree and the left deepest depth 
        if leftDepth > rightDepth:
            return left, leftDepth
        
        # If the deepest node on the right subtree is deeper than the deepest node 
        # on the left subtree return the right subtree and the right deepest depth 
        if rightDepth > leftDepth:
            return right, rightDepth
        
        
        # If the above two conditions isn't met, then leftDepth == rightDepth
        # leftDepth equal rightDepth means that the deepest node
        # in the left subtree has the same depth as the deepest node 
        # in the right subtree, as such, we should return the current node 
        # as it is the root of the current subtree that contains the deepest 
        # nodes on the left and right subtree.
        # return statment can also be `return node, rightDepth`
        return node, leftDepth


#自己重寫, time complexity O(n), space complexity O(h)
#思路: 分治法, dfs 左右子樹, 若左子樹的depth > 右子樹的depth => node.left 有可能為smallest subtree with all the deepest nodes' root => return left, leftDepth
#這裡的left 不是指node.left, 而是左分支 smallest subtree with all the deepest nodes' root
#若左子樹的depth > 右子樹的depth => return node, leftDepth => 此時node已成為該分支的 smallest subtree with all the deepest nodes' root
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.dfs(root, 0)[0]
    
    def dfs(self, node, depth):
        if not node.left and not node.right:
            return (node, depth)
        left_depth, right_depth = 0, 0
        if node.left:
            left, left_depth = self.dfs(node.left, depth + 1)
        if node.right:
            right, right_depth = self.dfs(node.right, depth + 1)
        if left_depth > right_depth:
            return (left, left_depth)
        if right_depth > left_depth:
            return (right, right_depth)
        if left_depth == right_depth:
            return (node, left_depth)













