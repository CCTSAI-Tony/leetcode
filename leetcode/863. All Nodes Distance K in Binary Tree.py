'''
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
'''

# If we view the tree structure as the graph, 
# then it is easy to come up the BFS solution to find the nodes that are located at a certain distance from the target node.

# What is missing in the original tree data structure that makes the above idea a bit tricky to implement 
# is the explicit pointer to a node's parent which is the neighbor for a node, the same as its children nodes.

# Due to this missing pointer, there is no explicit way for a node to reach out directly its neighbor nodes that is connected through the parent node.

# So the solution becomes clear, let's construct a graph from a given tree structure. 

# construct a map that maps each node to its parent. One could use less space in this case, since we do not store the child nodes as opposed to the above option.

# If one gets the above intuition, then it should not be a daunting job to implement the solutions. Here are some examples.


# set() 可以變 list() 不影響結果
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#  DFS AND GRAPH METHOD, TIME COMPLEXITY O(N)
#  The given tree is non-empty. 所以不用check if not root...
#  思路: 利用dict 建立往parent 的橋樑, 把binary tree轉化成undirected graph, 從target向外遍歷, 離target k edges的 nodes => append to ans
#  記得建立visited 防止重複遍歷, undiredted graph
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        parent_map = {}
        self.buildParentMap(root, None, parent_map)  #建立與上層連結
        ans = []
        visited = []
        self.dfs(target, 0, parent_map, visited, ans, K)  #從target TreeNode 向外遍歷
        return ans
        
        
    def buildParentMap(self, node, parent, parent_map):
        if not node:
            return
        parent_map[node] = parent
        self.buildParentMap(node.left, node, parent_map)
        self.buildParentMap(node.right, node, parent_map)
    
    
    def dfs(self, node, distance, parent_map, visited, ans, K):
        if not node or node in visited:   #重要,設立邊界條件還有防止重複遍歷
            return
        visited.append(node)
        if distance == K:
            ans.append(node.val)
        else:
            self.dfs(node.left, distance + 1, parent_map, visited, ans, K)
            self.dfs(node.right, distance + 1, parent_map , visited, ans, K)
            self.dfs(parent_map[node], distance + 1, parent_map, visited, ans, K)

#刷題用這個
#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        parents = {}
        stack = [(root, None)]
        while stack: #dfs iteration 遍歷
            node, parent = stack.pop()
            parents[node] = parent
            if node.left:
                stack.append((node.left, node))
            if node.right:
                stack.append((node.right, node))
        res = []
        visited = set()
        self.dfs(target, 0, parents, res, visited, K)
        return res
    
    def dfs(self, node, distance, parents, res, visited, K):
        if not node or node in visited:
            return 
        visited.add(node)
        if distance == K:
            res.append(node.val)
        else:
            self.dfs(node.left, distance+1, parents, res, visited, K)
            self.dfs(node.right, distance+1, parents, res, visited, K)
            self.dfs(parents[node], distance+1, parents, res, visited, K)





#DFS AND GRAPH METHOD, TIME COMPLEXITY O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def buildParentMap(self, node, parent, parentMap):
        if node is None:
            return
        parentMap[node] = parent
        self.buildParentMap(node.left, node, parentMap)
        self.buildParentMap(node.right, node, parentMap)
        
        
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # node: parent
        parentMap = {}
        
        # DFS to build the map that maps a node to its parent.
        self.buildParentMap(root, None, parentMap)
       
        # keep the records, since the graph is all connected, 這很重要 只能找新node
        visited = set()
        # results
        ans = []
       
        # Again, DFS to retrieve the nodes within the given distance
        #  this time with the help of the parentMap.
        # Starting from the target node
        def dfs(node, distance):
            if node is None or node in visited:
                return
            
            visited.add(node)
            
            if distance == K:
                ans.append(node.val)

            elif distance < K:
                dfs(node.left, distance+1)
                dfs(node.right, distance+1)
                dfs(parentMap[node], distance+1)  #往上追, parentMap在此發揮作用
            # else exceed the scope, no need to explore further
            #dfs fuction run 完會自動return 
        dfs(target, 0)
        
        return ans




















