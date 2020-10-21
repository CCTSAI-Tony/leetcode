'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''

# What does the "stateless functional view of algorithms" mean?

# We can think of an algorithm in the abstract as a description of a mechanism that takes certain inputs and produces certain outputs independent of the state of the world. 
# If you have a mechanism called "sum" that takes in 2 and 3 and produces 5, 
# it always produces 5 when given 2 and 3, no matter what the phase of the moon or who is the king of France today. 
# There is no "state" that the algorithm must consult other than the values provided as arguments.

# The distinction the author is drawing is that even in algorithms that are "pure" in this respect, 
# it is often convenient to do some pre-processing, store that as state, and then use that state during the operation of an algorithm. 
# Even if the result is an algorithm that appears to not depend on the state of the world, internally it is consuming or modifying its own private universe of state.

# Variables declared inside the class definition, but not inside a method are class or static variables:

# >>> class MyClass:
# ...     i = 3
# ...
# >>> MyClass.i
# 3 


# Python O( N ) solution. easy to understand

# EDIT: Thanks to @WKVictor , this solution uses 'deque' instead of 'list' as queue. And the performance is O( N )

# This is a great solution, but it is not O(N) because you pop(0) in the build() function. 
# Every pop(0) is already O(N) and this operation is applied to all nodes. Instead, you can use deque() for the list vals.

https://www.geeksforgeeks.org/binary-search-tree-data-structure/ 建議複習一下 binary search tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# leetcode 105 相同概念順便練習, time complexity O(n)
# 思路: 利用preorder 來封裝binary search tree, 並以此傳送string, 記得node 與 node 之間要間隔, 以利之後解碼
# 之後利用 bst 特性 minVal < vals[0] < maxVal 搭配preorder pop root的順序 來重建binary tree, 
import collections
class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        vals = []
        self.preOrder(root, vals)
        return " ".join(map(str, vals))  #技巧 node.val 記得留空格已利之後解碼
    
    def preOrder(self, node, vals):
        if node:
            vals.append(node.val)
            self.preOrder(node.left, vals)  #preorder, root left right
            self.preOrder(node.right, vals)
        
    # O( N ) since each val run build once
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        vals = collections.deque(int(val) for val in data.split())   #記得解碼需先轉成int(), split() 預設split 任何空格 => split(" ")
        return self.build(float("-inf"), float("inf"), vals)  
    
    def build(self, minVal, maxVal, vals):
        if vals and minVal < vals[0] < maxVal:  #一旦 vals[0] 的值不符合此不等式, 代表此node 為null, 換右邊tree
            val = vals.popleft()
            node = TreeNode(val)
            node.left = self.build(minVal, val, vals)  #建立左邊, 高招, recursion, maxVal = val
            node.right = self.build(val, maxVal, vals)
            return node
        return None

#自己重寫
import collections
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        vals = []
        self.preorder(root, vals)
        return " ".join(map(str, vals))
    
    def preorder(self, node, vals):
        if node:
            vals.append(node.val)
            self.preorder(node.left, vals)
            self.preorder(node.right, vals)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        vals = collections.deque([int(i) for i in data.split()])
        return self.build(float("-inf"), float("inf"), vals)
    
    def build(self, minval, maxval, preorder):
        if preorder and minval < preorder[0] < maxval:
            root_val = preorder.popleft()
            root = TreeNode(root_val)
            root.left = self.build(minval, root_val, preorder)
            root.right = self.build(root_val, maxval, preorder)
            return root
        return None
#binary search tree 重點: 左邊都是放比root 小的, 右邊都是放比root大的

# vals = [1,2,3,4,5,6]
# ' '.join(map(str, vals))

# '1 2 3 4 5 6'

# data = '1 2 3 4 5 6'
# vals = collections.deque(int(val) for val in data.split())
# vals
# deque([1, 2, 3, 4, 5, 6])

# collections.deque(i for i in range(5)), deque 裡面要放 iterable object
# deque([0, 1, 2, 3, 4])

# list(i for i in range(5))
# [0, 1, 2, 3, 4]

# what's the difference between this and #297 ?

# For Binary tree solution, we need to have "#" or "null" to indicate null node in the serialized string.
# However, for BST, we don't need such "#" which make it more compact.

# BT may have duplicated values while BST not.






































