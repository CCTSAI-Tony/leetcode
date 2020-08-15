'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#跟109,449,105 題一起服用
#自己重寫, time complexity O(n), 刷題用這個, 80ms
#思路: 因為是sorted list, 所以直接取list 的中間值, 左半邊都是比mid小, 右半邊都是比mid大, 符合bst 特性
#dfs 左右子樹, 當作root的 left or right, 左右子樹也是取該區間的中間值當作root, 這樣做出來的bst 才會是height-balanced binary search tree

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        return self.dfs(nums)
    
    def dfs(self, nums):
        if not nums:
            return None
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.dfs(nums[:mid]) #不包含mid, 因為mid 當作root
        root.right = self.dfs(nums[mid+1:])
        return root




 









class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums, 0, len(nums))

    def helper(self, nums, lower, upper):
        if lower == upper:
            return None

        mid = (lower + upper) // 2 #向下取整
        node = TreeNode(nums[mid]) #slice take O(n)
        node.left = self.helper(nums, lower, mid) #passing in bounds
        node.right = self.helper(nums, mid+1, upper) 

        return node #dfs的精髓 就是return

'''
A lot of the Python solutions use slices to split the array; however, it takes O(n) to slice, making the entire algorithm O(n logn). 
Therefore, we create a helper function to pass in the bounds of the array instead, making it O(n):

Please note the if lower == upper: return None statement -- since we are passing in bounds, nums will never be None. 
Therefore, we check if the lower and upper bounds are the same for our base case.

why the time complexity is O(n), isn't it O(logn)? Because you only have to call the recursive function logn times?

Well the slice takes O(n) since you're copying entirely. 
You are right about the recursive function logn calls but O(N) slicing python (look it up) > O(logn) so it's dominated as O(N). =>logn call + O(n) slicing

'''
#using slicing =>logn call * O(n) slicing (每層都有 O(n) slicing)
class Solution:
    # @param num, a list of integers
    # @return a tree node
    # 12:37
    def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) // 2

        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid]) #passing in slicing
        root.right = self.sortedArrayToBST(num[mid+1:])

        return root