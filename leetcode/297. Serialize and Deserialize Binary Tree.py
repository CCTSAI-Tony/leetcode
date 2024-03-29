'''
Serialization is the process of converting a data structure or object into a sequence of bits 
so that it can be stored in a file or memory buffer, or transmitted across a network connection link 
to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on 
how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree 
can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to 
follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# > 类型：BFS
# > Time Complexity O(N)
# > Space Complexity O(N)

#刷題用這個 Time Complexity O(N), Space Complexity O(N), 這題解法可以套用在449
#思路: 此題精髓: level order traversal => bfs serialize, 利用q 存取TreeNode, 以利之後分解連結in serialize, or 連結nodes in deserialize
import collections 
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """    
        if not root: 
            return ""
        q = collections.deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
            res.append(str(node.val) if node else '#')
        return ','.join(res) #看下面例子
                
    
    def deserialize (self, data):
        if not data: 
            return None
        nodes = data.split(',') #['1', '2', '3']
        root = TreeNode(int(nodes[0]))
        q = collections.deque([root])#一開始只有root, TreeNode, 用來連結其他nodes
        index = 1 #指針
        while q: #先左再右, 同serialize
            node = q.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))  #記得int()
                q.append(node.left)
            index += 1 #換下一個元素不管當前元素是否'#'
        
            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1
        return root

# res = ['1','2','3']
# ','.join(res)

# '1,2,3'

# '1,2,3'.split(",")
# ['1', '2', '3']

input: [1,2,3,null,null,4,5]
data: ['1', '2', '3', '#', '#', '4', '5', '#', '#', '#', '#']


#重寫第二次, time complexity O(n), space complexity O(n), n: number of nodes
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None
        data = list()
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
            data.append(str(node.val) if node else "#")
        return " ".join(data)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split()
        root = TreeNode(int(data[0]))
        q = deque([root])
        idx = 1
        while q:
            node = q.popleft()
            if data[idx] != "#":
                node.left = TreeNode(int(data[idx]))
                q.append(node.left)
            idx += 1
            if data[idx] != "#":
                node.right = TreeNode(int(data[idx]))
                q.append(node.right)
            idx += 1
        return root


# 重寫第三次, time complexity O(n), space complexity O(n)
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            res.append(node.val if node else "#")
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(map(str, res))
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "#":
            return None
        data_s = data.split(",")
        root = TreeNode(int(data_s[0]))
        idx = 1
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if data_s[idx] != "#":
                node.left = TreeNode(int(data_s[idx]))
                queue.append(node.left)
            idx += 1
            if data_s[idx] != "#":
                node.right = TreeNode(int(data_s[idx]))
                queue.append(node.right)
            idx += 1
        return root

