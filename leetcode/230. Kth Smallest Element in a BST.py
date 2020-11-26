'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#自己重寫 O(n), 刷題用這個, recursive
#思路: binary search tree 就要想到in order traversal, 使用全域變數來確認目前node是第幾小
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.level = 0
        self.ans = 0
        self.dfs(root, k)
        return self.ans
        
        
    def dfs(self, node, k):
        if not node:
            return
        self.dfs(node.left, k) #直探最小
        self.level += 1
        if self.level == k:
            self.ans = node.val
            return   #提早結束
        self.dfs(node.right, k)


#重寫第二次, time complexity O(n), space complexity O(h)
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.level = 0
        self.ans = None
        self.inorder(root, k)
        return self.ans
    
    def inorder(self, node, k):
        if not node or self.ans != None:
            return
        self.inorder(node.left, k)
        self.level += 1
        if self.level == k:
            self.ans = node.val
            return
        self.inorder(node.right, k)




#自己重寫 in order traversal, dfs iterative, 要多練習
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        level = 0
        while stack or root:
            while root:
                stack.append(root)
                root = root.left  
            root = stack.pop()  #root 切換成左分支最底層的node
            level += 1
            if level == k:
                return root.val
            root = root.right

#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        level = 0
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            level += 1
            if level == k:
                return root.val
            root = root.right

#重寫第三次, time complexity O(n), space complexity O(n)
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        level = 0
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            level += 1
            if level == k:
                return root.val
            root = root.right


# Recursive:
class Solution:
    def kthSmallest(self, root, k):
        self.k = k #class variable
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        self.helper(node.left) #go all the way down to the bottom node.left
        self.k -= 1 #trace back to the root, 回到上一層代表地位增加 k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)



#自己想的, 重寫第四次 bottom up, time compplexity O(n), space complexity O(h)
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = None
        self.inorder(root, 0, k)
        return self.res
    
    def inorder(self, node, rank, k):
        if not node:
            return rank
        cur = self.inorder(node.left, rank, k) + 1
        if cur == float("inf"):
            return float("inf")
        if cur == k:
            self.res = node.val
            return float("inf") #提早回去
        return self.inorder(node.right, cur, k)





# Iterative: plz know how the binary search tree works
class Solution:
    def kthSmallest(root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left #go all the way down to the bottom node.left the smallest
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right #go the node.right to find out the bigger one

















