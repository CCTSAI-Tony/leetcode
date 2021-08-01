'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.
'''

#自己重寫 time complexity O(n)
#思路: 利用inner, outer觀念 來判斷左右子樹是否對稱, 利用dfs 深入chceck, outer 的 outer 為最outer, inner的inner為最inner
#if not root => return True 滿重要的
#if 下層node outer 對稱, dfs 下下層outer, 直到盡頭, 再來換inner
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.dfs(root.left, root.right)
    
    def dfs(self, left, right):  #這種左右參數設計才能解題
        if not left and not right:
            return True
        if None in (left, right):
            return False
        
        if left.val == right.val:  #check 下層
            outer = self.dfs(left.left, right.right)
            inner = self.dfs(left.right, right.left)
            return outer and inner
        return False


# 重寫第二次, time complexity O(n), space complexity O(h)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.dfs(root.left, root.right)
    
    def dfs(self, left, right):
        if not left and not right:
            return True
        if None in [left, right]:
            return False
        if left.val == right.val:
            inner = self.dfs(left.right, right.left)
            outer = self.dfs(left.left, right.right)
            if inner and outer:
                return True
            return False
        return False


#bfs interative
#思路: 利用inner, outer 來判斷左右子樹是否對稱, if 下層node對稱, bfs 下下層, 
#dfs與bfs 都會完全遍歷所有pair, 只是順序不同而已
from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = deque([(root.left, root.right)])
        while queue:
            for _ in range(len(queue)):
                left, right = queue.popleft()
                if not left and not right:
                    continue
                if None in (left, right):
                    return False
                if left.val == right.val:
                    queue.append((left.left, right.right)) #outer
                    queue.append((left.right, right.left)) #inner
                else:
                    return False
        return True




#recursively solution
class Solution:
  def isSymmetric(self, root):
    if root is None:
      return True
    else:
      return self.dfs(root.left, root.right)

  def dfs(self, left, right):
    if left is None and right is None: #邊界情況 不能寫成if left and right == none > 會解釋成 if left ==true and right == none
      return True
    if left is None or right is None:
      return False

    if left.val == right.val:
      outPair = self.dfs(left.left, right.right)
      inPiar = self.dfs(left.right, right.left)
      return outPair and inPiar
    else:
      return False
'''
def tt():
    return True and False

tt()

False

def tt():
    return True and True

tt()

True


'''

#iteratively solution
class Solution:
	def isSymmetric(self, root):
      if root is None:
          return True
      stack = [(root.left, root.right)] #tuple
      while stack: #持續搜索
          left, right = stack.pop()
          if left is None and right is None:
              continue
          if left is None or right is None:
              return False
          if left.val == right.val:
              stack.append((left.left, right.right)) #outer
              stack.append((left.right, right.left)) #inner
          else:
              return False
      return True











