'''
Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

 

Example 1:


Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]
Example 2:

Input: root = [1], target = 0.000000, k = 1
Output: [1]
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104.
0 <= Node.val <= 109
-109 <= target <= 109
'''

# time complexity O(n), worst case O(n^2), space complexity O(n)
# 思路: quick select, pivot 為 pivot index的值 與target的距離
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        def partition(pivot_idx, left, right):
            pivot_dist = dist(pivot_idx)
            
            # 1. move pivot to end
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
            store_idx = left
            
            # 2. move more close elements to the left
            for i in range(left, right):
                if dist(i) < pivot_dist:
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1
                    
            # 3. move pivot to its final place
            nums[right], nums[store_idx] = nums[store_idx], nums[right]
            
            return store_idx
            
        def quickselect(left, right):
            """
            Sort a list within left..right till kth less close element
            takes its place.
            """
            # base case: the list contains only one element
            if left == right:
                return 
            
            # select a random pivot_index
            pivot_idx = randint(left, right)
            
            # find the pivot position in a sorted list
            true_idx = partition(pivot_idx, left, right)
            
            # if the pivot is in its final sorted position
            if true_idx == k:
                return
            
            if true_idx < k:
                # go right
                quickselect(true_idx, right)
            else:
                # go left
                quickselect(left, true_idx)
        
        nums = inorder(root)
        dist = lambda idx : abs(nums[idx] - target)
        quickselect(0, len(nums) - 1)
        return nums[:k]


# 重寫第二次, time complexity O(n), O(n^2) worst, space complexity O(n)
import random
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
            
        def partition(pivot_idx, left, right):
            pivot_dist = dist(pivot_idx)
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
            store_idx = left
            for i in range(left, right):
                if dist(i) < pivot_dist:
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1
            nums[right], nums[store_idx] = nums[store_idx], nums[right]
            return store_idx
        
        def quickselect(left, right):
            if left == right:
                return
            pivot_idx = random.randint(left, right)
            true_idx = partition(pivot_idx, left, right)
            if true_idx == k:
                return
            elif true_idx < k:
                quickselect(true_idx, right)
            else:
                quickselect(left, true_idx)
            
        nums = inorder(root)
        dist = lambda idx: abs(nums[idx] - target)
        quickselect(0, len(nums) - 1)
        return nums[:k]
