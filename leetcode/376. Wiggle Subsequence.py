'''
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. 
The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. 
In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, 
the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. 
A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, 
leaving the remaining elements in their original order.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
Example 3:

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?
'''


# python O(n) time O(1) space, easy to understand, 這題就是在求有幾處轉折+2
class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        length = 1
        up = None # current is increasing or not
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and up != True:
                length += 1
                up = True
            if nums[i] < nums[i - 1] and up != False:
                length += 1
                up = False
        return length


#Greedy, the longest wiggle subsequence always ends with the up trend's or down trend's last character! ex [1,17,5,15,5,16,8]

# 示例如下[12,64,50,50,41,21,22,17]
# 建立一个树，若前节点和现在节点冲突的话：相同则扔掉，否则将现在节点与前节点放入同一层，比如50、41、21
#      12
#       |
#      64
#     / | \
#   50 41 21 #冲突层，含有多个节点
#          |
#         22
#          |
#         17
# 注意到，这个树在冲突层时，取最小的值(或最大的值)会更好
# 所以，我们把树更新为线性表，若前节点和现在节点冲突，则表明现在节点更符合要求，把前节点指向现在节点
#      12
#       |
#      64
#       |
#      21 (放弃50、41) #冲突层，含有多个节点
#       |
#      22
#       |
#      17

# Python O(N) DP with 9 lines of readable code, memorize sign

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        sign, length = -(nums[1]-nums[0]), 1
        for i in range(1, len(nums)):
            dif = nums[i] - nums[i-1]
            if dif * sign < 0 or (sign==0 and dif!=0):  #dif * sign < 0 代表轉折, sign==0 and dif!=0 防止 ex [1,1,17,5,15,5,16,8]
                sign = dif
                length += 1
        return length



















