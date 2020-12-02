'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
'''
# 此題重要的是 當層node要放在同個list裡

'''
from collections import deque
queue = deque('24565435564')
queue

deque(['2', '4', '5', '6', '5', '4', '3', '5', '5', '6', '4'])

from collections import deque
queue = deque([2,3,4,5,5,6])
queue

deque([2, 3, 4, 5, 5, 6])

a = []
a.append([2])
a

[[2]]

'''

#自己重寫 time complexity O(n), space complexity O(n)
#思路: bfs traversal, 設立layer 每過一層就把該layer的node 加到res
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:  #這種edge case 一定要想到
            return []
        res = []
        queue = deque([root])
        while queue:
            layer = []
            for _ in range(len(queue)):
                node = queue.popleft()
                layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(layer)
        return res

#重寫第二次, time complexity O(n), space complexity O(n)
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

#重寫第三次, time complexity O(n), space complexity O(n)
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            new_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                new_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(new_level)
        return res


#自己想的, dfs, time complexity O(n), space complexity O(n)
from collections import defaultdict
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = defaultdict(list)
        self.helper(root, 0, levels)
        return levels.values()
    
    def helper(self, node, level, levels):
        if not node:
            return
        levels[level].append(node.val)
        self.helper(node.left, level + 1, levels)
        self.helper(node.right, level + 1, levels)


#單用一般的queue(list)
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue, res = [root] , []
        while queue:
            cur_level = []
            for i in range(len(queue)): #隨著當層有多少node 進行需要幾次iteration
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        return res

#使用deque
from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root: return []
        queue, res = deque([root]), [] #deque 裡面放的不是list 就是 string
        
        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft() #先後按照進入queue的順序
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val) #當層node放在同個list裡
            res.append(cur_level)
        return res

'''
Binary Tree Level Order Traversal

Time: O(N) | Space: O(size of return array + size of queue) -> Worst Case O(2N)
queue的概念用deque来实现，popleft() 时间复杂为O(1)即可

外围的While用来定义BFS的终止条件，所以我们最开始initialize queue的时候可以直接把root放进去
在每层的时候，通过一个cur_level记录当前层的node.val，size用来记录queue的在增加子孙node之前大小，因为之后我们会实时更新queue的大小。
当每次从queue中pop出来的节点，把它的左右子节点放进Queue以后，记得把节点本身的的value放进cur_level
for loop终止后，就可以把记录好的整层的数值，放入我们的return数组里。

A double-ended queue, or deque, supports adding and removing elements from either end. 
The more commonly used stacks and queues are degenerate forms of deques, where the inputs and outputs are restricted to a single end.

import collections

d = collections.deque('abcdefg')
print 'Deque:', d
print 'Length:', len(d)
print 'Left end:', d[0]
print 'Right end:', d[-1]

d.remove('c')
print 'remove(c):', d



Deque: deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
Length: 7
Left end: a
Right end: g
remove(c): deque(['a', 'b', 'd', 'e', 'f', 'g'])

import collections

# Add to the right
d = collections.deque()
d.extend('abcdefg')
print 'extend    :', d
d.append('h')
print 'append    :', d

# Add to the left
d = collections.deque()
d.extendleft('abcdefg')
print 'extendleft:', d
d.appendleft('h')
print 'appendleft:', d


extend    : deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
append    : deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
extendleft: deque(['g', 'f', 'e', 'd', 'c', 'b', 'a'])
appendleft: deque(['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'])
'''