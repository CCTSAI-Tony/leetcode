'''
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. 
There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. 
A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

 

Example 1:


Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:


Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. 
Then, we move one coin from the root of the tree to the right child.
 

Constraints:

The number of nodes in the tree is n.
1 <= n <= 100
0 <= Node.val <= n
The sum of all Node.val is n.
'''

# https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/466780/Python-with-detailed-explanation

'''
Intuition

If the leaf of a tree has 0 coins (an excess of -1 from what it needs), 
then we should push a coin from its parent onto the leaf. If it has say, 4 coins (an excess of 3), 
then we should push 3 coins off the leaf. In total, 
the number of moves from that leaf to or from its parent is excess = Math.abs(num_coins - 1). 
Afterwards, we never have to consider this leaf again in the rest of our calculation.
'''


# 刷題用這個, time complexity O(n), space complexity O(h)
# 思路: one move 只移動1 coin, 從最簡單condition 推起, 把 leaf node 多餘的錢 或少於的錢 變成abs(val) 傳回給parent 代表所需要的moves 來分配coints
# 因為每個node 的 coins >= 0, 傳回給parent 前, 記得-1 (自己需要留一個coin 或需要得到一個coin)
# 紀錄 bottom up process 中, coin 傳送的count 數
class Solution(object):
    def distributeCoins(self, root):
        self.ans = 0

        def dfs(node):
            if not node: 
                return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1 # 回傳給parent 總錢數

        dfs(root)
        return self.ans

# 重寫第二次, time complexity O(n), space complexity O(h)
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            ans += (abs(left) + abs(right))
            return left + right + node.val - 1 
        dfs(root)
        return ans

# 重寫第3次, time complexity O(n), space complexity O(h)
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans += (abs(left) + abs(right))
            return left + right + node.val - 1
        dfs(root)
        return self.ans

