'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]  bst 表達

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
'''

Python short and slick solution (108ms, beats 100%), both stack and Morris versions

# Here's a full solution using stack-based (iterative) inorder traversal. 
# Just to demonstrate how efficient this code is, I've included the code for a regular inorder traversal on the right:

# There are 2 cases: The values that need to be swapped are either adjacent or not adjacent. 
# If they're adjacent, then there will be one "drop"; if they're not adjacent, then there will be two "drops".

# adjacent: ... _ < _ < A > B < _ < _ ...
#                       ^^^^^
#                       drop #1

# not adjacent: ... _ < _ < A > X < _ < Y > B < _ < _ ... (X may be the same as Y, but it's irrelevant)
#                           ^^^^^       ^^^^^
#                           drop #1     drop #2
# In both cases, we want to swap A and B. 重要!! 題目說 Two elements of a binary search tree (BST) are swapped by mistake.

#刷題用這個, stack, 題目有說2個node 位置要互換
#思路: 依序從最小的位置慢慢遍歷到最大, 並且跟pre_node比較, 若發現小於pre_node, 代表順序錯了, 要互換
#利用bst特性 右邊的tree 比root大, cur好比右邊的tree, prev 好比root, prev, cur = node, node.right 
#還有root 比左邊tree大, cur 好比root, prev 好比左邊的tree
#隨著stack.pop() 逐步pop出root們, 此時root 就要跟左邊tree最後一個遇到的值比
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root):                                               |  def inorder(self, root):  #left>root>right, 注意是binary search tree
        cur, prev, drops, stack = root, TreeNode(float('-inf')), [], []        |      cur, stack = root, []
        while cur or stack:                                                    |      while cur or stack:
            while cur:                                                         |          while cur:
                stack.append(cur)                                              |              stack.append(cur)  #space O(log n) 跟層數相關
                cur = cur.left                                                 |              cur = cur.left
             #tree最左邊的node                                                                    
            node = stack.pop()                                                 |          node = stack.pop()  #pop掉stack 最後一個, 最底層的left
            if node.val < prev.val:                                            |          print(node.val)
                drops.append((prev, node)) #找到不match的地方
            prev, cur = node, node.right                                       |          cur = node.right
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val  |



#重寫第二次, time complexity O(n), space complexity O(1), 要注意的就是交換的位置
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        drops = []
        cur, prev = root, TreeNode(float("-inf"))
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val < prev.val:
                drops.append((cur, prev))
            cur, prev = cur.right, cur
        drops[0][1].val, drops[-1][0].val = drops[-1][0].val, drops[0][1].val







Input: [1,3,null,null,2]  bst 表達

   1
  /
 3
  \
   2

drops: [(3,2),(2,1)]

   1
  /
 3

drops: [(3,1)]

Full solution using Morris inorder traversal: constant space solution, 
time complexity O(N), space complexity O(1)

class Solution:
    def recoverTree(self, root):                                               |  def inorderMorris(self, root):
        cur, prev, drops = root, TreeNode(float('-inf')), []                   |      cur = root
        while cur:                                                             |      while cur:
            if cur.left:                                                       |          if cur.left:
                temp = cur.left                                                |              temp = cur.left
                while temp.right and temp.right != cur: temp = temp.right      |              while temp.right and temp.right != cur: temp = temp.right
                if not temp.right:                                             |              if not temp.right:
                    temp.right, cur = cur, cur.left                            |                  temp.right, cur = cur, cur.left
                    continue                                                   |                  continue
                temp.right = None                                              |              temp.right = None
            if cur.val < prev.val: drops.append((prev, cur))                   |          print(cur.val)
            prev, cur = cur, cur.right                                         |          cur = cur.right
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val  |



# Explanation
# I don't have any new ideas; just a cool way to implement an old idea.

# Use whatever inorder traversal you like (recursion/stack = O(log n) extra space, Morris = O(1) extra space). 
# As most people have figured out pretty easily, 
# the idea is to remember the last value you saw and compare it with the current value. If lastValue > currentValue, 
# then we know that something is "wrong", but it's not immediately clear which values have to be swapped.

# There are 2 cases: The values that need to be swapped are either adjacent or not adjacent. 
# If they're adjacent, then there will be one "drop"; if they're not adjacent, then there will be two "drops".

# adjacent: ... _ < _ < A > B < _ < _ ...
#                       ^^^^^
#                       drop #1

# not adjacent: ... _ < _ < A > X < _ < Y > B < _ < _ ... (X may be the same as Y, but it's irrelevant)
#                           ^^^^^       ^^^^^
#                           drop #1     drop #2
# In both cases, we want to swap A and B. 重要!! 題目說 Two elements of a binary search tree (BST) are swapped by mistake.

# So the idea is to keep a drops array and append a tuple of (lastNode, currentNode) whenever we come across lastValue > currentValue. 
# At the end of the traversal, the drops array must have either 1 or 2 tuples (otherwise, there would be more than 2 nodes that need to be swapped).

# Here's the clear but not-so-clean way to swap them:

# if len(drops) == 1: # drops == [(A, B)]
#     drops[0][0].val, drops[0][1].val = drops[0][1].val, drops[0][0].val
# else: # drops == [(A, X), (Y, B)]
#     drops[0][0].val, drops[1][1].val = drops[1][1].val, drops[0][0].val
# Here's the clean but not-so-clear way that gets rid of the conditional branching:

# drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val


https://www.youtube.com/watch?v=wGXB9OWhPTg&t=14s

Inorder Tree Traversal – Morris Traversal

# Python program to do inorder traversal without recursion and 
# without stack Morris inOrder Traversal
  
# A binary tree node
class Node:
      
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
  
# Iterative function for inorder tree traversal
def MorrisTraversal(root):
      
    # Set current to root of binary tree
    current = root 
      
    while(current is not None):
          
        if current.left is None:
            print current.data ,
            current = current.right
        else:
            #Find the inorder predecessor of current
            pre = current.left
            while(pre.right is not None and pre.right != current):
                pre = pre.right
   
            # Make current as right child of its inorder predecessor
            if(pre.right is None):
                pre.right = current
                current = current.left
                  
            # Revert the changes made in if part to restore the 
            # original tree i.e., fix the right child of predecssor
            else:
                pre.right = None
                print current.data ,
                current = current.right
              
# Driver program to test above function
""" 
Constructed binary tree is
            1
          /   \
        2      3
      /  \
    4     5
"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
  
MorrisTraversal(root)
  
# This code is contributed by Naveen Aili


# Python program for Morris Preorder traversal (Root, Left, Right) 
  
# A binary tree Node 
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
# Preorder traversal without  
# recursion and without stack 
def MorrisTraversal(root): 
    curr = root 
  
    while curr: 
        # If left child is null, print the 
        # current node data. And, update  
        # the current pointer to right child. 
        if curr.left is None: 
            print(curr.data) 
            curr = curr.right 
  
        else: 
            # Find the inorder predecessor 
            pre = curr.left 
  
            while pre.right is not None and pre.right is not curr: 
                pre = pre.right 
  
            # If the right child of inorder 
            # predecessor already points to 
            # the current node, update the  
            # current with it's right child 
            if pre.right is curr: 
                pre.right = None
                curr = curr.right 
                  
            # else If right child doesn't point 
            # to the current node, then print this 
            # node's data and update the right child 
            # pointer with the current node and update 
            # the current with it's left child 
            else: 
                print (curr.data) 
                pre.right = curr  
                curr = curr.left 






Post-order Python Morris

def post_order(root):
    if not root:
        return []

    current = root
    post_order_list = []

    while current:
        if not current.right:
            post_order_list.insert(0, current.val)  #insert(0) 代表位置index 0
            current = current.left
        else:
            # find left most of the right sub-tree
            predecessor = current.right
            while (predecessor.left) and (predecessor.left != current):
                predecessor = predecessor.left
            # and create a link from this to current
            if not predecessor.left:
                post_order_list.insert(0, current.val)
                predecessor.left = current
                current = current.right
            else:
                predecessor.left = None
                current = current.left
    return post_order_list






#刷題用這個
class Solution:
    def recoverTree(self, root):      
        cur, prev, drops = root, TreeNode(float('-inf')), []
        while cur:
            if cur.left:
                temp = cur.left
                while temp.right and temp.right != cur:
                    temp = temp.right
                if not temp.right:
                    temp.right = cur
                    cur = cur.left
                    continue
                temp.right = None
            if cur.val < prev.val:
                drops.append((prev, cur))
            prev, cur = cur, cur.right
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0]






































