'''
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
'''

# 自己重寫, time complexity O(n), space complexity O(n), 刷題用這個
# It's basically a modified level-order traversal
# 思路: 利用dict 來存儲每個col 的 node, 若node 有left node => 往下 col-1, right node => 往下 col + 1
# 利用bfs 來實現當層layer 相同row,col位置. 左邊優先的情況, 因為bfs 所以優先順序 => top to down

from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        queue = deque([(root, 0)])
        cols = defaultdict(list)
        max_index = float("-inf")
        min_index = float("inf")
        
        while queue:
            for _ in range(len(queue)):
                node, col = queue.popleft()
                cols[col].append(node.val)
                max_index = max(max_index, col)
                min_index = min(min_index, col)
                if node.left:
                    queue.append((node.left, col-1))
                if node.right:
                    queue.append((node.right, col+1))
        ans = []
        for k in range(min_index, max_index + 1):
            if k in cols:
                ans.append(cols[k])
        return ans


# 重寫第二次, time complexity O(nlogn), space complexity O(n)
from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        queue = deque([(root, 0)])
        cols = defaultdict(list)
        while queue:
            for _ in range(len(queue)):
                node, col = queue.popleft()
                cols[col].append(node.val)
                if node.left:
                    queue.append((node.left, col-1))
                if node.right:
                    queue.append((node.right, col+1))
        return [cols[col] for col in sorted(cols.keys())]



#自己想的dfs, time complexity O(klogk*mlogm), k: len(cols) m: len(col's nodes), 相比bfs 要兩個sort
#dfs 就要給予足夠的參數, 排序才能正確, ex: row, col, num(同個layer的位置) => 其實num位置參數可以不用, 因為dfs 早已左邊優先放進list
#只要sort(row) 就行了, 相同row, col 的先後順序不受sort(row)影響
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cols = defaultdict(list)
        self.dfs(root, 0, 0, 0, cols)
        return [[item[2] for item in sorted(cols[i], key= lambda x: (-x[0], x[1]))] for i in sorted(cols.keys())]
        
    def dfs(self, node, row, col, num, cols):
        cols[col].append((row, num, node.val))
        if node.left:
            self.dfs(node.left, row-1, col-1, 2*num, cols)
        if node.right:
            self.dfs(node.right, row-1, col+1, 2*num + 1, cols)

#自己重寫 8/28/2020
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cols = defaultdict(list)
        self.dfs(root, 0, 0, cols)
        return [[item[1] for item in sorted(cols[i], key= lambda x: -x[0])] for i in sorted(cols.keys())]
        
    def dfs(self, node, row, col, cols):
        cols[col].append((row, node.val))
        if node.left:
            self.dfs(node.left, row-1, col-1, cols)
        if node.right:
            self.dfs(node.right, row-1, col+1, cols)
