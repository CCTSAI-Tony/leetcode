'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \\       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \\       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
'''

# 刷題用這個, time complexity O(n), space complexity O(h)
# 思路: dfs
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(x, y) -> bool:
            if not x and not y:
                return True
            if None in [x, y]:
                return False
            if x.val == y.val:
                left = dfs(x.left, y.left)
                right = dfs(x.right, y.right)
                return True if left and right else False
            return False
        return dfs(p, q)


# DFS with stack   
class Solution(object):
    def isSameTree2(self, p, q):
        stack = [(p, q)] #tuple
        while stack:
            node1, node2 = stack.pop() #接續pop最後一個 深度搜索
            if not node1 and not node2: #兩者都是none 則contine 新迴圈
                continue
            elif None in [node1, node2]: #若其中有一為none
                return False
            else:
                if node1.val != node2.val:
                    return False
                stack.append((node1.right, node2.right)) #在此題 先right 還是left都可以 只是搜索方向不一樣而已
                stack.append((node1.left, node2.left)) #stack = stack = [(node1.right, node2.right),[(node1.left, node2.left)]]
        return True

# BFS with queue 
class Solution(object):  
    def isSameTree3(self, p, q):
        queue = [(p, q)] #新增的排在之前的後面
        while queue:
            node1, node2 = queue.pop(0) #pop(0) bfs 精神 同層搜完才往下層
            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
        return True
'''
There is no difference between "DFS with stack" and "BFS with queue "

Yes there is, the order you add to the stack/queue, and whether you pop off the left or the rightmost element.
'''

'''
小知識：
事实上是没有区别的，以下三种写法是等价的

class A:
    pass
    
class A():
    pass
    
class A(object):
    pass

'''




