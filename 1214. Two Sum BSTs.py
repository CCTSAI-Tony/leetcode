'''
Given two binary search trees, return True if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

 

Example 1:



Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.
Example 2:



Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false
 

Constraints:

Each tree has at most 5000 nodes.
-10^9 <= target, node.val <= 10^9
'''

#自己想的, time complexity O(n), space complexity O(n) 116ms
#思路: 利用inorder traversal 遍歷兩個bst 來分別建立list, 並把list的元素放進dic, 再遍歷其中一個list, 看是否另一個list的dic有元素一起搭配 = target (two sum proplem)
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        tree1 = []
        tree2 = []
        map1 = {}
        map2 = {}
        self.inorder(root1, tree1)
        self.inorder(root2, tree2)
        for num in tree1:
            map1[num] = num
        for num in tree2:
            map2[num] = num
        for num in tree1:
            if (target - num) in map2:
                return True
        return False
            
        
    def inorder(self, node, array):
        if not node:
            return
        self.inorder(node.left, array)
        array.append(node.val)
        self.inorder(node.right, array)



#別人優化版, 太複雜了, time complexity O(n), space complexity O(n)
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        firstStack = []
        secondStack = []
        tempNode1, tempNode2 = root1, root2
        
        # start with the leftmost node in the first BST
        while tempNode1:
            firstStack.append(tempNode1)
            tempNode1 = tempNode1.left
        
        #start with the rightmost node in the second BST
        while tempNode2:
            secondStack.append(tempNode2)
            tempNode2 = tempNode2.right
        
        # function to get the inorder successor of the first BST
        def findNextNode():
            if not len(firstStack):
                return None
            retNode = firstStack.pop()
            root = retNode.right
            while root:
                firstStack.append(root)
                root = root.left
            return retNode
        
        # function to get the inorder predecessor of the second BST
        def findPrevNode():
            if not len(secondStack):
                return None
            retNode = secondStack.pop()
            root = retNode.left
            while root:
                secondStack.append(root)
                root = root.right
            return retNode
        
        
        firstNode = findNextNode()
        secondNode = findPrevNode()
        
        
        while firstNode and secondNode:
            if firstNode.val + secondNode.val == target:
                return True
            if firstNode.val + secondNode.val > target:
                secondNode = findPrevNode()
            else:
                firstNode = findNextNode()
         
        return False
