'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''

https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram 強烈建議看

This problem requires quite a bit of quirky thinking steps. Take it slow until you fully grasp it.


# Concise DFS solution with detailed explanation [Python]

# The idea is to update node values with the biggest, positive cumulative sum gathered by its children:

# If both contributions are negative, no value is added.
# If both are positive, only the biggest one is added, so that we don't include both children during the rest of the tree exploration.
# Leaves return its own value and we recursively work our way upwards.
# A global maximum sum variable is maintained so that every path can be individually checked, 
# while updated node values on the tree allow for exploration of other valid paths outside of the current subtree.
# More details in the code comments:

#time complexity O(N), 分治法
# 思路: 在下層遇到左右分叉利用分治法來挑選比較大的一條路, 並在dfs的途中以目前的node當作root更新路徑sum最大值
# 思路: 這題利用左右子樹若貢獻值< 0則不加入的greedy思想 來找出最大的path sum
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return None
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum
    
    def dfs(self, node):
        if not node: 
            return 0
        
        # only add positive contributions, 可以斷支
        leftST_sum = max(0, self.dfs(node.left))
        rightST_sum = max(0, self.dfs(node.right))

        # check if cumulative sum at current node > global max sum so far
        # this evaluates a candidate path
        self.max_sum = max(self.max_sum, leftST_sum + rightST_sum + node.val)  
        
        # add to the current node ONLY one of the children contributions
        # in order to maintain the constraint of considering only paths
        # if not, we would be exploring the whole tree - against problem definition
        return max(leftST_sum, rightST_sum) + node.val



# The key is to always choose the maximum cumulative sum path, while updating the "global" maximum value, from the leaves upwards.





























