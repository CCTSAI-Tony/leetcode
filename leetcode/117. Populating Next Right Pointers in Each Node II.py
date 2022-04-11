'''
Given a binary tree

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

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), 
your function should populate each next pointer to point to its next right node, 
just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100

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


#自己重寫, 刷題用這個, space complexity O(1), time complexity O(n)
#思路: double while loops, 利用linked list 的想法 搭配dummy node 來連結同level的next, 記住, dummy.next都會連結下層最左邊的node, 當作下一個root
#temp指針搭配dummy  來連結 root 下層的node, 當root左右child 都連結後, 移動root to root.next, 使得下層node可以跨root 連結!!
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        res = root
        dummy = temp = Node(-1)
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
#思路: 跟116解法一樣, 使用linkedlist
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        dummy = cur = Node(0)
        res = root
        while root:
            while root:
                if root.left:
                    cur.next = root.left
                    cur = cur.next
                if root.right:
                    cur.next = root.right
                    cur = cur.next
                root = root.next
            cur = dummy
            root = cur.next
            cur.next = None
        return res

#重寫第三次, time complexity O(n), space complexity O(n)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        dummy = temp = Node()
        res = root
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

#自己想的, bfs, space complexity O(n), time complexity O(n)
#思路: 使用new_queue 來代表下層node, 當層queue都沒有元素時, 代表目前node是當層最後一個(預設next = None), 不然node.next = 現在當層queue的左邊第一個
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
                    break
                else:
                    node.next = queue[0]
            queue = new_queue
        return root

# bfs 第二解法
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        res = root
        queue = deque([root])
        while queue:
            dummy = cur = Node(0)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    cur.next = node.left
                    cur = cur.next
                if node.right:
                    queue.append(node.right)
                    cur.next = node.right
                    cur = cur.next
        return res

.........................................................................................................................................................................       
#space complexity O(1), time complexity O(n)
#思路: double while loops, 利用linked list 的想法 搭配dummy node 來連結同level的next, 記住, dummy.next都會連結下層的最左邊, 當作下一個root
#temp指針搭配dummy  來連結 root 下層的node, 當root左右child 都連結後, 移動root to root.next, 使得下層node可以跨root 連結!!
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        dummy = Node(-1, None, None, None)
        tmp = dummy
        res = root
        while root:
            while root:
                if root.left:
                    tmp.next = root.left
                    tmp = tmp.next
                if root.right:
                    tmp.next = root.right
                    tmp = tmp.next
                root = root.next
            root = dummy.next
            tmp = dummy
            dummy.next = None  #back to default
        return res



#思路: 利用bfs 來加入每層的node, 利用tail來紀錄每層的最右邊(最後一個加入的)
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        stack = deque([root])
        tail = root #記錄尾巴
        while stack:
            node = stack.popleft() #bfs
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if node == tail:
                tail.next = None
                tail = stack[-1] if stack else None #stack[-1] 當層最後一個
            else:
                node.next = stack[0] #接續右邊
        return root


















