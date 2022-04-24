'''
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. 
Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.  (The values of the nodes may still be duplicates.)

Left boundary is defined as the path from root to the left-most node. 
Right boundary is defined as the path from root to the right-most node. 
If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. 
Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. 
If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1

Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
 

Example 2

Input:
    ____1_____
   /          \
  2            3
 / \          / 
4   5        6   
   / \      / \
  7   8    9  10  
       
Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].
'''
#time complexity O(n)
#思路: anti-clockwise, 分解三個helper 來收集node, 依序為 leftbound, leaves, rightbound, 注意: helper之間 不能收集同樣的node
#例如leftmost node 只能由leaves helper 收集, 另外leftbound 是上往下收集, rightbount 是下往上收集, 考驗你的recursion 能力
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        if not root:
            return []
        self.boundary = [root.val]
        self.dfs_leftbound(root.left)
        self.dfs_leaves(root, root)
        self.dfs_rightbound(root.right)
        return self.boundary

    def dfs_leftbound(self, node):
        if not node or (not node.left and not node.right): #left most node 歸類到leaves 
            return
        self.boundary.append(node.val)  #左邊boundary 從上到下
        if node.left: #優先往左走, 若沒有左邊子樹只好往右走
            self.dfs_leftbound(node.left)
        else:
            self.dfs_leftbound(node.right)

    def dfs_leaves(self, node, root):
        if not node:
            return
        self.dfs_leaves(node.left, root)
        if node != root and not node.left and not node.right: # node != root  不要重複加到root
            self.boundary.append(node.val)
            return
        self.dfs_leaves(node.right, root)

    def dfs_rightbound(self, node):
        if not node or (not node.left and not node.right):
            return
        if node.right: #優先往右走, 若沒有右邊子樹只好往左走
            self.dfs_rightbound(node.right)
        else:
            self.dfs_rightbound(node.left)
        self.boundary.append(node.val) #右邊boundary 從下到上



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#自己重寫, time complexity O(n)
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.boundary = [root.val]
        self.left_bound(root.left)
        self.leaves(root, root)
        self.right_bound(root.right)
        return self.boundary
        
    def left_bound(self, node):
        if not node or (not node.left and not node.right):
            return
        self.boundary.append(node.val)
        if node.left:
            self.left_bound(node.left)
        else:
            self.left_bound(node.right)
    
    def leaves(self, node, root):
        if not node:
            return
        self.leaves(node.left, root)
        if node != root and not node.left and not node.right:
            self.boundary.append(node.val)
            return
        self.leaves(node.right, root)
        
    
    def right_bound(self, node):
        if not node or (not node.left and not node.right):
            return
        if node.right:
            self.right_bound(node.right)
        else:
            self.right_bound(node.left)
        self.boundary.append(node.val)


#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        boundary = [root.val]
        self.left_boundary(root.left, boundary)
        self.collect_leaves(root, root, boundary)
        self.right_boundary(root.right, boundary)
        return boundary
    
    def left_boundary(self, node, boundary):
        if not node or (not node.left and not node.right):
            return
        boundary.append(node.val)
        self.left_boundary(node.left, boundary)
        if not node.left:
            self.left_boundary(node.right, boundary)
    
    def collect_leaves(self, node, root, boundary):
        if not node:
            return
        if node != root and (not node.left and not node.right):
            boundary.append(node.val)
        self.collect_leaves(node.left, root, boundary)
        self.collect_leaves(node.right, root, boundary)
        
    def right_boundary(self, node, boundary):
        if not node or (not node.left and not node.right):
            return
        self.right_boundary(node.right, boundary)
        if not node.right:
            self.right_boundary(node.left, boundary)
        boundary.append(node.val)


# 重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        if not root.left and not root.right:
            return [root.val]
        res = [root.val]
        self.left_bound(root.left, res)
        self.leaves_bound(root, res)
        self.right_bound(root.right, res)
        return res
        
    def left_bound(self, node, res):
        if not node or (not node.left and not node.right):
            return
        res.append(node.val)
        if node.left:
            self.left_bound(node.left, res)
        else:
            self.left_bound(node.right, res)
            
    def leaves_bound(self, node, res):
        if not node.left and not node.right:
            res.append(node.val)
            return
        if node.left:
            self.leaves_bound(node.left, res)
        if node.right:
            self.leaves_bound(node.right, res)
            
    def right_bound(self, node, res):
        if not node or (not node.left and not node.right):
            return
        if node.right:
            self.right_bound(node.right, res)
        else:
            self.right_bound(node.left, res)
        res.append(node.val)



# 重寫第三次, time complexity O(n), space complexity O(h)
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = [root.val]
        def traverse_left(node):
            if not node:
                return
            if not node.left and not node.right:
                return
            res.append(node.val)
            if node.left:
                traverse_left(node.left)
            else:
                traverse_left(node.right)
        def traverse_leaf(node):
            if not node.left and not node.right and node != root:
                res.append(node.val)
                return
            if node.left:
                traverse_leaf(node.left)
            if node.right:
                traverse_leaf(node.right)
        def traverse_right(node):
            if not node:
                return
            if not node.left and not node.right:
                return
            if node.right:
                traverse_right(node.right)
            else:
                traverse_right(node.left)
            res.append(node.val)
            
        traverse_left(root.left)
        traverse_leaf(root)
        traverse_right(root.right)
        return res







