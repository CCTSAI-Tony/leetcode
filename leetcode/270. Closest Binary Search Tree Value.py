'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
'''

#自己想的, time complexity O(logn)
#思路: bst, 針對每個遍歷node計算node.val 與 target的距離, 若小於前面的紀錄則更新答案node, 依照bst的特性, 若target > node.val, 則往右邊遍歷, 不需往左邊, 反之亦然
#因為往左邊遍歷的node與target的距離 一定都比該當層node來得高
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.close = float("inf")
        self.ans = None
        self.dfs(root, target)
        return self.ans.val
    
    def dfs(self, node, target):
        if not node:
            return
        temp = abs(node.val - target)
        if temp < self.close:
            self.close = temp
            self.ans = node
        if target > node.val:
            self.dfs(node.right, target)
        elif target < node.val:
            self.dfs(node.left, target)





            