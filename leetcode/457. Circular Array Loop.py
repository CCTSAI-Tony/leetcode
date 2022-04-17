'''
You are given a circular array nums of positive and negative integers. If a number k at an index is positive, then move forward k steps. Conversely, 
if it's negative (-k), move backward k steps. Since the array is circular, you may assume that the last element's next element is the first element, 
and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in nums. A cycle must start and end at the same index and the cycle's length > 1. 
Furthermore, movements in a cycle must all follow a single direction. In other words, a cycle must not consist of both forward and backward movements.

 

Example 1:

Input: [2,-1,1,2,2]
Output: true
Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.
Example 2:

Input: [-1,2]
Output: false
Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because the cycle's length is 1. By definition the cycle's length must be greater than 1.
Example 3:

Input: [-2,1,-1,-2,-2]
Output: false
Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle, because movement from index 1 -> 2 is a forward movement, 
but movement from index 2 -> 1 is a backward movement. All movements in a cycle must follow a single direction.
 

Note:

-1000 ≤ nums[i] ≤ 1000
nums[i] ≠ 0
1 ≤ nums.length ≤ 5000
 

Follow up:

Could you solve it in O(n) time complexity and O(1) extra space complexity?
'''

python 1 pointer O(n) time O(1) space
not a real O(1) space solution if modifying input is not allowed.

class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 2:
            return False
        
        n = len(nums)
        for i in range(n):           
            if type(nums[i]) != int: # visited element, 被mark過
                continue
            if nums[i] % n == 0: # self-loop
                continue
            
            direction = (nums[i] > 0) # loop direction, cannot be changed midway, return True or False
            
            mark = str(i)  #string 當下的index
            while (type(nums[i]) == int) and (direction ^ (nums[i] < 0)) and (nums[i] % n != 0):
                jump = nums[i]
                nums[i] = mark
                i = (i + jump) % n  #circular
                
            if nums[i] == mark:  #回到當初的index, 完成circle
                return True
            
        return False

#  (direction ^ (nums[i] < 0))  =>  xor, 要一true 一false => true, 因此若中間換方向, 變成True ^ True or False ^ False => False


#  自己重寫 python 1 pointer 
#  time complexity O(n),  space complexity O(1) 
#  not a real O(1) space solution if modifying input is not allowed.
#  思路: 利用單指針check nums[i] 是否self loop cycle's length == 1, 並mark nums[i] = str(i) (visited)
#  若有circle 任何一個member 在這circle的都可以回到自己的index, 然而不能形成單一方向 circle的元素就mark起來, 防止再度遍歷
#  題目有說, cycle 裡的成員只能有一個方向
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 2:
            return False
        
        n = len(nums)
        for i in range(n):
            if type(nums[i]) != int:  # visited element, 被mark過
                continue
            if nums[i] % n == 0:  # self-loop
                continue
            
            direction = nums[i] < 0  # loop direction, cannot be changed midway, return True or False
            
            mark = str(i)  #string 當下的index
            
            while type(nums[i]) == int and (nums[i] < 0) == direction and nums[i] % n != 0:
                jump = nums[i]
                nums[i] = mark  #代表一個記號, 同屬一個circle 的 mark
                i = (i + jump) % n
            
            if nums[i] == mark: #代表回到一樣的mark, 形成一個circle
                return True
        
        return False


























