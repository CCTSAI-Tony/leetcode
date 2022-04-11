'''
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

 

Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
'''

# 刷題用這個, time complexity: O(n), space complexity O(logn)
# 思路: 使用dfs 來遍歷整個tree, 利用 isParentExist 來判斷subtree是否加入到res, recursion back 時, 再對左右tree 剪枝
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []
        def delete(node, isParentExist):
            if not node:
                return None
            node.left = delete(node.left, node.val not in to_delete)
            node.right = delete(node.right, node.val not in to_delete)
            if node.val in to_delete:
                return None
            if not isParentExist:
                res.append(node)
            return node
        delete(root, False)
        return res


# 重寫第二次, bfs, time complexity: O(n), space complexity O(n)
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        queue = deque([(root, False)])
        res = []
        while queue:
            for _ in range(len(queue)):
                node, hasParent = queue.popleft()
                if not hasParent and node.val not in to_delete:
                    res.append(node)
                child_has_parent = node.val not in to_delete
                
                if node.left:
                    queue.append((node.left, child_has_parent))
                    if node.left.val in to_delete:
                        node.left = None
                        
                if node.right:
                    queue.append((node.right, child_has_parent))
                    if node.right.val in to_delete:
                        node.right = None 
        return res





