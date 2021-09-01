'''
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. 
The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, 
where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.
'''

# 題目條件: The binary tree has the same structure as a full binary tree, but some nodes are null. 
# The width of one level is defined as the length between the end-nodes. 代表end-nodes都在同一層來計算level width, 最大width任何一層都有可能

# The main idea with this question is we will give each node a position value. If we go down the left neighbor, 
# then position -> position * 2; and if we go down the right neighbor, then position -> position * 2 + 1. 
# This makes it so that when we look at the position values L and R of two nodes with the same depth, the width will be R - L + 1.

# From there, we have two choices for traversals: BFS or DFS. In a BFS, all the nodes with the same depth are searched adjacent to each other, 
# so we only need to remember the first and last positions seen for each depth.

#自己重寫 bfs, time complexity O(n), 40ms
#思路: 為當層每個node 上位置編號, 最左邊0, 最右邊 2^h - 1 如何做到? 設上層root 位置編號k, 左邊就 k*2 右邊就 k*2 + 1, 自己推算就清楚
#再對當層紀錄最大最小值, none node則跳過, width 兩邊一定是非none node, 兩者相減+1 就是該層width
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        max_width = 0
        queue = deque([(root, 0)])
        while queue:
            layer_min = float("inf")
            layer_max = float("-inf")
            for _ in range(len(queue)):
                node, val = queue.popleft()
                if node:
                    layer_min = min(layer_min, val)
                    layer_max = max(layer_max, val)
                    queue.append((node.left, val*2))
                    queue.append((node.right, val*2 + 1))
            
            max_width = max(max_width, layer_max - layer_min + 1)
            
        return max_width


# 重寫第二次, time complexity O(n), space complexity O(n)
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        queue = deque([(root, 0)])
        while queue:
            layer_min = float("inf")
            layer_max = float("-inf")
            for _ in range(len(queue)):
                node, pos = queue.popleft()
                layer_min = min(layer_min, pos)
                layer_max = max(layer_max, pos)
                if node.left:
                    queue.append((node.left, pos*2))
                if node.right:
                    queue.append((node.right, pos*2 + 1))
            max_width = max(max_width, layer_max - layer_min + 1)
        return max_width


#自己重寫 dfs, time complexity O(n), 44ms
#思路: 為當層每個node 上位置編號, 最左邊0, 最右邊 2^k - 1 如何做到? 設上層root 位置編號k, 左邊就 k*2 右邊就 k*2 -1, 自己推算就清楚
#利用dfs 與 defaultdict 紀錄不同層每個node的pos, none node則跳過, width 兩邊一定是非none node, 兩者相減+1 就是該層width
#再從dict依續找出max(每層最大-最小) + 1 就是答案
from collections import defaultdict
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        levelPos = defaultdict(list)
        self.dfs(root, 0, 0, levelPos)
        return max(max(levelPos[i])- min(levelPos[i]) for i in levelPos) + 1
        
    def dfs(self, node, depth, pos, levelPos):
        if node:
            levelPos[depth].append(pos)
            self.dfs(node.left, depth+1, pos*2, levelPos)
            self.dfs(node.right, depth+1, pos*2-1, levelPos)





class Solution:
    def widthOfBinaryTree(self, root):
        queue = [(root, 0, 0)]
        cur_depth = left = ans = 0
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth+1, pos*2))
                queue.append((node.right, depth+1, pos*2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos  #當層最左邊的非 null node 第一個被紀錄被當left, 之後其他當層node 的 pos - 當層left + 1 就是width
                ans = max(pos - left + 1, ans)

        return ans


# It might be more natural to attempt a DFS. Here, we create a dfs iterator that yields the depth and position of each node.

# After, we need to know for each depth, what was the leftmost position left[depth] and the rightmost position right[depth]. 
# We'll remember the largest width as we iterate through the nodes.

#原來yield 可以這樣用
class Solution:
    def widthOfBinaryTree(self, root):
        left = {}
        right = {}
        ans = 0
        for depth, pos in self.dfs(root):
            left[depth] = min(left.get(depth, pos), pos)
            right[depth] = max(right.get(depth, pos), pos)
            ans = max(ans, right[depth] - left[depth] + 1)

        return ans

    def dfs(self, node, depth = 0, pos = 0):
            if node:
                yield depth, pos
                yield from dfs(node.left, depth + 1, pos * 2)
                yield from dfs(node.right, depth + 1, pos * 2 + 1)

 













 



















