'''
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, 
but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
 

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
 

Note: All the values of tree nodes are in the range of [-1e7, 1e7].
'''

#可以跟leetcode 543一起服用
#自己重寫, time complexity O(n), 經典題! 還要看parent.val 來決定return 的內容, return前 => update 全局變數
#思路: dfs分治法, 查看當下左右子node的 (increasing length, decreasing length), 並即時更新最大連續長度 => self.max_len = max(self.max_len, l_i+r_d+1, l_d+r_i+1)
#每個node return (increasing length, decreasing length) 給上一層, 隨著node.val 相較parent.val是連續上升還是連續下降or其他, 來調整return 的內容
#node.left => l_i, l_d, node.right => r_i, r_d, 若node.val = parent.val + 1 => return (max(l_i, r_i) + 1, 0), 因為node.val 相較parent.val 是increasing, 所以return 0 for decreasing
#若node.val = parent.val - 1 => return return (0, max(l_d, r_d) + 1), 因為node.val 相較parent.val 是decreasing, 所以return 0 for increasing
#若node.val 不跟parent.val 相差1 or 等於parent.val => return (0, 0)
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.max_len = 0
        self.dfs(root, root)
        return self.max_len
    
    def dfs(self, node, parent):
        if not node:
            return (0, 0)
        l_i, l_d = self.dfs(node.left, node)
        r_i, r_d = self.dfs(node.right, node)
        self.max_len = max(self.max_len, l_i+r_d+1, l_d+r_i+1)
        if node.val == parent.val + 1:
            return (max(l_i, r_i) + 1, 0)
        if node.val == parent.val - 1:
            return (0, max(l_d, r_d) + 1)
        else:
            return (0, 0)


