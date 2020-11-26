'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." 
Besides the root, each house has one and only one parent house. 
After a tour, the smart thief realized that "all houses in this place forms a binary tree". 
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
'''


# We construct a dp tree.
# Each node (dp_node) in this dp tree is an array of two elements:
# dp_node = [your gain when you ROB the current node, your gain when you SKIP the current node]

# dp_node[0] =[your gain when you ROB the current node]
# dp_node[1] =[your gain when you SKIP the current node]
# we start by scanning from the leaf: Depth First Search

# For each node you have 2 options:

# option 1: ROB the node, then you can't rob the child/children of the node.
# dp_node[0] = node.val + dp_node.left[1] + dp_node.right[1]
# option 2: SKIP the node, then you can ROB or SKIP the child/children of the node.
# dp_node[1] = max(dp_node.left[0], dp_node.left[1]) + max(dp_node.right[0], dp_node.right[1])
# the maximum of gain of the node depents on max(dp_node[0],dp_node[1])

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



    """
    Input: [3,4,5,1,3,null,1]
 input tree            dp tree:
     3                  [3+3+1,4+5]
    / \                /        \
   4   5            [4,3]      [5,1]
  / \   \          /     \          \
 1   2   1      [1,0]    [2,0]     [1,0]
                / \       /  \        /  \
           [0,0] [0,0] [0,0] [0,0]  [0,0] [0,0]
    
    """
# 刷題用這個
# 分治法 Depth First Search 經典好題
# 其實就是 divide and conquer, 分治法 
# time complexity O(n), space complexity O(n), n is total nodes
# But we used LogN level of recursion. N is the number of houses.
# 注意!! 不是dp
# 思路: 利用分治法查詢左右(左右 + 不包含左右的左右一層最大值, 不包含左右最大值), 再merge return 給上層 (當層+不包含下一層最大值, 不包含當層最大值)
class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root))
    
    def dfs(self, root: TreeNode):
        if not root:
            return (0, 0) #有沒有包括自己都是0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return (root.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1]))

# 用這例子思考比較好懂 => 4+3 = 7
         4
        /
      1
     /   
   2
  /
3

# 自己重寫
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.dfs(root))
    
    def dfs(self, node):
        if not node:
            return (0,0)
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        return (node.val + left[1] + right[1], max(left) + max(right))


@@
# what it means to get max(dp_node.left[0], dp_node.left[1]) + max(dp_node.right[0], dp_node.right[1]) is

# for the left child node, I have two choices: to ROB or to SKIP. I make the choice based on which choice gives me the maximum gain. 
# thus max(dp_node.left[0], dp_node.left[1])
# for the right child node, I follow the same logic. I have two choices: to ROB or to SKIP. 
# I make the choice based on which choice gives me the maximum gain. thus max(dp_node.right[0], dp_node.right[1])
# the max gain of option 2 is the sum of max gain based on the choice I made for left child node and max gain based on the choice I made for right child node






