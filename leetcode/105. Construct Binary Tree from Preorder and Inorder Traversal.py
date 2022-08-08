'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''

               1
             /    \
            2      3
          /  \\      \
         4    5       6
                    /   \
                   7     8
                    \
                     9

pre(root,l,r) (1)245 36798
in(l,root,r)  425 (1) 37968

Looking at preorder traversal, the first value (node 1) must be the root.
Then, we find the index of root within in-order traversal, and split into two sub problems.
'''

#  刷題用這個
#  自己重寫, 好理解 time complexity O(n^2), 因為pop(0), space complexity O(logn)
#  思路: 利用preorder(root>left>right) 的特性pop(0)找出該inorder序列最上層的root, 在利用root的index 與inorder特性 left>root>right, 把inorder拆兩部分
#  左子樹 |root| 右子樹, 先從左子樹遞迴搜尋左子樹這邊的root, 因為preorder.pop(0) 是優先pop出左子樹的root, 之後再對左子樹左右分割 左子樹的inorder, 並做相同的事
#  直到preorder pop完左子樹的部分, 開始pop右子樹的部分, 做一樣的事, 左右子樹 inorder切分到最後會變empty, 此時代表 null node
from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder = deque(preorder)
        return self.helper(preorder, inorder, 0, len(inorder))
    
    def helper(self, preorder, inorder, l, r):
        if l < r:
            val = preorder.popleft()
            root = TreeNode(val)
            idx = inorder.index(val)
            root.left = self.helper(preorder, inorder, l, idx) 
            root.right = self.helper(preorder, inorder, idx+1, r)
            return root
        return None




class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            root_value = preorder.pop(0)
            root_index = inorder.index(root_value)
            root = TreeNode(inorder[root_index])
            root.left = self.buildTree(preorder, inorder[:root_index]) #time complexity O(n)
            root.right = self.buildTree(preorder, inorder[root_index+1:])
            return root
        return None

#重寫第二次, time complexity O(nlogn), space complexity O(nlogn)
from collections import deque #用deque 減少time complexity, 因為 inorder[:idx]
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder = deque(preorder)
        return self.helper(preorder, inorder)
    
    def helper(self, preorder, inorder):
        if inorder:
            val = preorder.popleft()
            root = TreeNode(val)
            idx = inorder.index(val)
            root.left = self.helper(preorder, inorder[:idx]) 
            root.right = self.helper(preorder, inorder[idx+1:])
            return root
        return None

#重寫第三次, time complexity O(nlogn), space complexity O(nlogn)
from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder = deque(preorder)
        return self.dfs(preorder, inorder)
        
    def dfs(self, preorder, inorder):
        if not inorder:
            return
        val = preorder.popleft()
        root = TreeNode(val)
        idx = inorder.index(val)
        left = inorder[:idx]
        right = inorder[idx+1:]
        root.left = self.dfs(preorder, left)
        root.right = self.dfs(preorder, right)
        return root

#重寫第四次, time complexity O(nlogn), space complexity O(nlogn)
from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder = deque(preorder)
        return self.dfs(preorder, inorder)
    
    def dfs(self, preorder, inorder):
        if not inorder or not preorder:
            return
        val = preorder.popleft()
        index = inorder.index(val)
        if len(inorder) == 1:
            return TreeNode(val)
        else:
            node = TreeNode(val)
            left = self.dfs(preorder, inorder[:index])
            right = self.dfs(preorder, inorder[index+1:])
            node.left = left
            node.right = right
            return node



#dfs 
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.
 class Solution(object):
    def buildTree(self, preorder, inorder):
        if inorder: #這行重要, 若inorder 為空 return None, 給上面root null children
            ind = inorder.index(preorder.pop(0)) #找出inorder root 的index 這裡preorder.pop(0)依序pop出 inorder root, 最終preorder會pop完
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind]) #建構左樹 子樹走到最後會回報None  記得要先左後右 因為preorder.pop(0)順序是從左到右
            root.right = self.buildTree(preorder, inorder[ind+1:]) #建構右樹
            return root #注意 這裡return indentation 要在if 裡面, 若跟if同排則會產生local valuable衝突, 因為root 是 if 裡面的local valuable






list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5] 
print(list1.index(4)) 
3

list2 = ['cat', 'bat', 'mat', 'cat', 'pet'] 
print(list2.index('cat')) 
0  #回覆最前的index, 若有重複元素





a = Solution()
b = a.buildTree(None,None)
b == None
True

a = Solution()
b = a.buildTree([2,3,4],None)
b == None
True












'''