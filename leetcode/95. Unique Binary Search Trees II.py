# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2], 1,none > 1,none,3,2,none > 1,none,3,2
  [3,2,null,1],>  3,2,none,1 最後系統會直接審略後面的none
  [3,1,null,null,2], 3,1,none,none,2
  [2,1,3], 
  [1,null,2,null,3] >1,none,2,none,3
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:
                          *
   1         3     3      2      1
    \\       /     /      / \\     \
     3     2     1      1   3      2
    /     /       \\                \
   2     1         2                 3


'''
#time complexity O(n^2)
#思路: dfs 分治法
class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.cal([i for i in range(1, n+1)]) #[1,2,3,,,n], 讓每個數字當作node
        
    def cal(self, lst):
        if not lst: 
            return [None] #base case 
        res=[] #這是放在help內 代表當層開始都是空的, 下層不影響上層
        for i in range(len(lst)):
            for left in self.cal(lst[:i]): #左右分開 最後會變成 for left in none
                for right in self.cal(lst[i+1:]):
                    node, node.left, node.right=TreeNode(lst[i]), left, right
                    res+=[node]
        return res
'''
【思路】

二叉查找树，也称为二叉搜索树，二叉排序树。它可以是一棵空树，也可以是具有下列性质的二叉树：

         若二叉查找树的左子树不空，则左子树上的所有结点的值均小于它的根结点的值，若右子树不为空，则右子树上所有结点的值均大于它的根结点的值；它的左右子树也分别为二叉排序树。


[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

注意: 最後子節點沒有後續   都是先報左再抱右 root層左右都要報,  !!!!冷大哥說此數據結構遍歷到最後的子節點不會出現none 系統直接省略none 
'''

'''
self.cal([i for i in range(1, n+1)])
We want all possible BST made of sequence of length n with root value 1, and all possible BST with root value 2 , and so on to root value n, all together we get our answer

for left in self.cal(lst[:i]):
          for right in self.cal(lst[i+1:]):
lst[i] is the root value of the following BSTs we want to calculate
To construct BST of root value lst[i], we just need to construct BST using lst[:i] and set it as left child, construct BST using lst[i+1:] and set it as right child
cal(lst[:i]) returns all possible BST made of sequence of length i , with root value from lst[0] to lst[i-1]
cal(lst[i+1:]) returns all possible BST made of sequence of length len(lst) - (i + 1), with root value from ls[i+1] to lst[-1]:last one
now we can just iterate through all combinations of left child structure and right child structure and we are done




'''