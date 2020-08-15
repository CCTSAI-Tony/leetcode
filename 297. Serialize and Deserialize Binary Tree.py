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

#思路: bfs serialize, 利用q 存取TreeNode, 以利之後分解連結in serialize, or 連結nodes in deserialize
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










