'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, 
just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

此題與leetcode 117最大差別是此題給perfect binary tree, 但117是一般binary tree, 所以117的解法適用116
參照leetcode 117解法

#time complexity O(n)
#思路: 使用new_queue 來代表下層node, 當層queue都沒有元素時, 代表目前node是當層最後一個, 接None, 不然node.next = 現在當層queue的左邊第一個
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque([root])
        while queue:
            new_queue = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
                if not queue:
                    node.next = None
                else:
                    node.next = queue[0]
            queue = new_queue
        return root


#自己重寫, 刷題用這個, space complexity O(1), time complexity O(n)
#思路: double while loops, 利用linked list 的想法 搭配dummy node 來連結同level的next, 記住, dummy.next都會連結下層最左邊的node, 當作下一個root
#temp指針搭配dummy  來連結 root 下層的node, 當root左右child 都連結後, 移動root to root.next, 使得下層node可以跨 root 連結!!
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        res = root
        dummy = temp = Node(0)
        while root:
            while root:
                if root.left:
                    temp.next = root.left
                    temp = temp.next
                if root.right:
                    temp.next = root.right
                    temp = temp.next
                root = root.next
            root = dummy.next
            dummy.next = None
            temp = dummy
        return res


#重寫第二次, time complexity O(n), space complexity O(1)
#思路: 使用linkedlist 來串連下層node
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        res = root
        dummy = cur = Node(0)
        while root:
            while root:
                if root.left:
                    cur.next = root.left
                    cur = cur.next
                if root.right:
                    cur.next = root.right
                    cur = cur.next
                root = root.next
            root = dummy.next
            cur = dummy
            dummy.next = None
        return res


#重寫第三次, time complexity O(n), space complexity O(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        res = root
        dummy = temp = Node()
        while root:
            while root:
                if root.left:
                    temp.next = root.left
                    temp = temp.next
                if root.right:
                    temp.next = root.right
                    temp = temp.next
                root = root.next
            root = dummy.next
            temp = dummy
            dummy.next = None
        return res









......................................................................................................................................................................... 
#DFS + stack
class Solution:
    def connect(self, root):
        if not root:
            return 
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left and curr.right: #check if it is not the last level
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left #bridge
                stack.append(curr.right) #先左先右其實不影響答案 只是遍歷順序問題
                stack.append(curr.left)
        return root

#BFS + stack
class Solution:
    def connect2(self, root):
        if not root:
            return 
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                queue.append(curr.left)
                queue.append(curr.right)
        return root


#iteration
class Solution:
    def connect(self, root):
        if root and root.left and root.right: #這裡不能省略 if root 不然會產生 nonetype object has no attribute left
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root




















