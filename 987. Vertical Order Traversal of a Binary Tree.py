'''
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, 
we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

 

Example 1:



Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
Example 2:



Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 

Note:

The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.
'''


python queue + hash map, time complexity O(nlogn) 因為有sort
#思路: 利用dict 儲存同一x軸的座標的node, 再利用tuple (vd,node.val) 來對x軸的座標的 nodes 做排序, 例如 vd 越大者優先, 相同座標值越小者優先
# stack iteration
import collections
class Solution:
    def verticalTraversal(self,root):
        dic=collections.defaultdict(list)
        queue=[(root,0,0)]  #儲存node, position
        ans=[]
        while queue:
            for _ in range(len(queue)):
                node,hd,vd=queue.pop(0)  #bfs
                dic[hd].append((vd,node.val)) #利用dict 建立 hd: (vd,node.val) pair, 這邊hd 代表 x軸的座標
                if node.left:
                    queue.append((node.left,hd-1,vd-1))
                if node.right:
                    queue.append((node.right,hd+1,vd-1))
        for i in sorted(dic.keys()):  #從水平最左到最右遍歷每個verticle 線
            level=[x[1] for x in sorted(dic[i],key=lambda x:(-x[0],x[1]))]   #x = (vd, node.val), sorted(dic[i]:針對同一個水平做排序, -x[0] 負越少的排前面
            ans.append(level)
        return ans


# key=lambda x:(-x[0],x[1]), x[1] => 相同位置以數字小的優先

# ->Root node is considered as 0 horizontal distance.
# ->As we move left hd is decreased by 1 and is increased by 1 as we move right.
# ->vd is used to get the top to bottom series.
# ->comparison in each dic is done based on vd value
# -> if vd comes out to be same then node value is compared.



#自己重寫, 刷題用這個
#  思路: 利用dict 儲存同一x軸的座標的node(hd = key), 儲存以tuple 的形式 (vd, node.val)
#  再利用tuple (vd,node.val) 來對x軸的座標的 nodes 做排序, 例如 vd 越大者優先, 相同座標值越小者優先, res再append排序後的node.val, 
#  重複此流程從左到右遍歷每個x軸座標
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic = defaultdict(list)
        res = []
        self.dfs(root, 0, 0, dic)
        for i in sorted(dic.keys()):
            level = [x[1] for x in sorted(dic[i], key=lambda x: (-x[0],x[1]))]
            res.append(level)
        return res
    
    
    
    def dfs (self, node, hd, vd, dic):
        if node:
            dic[hd].append((vd, node.val))
            self.dfs(node.left, hd-1, vd-1, dic)
            self.dfs(node.right, hd+1, vd-1, dic)
















