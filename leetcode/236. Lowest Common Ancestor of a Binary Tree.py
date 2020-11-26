'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node 
in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/158060/Python-DFS-tm

# 236. Lowest Common Ancestor of a Binary Tree
# > 类型：DFS分制
# > Time Complexity O(n)
# > Space Complexity O(h)

# p and q are different and both values will exist in the binary tree. 題目條件!
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/158060/Python-DFS-tm
# 这道Follow Up没有BST的特性，所以要对几种case一个一个进行测试。
# Condition为两种：如果没找到，返回None，找到则返回当前的root(因为找到一个root就不需要继续深入)
# 比对方式：
# 如果parent的左右孩子都有返回，说明parent就是LCA
# 如果左边没有返回：则右边返回的就是LCA 包含嵌套關係
# 如果右边没有返回：则左边返回的就是LCA 包含嵌套關係

# Time Complexity O(n), Space Complexity O(h)
# 思路: 請用例圖做推演, 搜尋左右子樹是否為 p, q node, 若找到則回報該 node 給上一層, 若當層左右都有回報則代表該node 就是 lca, 並回報當層TreeNode給上一層
# 從最上層root的角度看, 若沒有左右同時回報, 則代表左, 右其一有回報的必定是lca (包含嵌套case, p是ｑ的children之類的)
# 但從其他node看, 若沒有左右同時回報, 則回報該分支的結果給上一層
class Solution(object):
    def lowestCommonAncestor(self, root, p, q) -> 'TreeNode':
        if not root: #沒搜索到
            return None
            # 也可以為 if root in (p, q):
        if root == p or root == q: #找到其中一個node(找到一个root就不需要继续深入), 因此嵌套的node會找不到
            return root
        left = self.lowestCommonAncestor(root.left, p , q)
        right = self.lowestCommonAncestor(root.right, p , q)
        
        if left and right:
            return root
        elif not left:
            return right 
        else:
            return left

# 不行 if root == (p or q), why, (p or q) 永遠只會return 第一個為True 的 object, q永遠不會被evaluated
# (2 or 5) => 2, (5 or 2) => 5
# 不行 if root == p or q:
# why? similar to the example belowx
# if name == "Kevin" or "Jon" or "Inbar":
#     is logically equivalent to:
# if (name == "Kevin") or ("Jon") or ("Inbar"):

# There are two common ways to properly construct this conditional.

# Use multiple == operators to explicitly check against each value:
# if name == "Kevin" or name == "Jon" or name == "Inbar":

# Compose a sequence of valid values, and use the in operator to test for membership:
# if name in {"Kevin", "Jon", "Inbar"}:


# Q & A
# 问题一：为啥左边没有返回，则右边返回的就是lca啊 (@chris1011)

# image

# 题目定义里明确了p和q都是unique的值，并且p和q都存在于这颗树里。
# 所以举个例子

# 如果p = 5， q = 4

# 我们得知的信息是，就算root节点3的右边不包含p或者q其中任何一个节点，左边也必须会有一个最小公共祖先，因为这道题允许嵌套关系

# 理解了这点，回答你的问题，我们为什么没有右则返回左(你的问题是没有左返回右，一个道理哈)，当我们递归完，左右分别返回到root节点3，得到下面的结果：

# root的左边返回回来5
# root的右边返回回来None (因为q=4，和p是嵌套关系，不在root的右边)
# 根据题目定义，我们知道只要左边有返回，右边返回None也没关系。因为另外一个node，和左边返回上来的5，一定是嵌套的关系。
# 所以LCA就是左边返回上来的5。





