'''
Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.

 

Example 1:


Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
Example 2:


Input: root = [1,null,2,null,0,3]
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 105

'''

#刷題用這個, time complexity O(n), space complexity O(n)
#思路: 分治法, 利用傳参方式, 把同一支脈上的最大值與最小值傳至leaf, 到leaf時計算這支脈的最大diff, 回傳給上一層node 來retrun 左右分支比較大的diff
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.dfs(root, float("-inf"), float("inf"))
    
    def dfs(self, node, curMax, curMin):
        if not node:
            return curMax - curMin
        curMax = max(curMax, node.val)
        curMin = min(curMin, node.val)
        left = self.dfs(node.left, curMax, curMin)
        right = self.dfs(node.right, curMax, curMin)
        return max(left, right)




#自己想的naive solution, time complexity O(n^2), space complexity O(n^2)
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.maxDiff = 0
        self.dfs(root)
        return self.maxDiff
    
    def dfs(self, node):
        if not node.left and not node.right:
            return [node.val]
        childs = []
        if node.left:
            childs += self.dfs(node.left)
        if node.right:
            childs += self.dfs(node.right)
        cur = node.val
        for num in set(childs):
            self.maxDiff = max(self.maxDiff, abs(cur - num))
        childs.append(cur)
        return childs