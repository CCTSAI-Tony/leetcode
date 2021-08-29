'''
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. 
For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, 
and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

 

Example 1:



Input: root = [4,2,5,1,3]


Output: [1,2,3,4,5]

Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

Example 2:

Input: root = [2,1,3]
Output: [1,2,3]
Example 3:

Input: root = []
Output: []
Explanation: Input is an empty tree. Output is also an empty Linked List.
Example 4:

Input: root = [1]
Output: [1]
 

Constraints:

-1000 <= Node.val <= 1000
Node.left.val < Node.val < Node.right.val
All values of Node.val are unique.
0 <= Number of Nodes <= 2000
'''

#刷題用這個!!
#iterative time complexity O(n)
#思路: 看到bst 就要想到 inorder traversal, 利用stack 搭配inorder traversal, 這個inorder 模板 有在刷題筆記裡
#使用 dummy node 來連結最小與最大 node
class Solution:
    def treeToDoublyList(self, root):
        if not root: 
            return
        dummy = Node(0, None, None)
        prev = dummy
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left, prev.right, prev = prev, node, node
            node = node.right
        dummy.right.left, prev.right = prev, dummy.right
        return dummy.right

#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        stack = []
        dummy = pre = Node(0)
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left = pre
            pre.right = node
            pre = node
            node = node.right
        dummy.right.left = pre
        pre.right = dummy.right
        return dummy.right


# 重寫第三次, time complexity O(n), space complexity O(n)
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        stack = []
        dummy = pre = Node(0)
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left = pre
            pre.right = node
            pre = node
            node = node.right
        dummy.right.left = pre
        pre.right = dummy.right
        return dummy.right


#自己想的, time complexity O(n)
#思路: 利用bst的特性和分治法, 回報該node區間的最小node, 與最大node, 以利上面的node做判斷, 互相連結左區間的最大值, 右區間的最小值
#注意: 最後 最大node, 最小node 頭尾要相連接, 所以return left_min, right_max
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        left, right = self.dfs(root)
        left.left = right
        right.right = left
        return left
    
    def dfs(self, node):
        left, right = node, node #若沒有左右children, return 自己
        if node.left:
            left_min, left_max = self.dfs(node.left)
            node.left = left_max
            left_max.right = node
            left = left_min
        if node.right:
            right_min, right_max = self.dfs(node.right)
            node.right = right_min
            right_min.left = node
            right = right_max
        return (left, right)












