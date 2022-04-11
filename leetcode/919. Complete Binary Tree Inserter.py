'''
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

Implement the CBTInserter class:

CBTInserter(TreeNode root) Initializes the data structure with the root of the complete binary tree.
int insert(int v) Inserts a TreeNode into the tree with value Node.val == val so that the tree remains complete, and returns the value of the parent of the inserted TreeNode.
TreeNode get_root() Returns the root node of the tree.
 

Example 1:


Input
["CBTInserter", "insert", "insert", "get_root"]
[[[1, 2]], [3], [4], []]
Output
[null, 1, 2, [1, 2, 3, 4]]

Explanation
CBTInserter cBTInserter = new CBTInserter([1, 2]);
cBTInserter.insert(3);  // return 1
cBTInserter.insert(4);  // return 2
cBTInserter.get_root(); // return [1, 2, 3, 4]
 

Constraints:

The number of nodes in the tree will be in the range [1, 1000].
0 <= Node.val <= 5000
root is a complete binary tree.
0 <= val <= 5000
At most 104 calls will be made to insert and get_root.
'''
'''
Intuition

Consider all the nodes numbered first by level and then left to right. Call this the "number order" of the nodes.

At each insertion step, we want to insert into the node with the lowest number (that still has 0 or 1 children).

By maintaining a deque (double ended queue) of these nodes in number order, we can solve the problem. 
After inserting a node, that node now has the highest number and no children, so it goes at the end of the deque. 
To get the node with the lowest number, we pop from the beginning of the deque.

Algorithm

First, perform a breadth-first search to populate the deque with nodes that have 0 or 1 children, in number order.

Now when inserting a node, the parent is the first element of deque, and we add this new node to our deque.


'''

# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: 使用deque 搭配bfs 來把low level(底下有空缺) 又愈靠左的node 排在queue 的前面, 之後insert 的時候, 把insert 的node 放入queue 的尾端, 因為上一level 可能有些未填滿的node
# insert 的node 要插在queue的第一個node的下面, 直到左右都被插滿後, queue把第一個node 給pop掉
class CBTInserter(object):
    def __init__(self, root):
        self.deque = collections.deque()
        self.root = root
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, v):
        node = self.deque[0]
        self.deque.append(TreeNode(v))
        if not node.left:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.popleft()
        return node.val

    def get_root(self):
        return self.root


# 重寫第二次, time complexity O(n), space complexity O(n)
from collections import deque
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.queue = deque()
        self.q = deque([(root)])
        while self.q:
            for _ in range(len(self.q)):
                node = self.q.popleft()
                if not node.left or not node.right:
                    self.queue.append(node)
                if node.left:
                    self.q.append(node.left)
                if node.right:
                    self.q.append(node.right)

    def insert(self, val: int) -> int:
        node = TreeNode(val)
        self.queue.append(node)
        parent = self.queue[0]
        if not parent.left:
            parent.left = self.queue[-1]
        elif not parent.right:
            parent.right = self.queue[-1]
            self.queue.popleft()
        return parent.val
        

    def get_root(self) -> Optional[TreeNode]:
        return self.root
