'''
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

 

Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:


Input: root = [2,1,1]
Output: [[1]]
Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
 

Constraints:

The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200
'''
# why preorder doesn't work in this solution?

# It is post-order because we must first know the serialization of a node's left subtree and right subtree, 
# before we can get its own serialization.. pre-order simply cannot achieve that

# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: 關鍵是使用postorder traversal 加上 tree_string
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.tree_str_count, self.result = collections.defaultdict(int), []
        self.postorder(root)
        return self.result
    
    def postorder(self, node):
        """
        :type node: TreeNode
        :rtype: str
        """
        if not node:
            return '#'
        tree_str = str(node.val) + ',' + self.postorder(node.left) + ',' + self.postorder(node.right)
        if self.tree_str_count[tree_str] == 1:
            self.result.append(node)
        self.tree_str_count[tree_str] += 1
        return tree_str


# 重寫第二次, time complexity O(n), space complexity O(n)
from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        memo = defaultdict(int)
        ans = []
        def postorder(node):
            if node == None:
                return "#"
            tree_string = str(node.val) + "," + postorder(node.left) + "," + postorder(node.right)
            if memo[tree_string] == 1:
                ans.append(node)
            
            memo[tree_string] += 1
            return tree_string
        postorder(root)
        return ans

