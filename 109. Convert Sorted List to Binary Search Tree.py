'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

 '''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# convert to array first, time complexity O(n), space complexity O(h)
# 思路:  先把linked list 變成list, 再用dfs把整個list區間分一半, 中間的當作root, 之後左邊的中間當作root.left, 右邊的中間當作root.right, 
# why 整體區間 // 2 = mid 就可以當root, 若區間是偶數個node呢?  畫個圖就知道若是偶數個元素 mid 與 mid + 1 當root 都可以成為 height balanced BST
# 但奇數個就只能是mid 
# 因為是sorted list, 所以直接取list 的中間值, 左半邊都是比mid小, 右半邊都是比mid大, 符合bst 特性

#模板3 刷題用這個
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        left, right = 0, len(lst)-1
        return self.dfs(lst, left, right)
    
    
    def dfs(self, lst, left, right):
        if left + 1 > right:  # input [0]
            return TreeNode(lst[left])
        if left + 1 == right:  #[1,2]
            temp = TreeNode(lst[right])  
            temp.left = self.dfs(lst, left, left)
            return temp
        mid = (left + right) // 2
        root = TreeNode(lst[mid])  
        root.left = self.dfs(lst, left, mid - 1)  #跟普通模板3不一樣, 因為要避開mid 避免重複, 但剩下處理都一樣
        root.right = self.dfs(lst, mid + 1, right)
        return root

#這邊 temp = TreeNode(lst[left]) 也是可以的, 之後就是 temp.right = self.dfs(lst, right, right), 自己畫圖就知道, bst會不一樣, 但還是符合 height balanced BST



# 左閉又開
 class Solution:
    def sortedListToBST1(self, head):
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        return self.dfs(ls,0,len(ls))
    def dfs(self,ls,lower,upper):
        if lower == upper:
            return None
        mid = (lower + upper) // 2
        node = TreeNode(ls[mid])
        node.left = self.dfs(ls,lower,mid)
        node.right = self.dfs(ls,mid+1,upper)
        return node

#模板1
class Solution:
  def sortedListToBST1(self, head):
    ls = []
    while head:
        ls.append(head.val)
        head = head.next
    return self.helper(ls, 0, len(ls)-1)

  def helper(self, ls, start, end):
      if start > end:
          return None
      if start == end:
          return TreeNode(ls[start])
      mid = (start+end) // 2
      root = TreeNode(ls[mid])
      root.left = self.helper(ls, start, mid-1)
      root.right = self.helper(ls, mid+1, end)
      return root
 



'''
as the same as problem 108, but need to do some treatments to ListNode

'''
