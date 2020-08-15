class Solution(object):
    def removeElement(self, nums, val):
        start, end = 0, len(nums) - 1 # tuple
        while start <= end:
        	if nums[start] == val:
        	   nums[start], nums[end], end = nums[end], nums[start], end - 1 #似 pop()
        	else: 
        		start +=1
        return start

        '''
        a = Solution()
        a.removeElement([0,1,2,2,3,0,4,2],2)
        [0, 1, 4, 0, 3, 2, 2, 2]
        start = 5
        
        '''