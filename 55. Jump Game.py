class Solution:
    def canJump(self, nums):
        max_reach, n = 0, len(nums)
        for i, x in enumerate(nums):
            if max_reach < i: return False  #[1,1,0,2,3]
            if max_reach >= n - 1: return True
            max_reach = max(max_reach, i + x) #所在位置加值 [1,3 ,0,2,3]


'''
[1,2,3,0,1,0,0,4]
'''

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        stepsLeft = nums[0]

        if not stepsLeft and len(nums) > 1: #例如[0,1,2]
            return False

        for num in nums[1:-1]:
            stepsLeft = max(stepsLeft - 1, num) #為啥減一 確保[1,1,1,1,1] 能不斷跳 像[1,1,1,0,1]就會failss
            if not stepsLeft:
                return False

        return True

'''
method2
'''