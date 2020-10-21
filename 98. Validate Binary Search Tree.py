'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

#   node.val            lowerbound, upperbound
    #      5                    -inf, inf
    #    /   \                 /         \
    #   3      8          -inf,5         5,inf
	#  /  \               /     \
    # 1    7(invalid)   -inf,3   3,5(node.val = 7 > upperbound = 5)


# 經典題, 刷題用recursion  
# recursion, preorder traversal time complexity O(n)
# 思路: 利用preorder traversal, root,left,right, 把當前node的val 設成boundary 給左右子樹, 若子樹node超過這個boundary就是False
# 注意binary search tree 在此題是不允許duplicate node, 所以符合 node.left.val < root.val < root.right.val
class Solution(object):
	def isValidBST(self, root: TreeNode) -> bool:
		return self.dfs(root, float('-inf'), float('inf')) #預先給很小與很大值 記得使用float() 裡面是'inf' or '-inf'

    def dfs(self, node, lower, upper): #這裡def dfs()裡面沒包含self 因為非直接在class下面
            if not node: #遍歷完了
                return True
            if node.val >= upper or node.val <= lower: #注意>= <=
                return False
            return self.dfs(node.left, lower, node.val) and self.dfs(node.right, node.val, upper)

 # iteration, preorder
class Solution(object):
	def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]  #先放入初始item
        while stack:
            cur_node, lower, upper = stack.pop() #依序pop
            if cur_node.val <= lower or cur_node.val >= upper:
                return False
            if cur_node.left: #不為none時
                stack.append((cur_node.left, lower, cur_node.val)) #更新upper
            if cur_node.right:
                stack.append((cur_node.right, cur_node.val, upper)) #更新lower
        return True #全部遍歷完了

'''
General Idea: Keep track of the lowerbound and upperbound of the current node, update the lowerbound and upperbound when we reach left/right child

'''
'''
stack = [('cur_node', float('-inf'), float('inf'))]
cur_node, lower, upper = stack.pop()
print(cur_node)
print(lower)
print(upper)

cur_node
-inf
inf

def tt():
    return True and False

tt()

False


'''





















