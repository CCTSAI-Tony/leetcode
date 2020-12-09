'''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''
#此題node 有可能是負數
#刷題用這個 # O(n) extra space, time complexity O(n), as we just traverse once
#思路: If within this path, there is a valid solution, then there must be a oldPathSum such that currPathSum - oldPathSum = target.
#use cache to store path, once traversed all the childs of this branch, reduce cache[path]-= 1, cause no more child path use this old_path
class Solution(object):
    def pathSum(self, root, sum):
        # define global result and path
        self.result = 0
        cache = {0:1}  #currentsum = 0, frequency = 1, 初始值重要!
        
        # recursive to get result
        self.dfs(root, sum, 0, cache)
        
        # return result
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return  
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 非常重要
        cache[currPathSum] -= 1  #代表這支線都已遍歷完畢


#自己重寫 time complexity O(n), space complexity O(n)
from collections import defaultdict
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        cache = defaultdict(int)
        cache[0] = 1
        self.res = 0
        self.dfs(root, cache, 0, sum)
        return self.res
    
    def dfs(self, node, cache, path, sum):
        if not node:
            return
        path += node.val
        old_path = path - sum
        self.res += cache[old_path]
        cache[path] += 1
        self.dfs(node.left, cache, path, sum)
        self.dfs(node.right, cache, path, sum)
        cache[path] -= 1


#重寫第二次, time complexity O(n), space complexity O(n)
from collections import defaultdict
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        memo = defaultdict(int)
        memo[0] = 1 #關鍵
        self.count = 0
        self.dfs(root, memo, 0, sum)
        return self.count
        
    def dfs(self, node, memo, curSum, target):
        if not node:
            return
        curSum += node.val
        temp = curSum - target
        self.count += memo[temp]
        memo[curSum] += 1
        self.dfs(node.left, memo, curSum, target)
        self.dfs(node.right, memo, curSum, target)
        memo[curSum] -= 1





# Python step-by-step walk through. Easy to understand. Two solutions comparison. 

# 1. Brute Force: O(nlogn) ~ O(n^2)
# 1.1 High level walk-through:
# (Define return) Define a global var: self.numOfPaths in the main function.
# (1st layer DFS) Use recursive traverse to go through each node (can be any order: pre, in, post all fine).
# (2nd layer DFS) For each node, walk all paths. If a path sum equals to the target: self.numOfPaths += 1
# Return result: return self.numOfPaths
# 1.2 Complexity analysis
# 1.2.1 Space
# Space complexity is O(1), due to there is no extra cache. However, for any recursive question, we need to think about stack overflow, 
# namely the recursion should not go too deep.
# Assume we have n TreeNodes in total, the tree height will vary from O(n) (single sided tree) to O(logn)(balanced tree).
# The two DFS will go as deep as the tree height.
# 1.2.2 Time
# Time complexity depends on the two DFS.
# 1st layer DFS will always take O(n), due to here we will take each node out, there are in total n TreeNodes
# 2nd layer DFS will take range from O(n) (single sided tree) to O(logn)(balanced tree). 
# This is due to here we are get all the paths from a given node. The length of path is proportional to the tree height.
# Therefore, the total time complexity is O(nlogn) to O(n^2).

# 暴力解!! time complexity O(nlogn) to O(n^2), => O(n) (single sided tree) to O(logn)(balanced tree)
# 思路: dfs 每個node, 並在每個node 都test把自己當root的路徑是否 == target
class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # define global return var
        self.numOfPaths = 0
        # 1st layer DFS to go through each node
        self.dfs(root, target)
        # return result
        return self.numOfPaths
    
    # define: traverse through the tree, at each treenode, call another DFS to test if a path sum include the answer
    def dfs(self, node, target):
        # exit condition
        if node is None:
            return 
        # dfs break down 
        self.test(node, target) # you can move the line to any order, here is pre-order, root,left,right
        self.dfs(node.left, target)
        self.dfs(node.right, target)
        
    # define: for a given node, DFS to find any path that sum == target, if find self.numOfPaths += 1
    def test(self, node, target):
        # exit condition
        if node is None:
            return
        if node.val == target:
            self.numOfPaths += 1
            
        # test break down
        self.test(node.left, target-node.val)
        self.test(node.right, target-node.val)




# 2. Memorization of path sum: O(n)
# 2.1 High level walk through
# In order to optimize from the brutal force solution, we will have to think of a clear way to memorize the intermediate result. 
# Namely in the brutal force solution, we did a lot repeated calculation. For example 1->3->5, we calculated: 1, 1+3, 1+3+5, 3, 3+5, 5.
# This is a classical 'space and time tradeoff': we can create a dictionary (named cache) which saves all the path sum (from root to current node) and their frequency.
# Again, we traverse through the tree, at each node, we can get the currPathSum (from root to current node). 
# If within this path, there is a valid solution, then there must be a oldPathSum such that currPathSum - oldPathSum = target.
# We just need to add the frequency of the oldPathSum to the result.
# During the DFS break down, we need to -1 in cache[currPathSum], because this path is not available in later traverse.
# Check the graph below for easy visualization.

# 2.2 Complexity analysis:
# 2.2.1 Space complexity
# O(n) extra space

# 2.2.1 Time complexity
# O(n) as we just traverse once
































































