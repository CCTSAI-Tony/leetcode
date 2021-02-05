'''
Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exactly middle of the first row it can be put. 
The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). 
You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. 
The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, 
you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. 
However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.
Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]
Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
Example 3:
Input:
      1
     / \
    2   5
   / 
  3 
 / 
4 
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
Note: The height of binary tree is in the range of [1, 10].
'''

#刷題用這個, time complexity O(h*2^h), space complexity O(h*2^h) We need to fill the resres array of size h * 2^h - 1  Here, hh refers to the height of the given tree.
#2^h - 1 是list 的長度, 有h層 => 所以最差要填滿 h * (2^h - 1) 個坑
#思路: 先取得樹高得知list長度, 再利用遞迴與node在特定區間正中間的特性, 把lists填滿
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def get_height(node):
            return 0 if not node else 1 + max(get_height(node.left), get_height(node.right))
        
        def update_output(node, row, left, right):
            if not node:
                return
            mid = (left + right) / 2
            self.output[row][mid] = str(node.val)
            update_output(node.left, row + 1 , left, mid - 1)
            update_output(node.right, row + 1 , mid + 1, right)
            
        height = get_height(root)
        width = 2 ** height - 1
        self.output = [[''] * width for i in range(height)]
        update_output(node=root, row=0, left=0, right=width - 1)
        return self.output



#重寫第一次, time complexity O(h * (2**h - 1)), space complexity O(h * (2**h - 1))
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def get_height(node):
            return 0 if not node else 1 + max(get_height(node.left), get_height(node.right))
        
        def fill_positions(node, height, left, right):
            if not node:
                return 
            mid = left + (right - left) // 2
            self.rows[height][mid] = str(node.val)
            fill_positions(node.left, height + 1, left, mid - 1)
            fill_positions(node.right, height + 1, mid + 1, right)
            
        h = get_height(root)
        self.rows = [[""] * (2 ** h - 1) for _ in range(h)]
        fill_positions(root, 0, 0, 2 ** h - 2) # 2 ** h - 2 => zero based index issue
        return self.rows



