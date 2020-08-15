'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''

# in that problem, the idea is:

# initial sub = [max, max], we use a list of length 2 to store the subsequence, or smaller value which may form the new subsequence.
# traversing the nums：
# a) if val <= sub[0], then we update sub[0] = val.
# b) else if sub[0] < val <= sub[1], the we update sub[1] = val.
# c) else: sub[1] < val, we find a 3 length subsequence. done!
# The key to understanding this solution is if we have found a subsequence of length 2. 
# If the next element is larger than sub[1], then a subsequence of length 3 is found. If the next element is smaller than sub[0] or sub[1], 
# then we find a part of a new subsequence and save it. At the same time, the known subsequence length is 2.

# Here is the solution's track, say we have nums = [9, 7, 10, 1, 8, 9].

# i = 0:    sub = [9, max];
# i = 1:    sub = [7, max];
# i = 2:    sub = [7, 10];
# i = 3:    sub = [1, 10];
# i = 4:    sub = [1, 8];
# i = 5:    sub[1] < 9, done.
# def increasingTriplet(self, nums):
#         sub = [float('inf'), float('inf')]
#         for n in nums:
#             if n <= sub[0]:
#                 sub[0] = n
#             elif n <= sub[1]:
#                 sub[1] = n
#             else:
#                 return True
#         return False
# So back to this question, the idea extends to:

# initial sub = [ ].
# traversing the nums:
# a) if val > sub's all elements, then subsequence length increased by 1, sub.append(val);
# b) if sub[i-1] < val < sub[i], then we find a smaller value, update sub[i] = val. 
# Some of the elements stored in the sub[ ] are known subsequences, and the other part is elements of other possible new subsequences. 
# However, the length of the known subsequences is unchanged.
# return the sub[ ]'s length.
# Here is the solution's track, as we have nums = [8, 2, 5, 1, 6, 7, 9, 3],when we traversing the nums:

i = 0,    sub = [8]
i = 1,    sub = [2] #value < sub[0], replace sub[0]
i = 2,    sub = [2, 5]
i = 3,    sub = [1, 5],    # element has been changed, but the sub's length has not changed.
i = 4,    sub = [1, 5, 6]
i = 5,    sub = [1, 5, 6, 7]
i = 6,    sub = [1, 5, 6, 7, 9]
i = 7,    sub = [1, 3, 6, 7, 9]    #done! Although the elements are not correct, but the length is correct.
# O(n*m) solution. m is the sub[]'s length
# 雙指針解法
# 思路:另存一個sub, 一指針遍歷nums, 另一指針遍歷sub元素(從小到大), 若num > 全部sub, 則添加num至sub
# 若num <= sub元素, 則替換該位置元素換成比較小的num, 最終發現雖然換成比較小的num, sub 有可能不是subsequence了, 但len of increasing subsequence 依舊不變
# 因為換了比較小的元素不影響曾經有這個位置存在的事實
class Solution(object):
    def lengthOfLIS(self, nums):
            sub = []
            for val in nums:
                pos , sub_len = 0, len(sub)
                while(pos <= sub_len):    # update the element to the correct position of the sub via pos += 1 from 0 to sub_len.
                    if pos == sub_len: #val > sub's all elements
                        sub.append(val)
                        break #codes outside while loop
                    elif val <= sub[pos]:
                        sub[pos] = val 
                        break
                    else:
                        pos += 1
            
            return len(sub)

# Because of sub[ ] is incremental, we can use a binary search to find the correct insertion position.

# 模板2, 刷題請用模板1, time complexity O(nlogn), 64ms
# 雙指針解法
# 思路:另存一個sub, 一指針遍歷nums, 另一指針遍歷sub元素(從小到大), 若num > 全部sub, 則添加num至sub => 代表連續增大序列長度+1
# 若num <= sub元素, 則替換該位置元素換成比較小的num, 最終發現雖然換成比較小的num, sub 有可能不是subsequence了, 但len of increasing subsequence 依舊不變
# 因為換了比較小的元素不影響曾經有這個位置存在的事實, 比較小的元素屬於其他的 increasing subsequence(包含比它更小的)
# 這麼做是增加未來的num 成為最長連續序列的可能, 另外在遍歷sub的過程可以使用binary search 來減少複雜度
# 有russian doll envelopes的思想, 更新sub裡面的元素替換比較小的值, 因為之後遇到新元素,比較小的值比較容易連出長sequence
# 可以搭配russian doll envelopes 服用
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sub = [nums[0]]
        for i in range(1,len(nums)):
            pos = self.bs(i, nums, sub)
            if pos == len(sub):
                sub.append(nums[i])
            else:
                sub[pos] = nums[i]
        return len(sub)
    
    def bs(self, i, nums, sub):
        left, right = 0, len(sub)-1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if sub[mid] >= nums[i]:
                right = mid
            else:
                left = mid
        if sub[left] >= nums[i]:
            return left
        elif sub[right] >= nums[i]:
            return right
        return right + 1

 




# 模板1, 刷題用這個
# O(nlogn) solution with binary search
class Solution(object):
    def lengthOfLIS(self, nums):
        sub = []
        for val in nums:
            pos = self.binarySearch(sub, val)
            if pos == len(sub): #val > sub's all elements
                sub.append(val)
            else:
                sub[pos] = val
        return len(sub)  

    def binarySearch(self, sub, val):
            lo, hi = 0, len(sub)-1
            while lo <= hi:
                mid = (lo+hi)//2
                if sub[mid] < val:
                    lo = mid + 1
                elif val < sub[mid]:
                    hi = mid - 1
                else:
                    return mid #出現重複的 ex: sub = [1, 3, 6, 7, 9, 3]
            return lo  
                

            
            
        
#dp 
#這題比較特別在於 increasing subsequence 不在意中間是否沒連續變大
#using dP, dp[i] represents the length of LIS ENDING with nums[i] !!, so for j < i you should check all dp[j] and update dp[i]. 就是這個意思
#time complexity O(n^2), 2008ms
class Solution(object):
    def lengthOfLIS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1]*len(nums)
        for i in range (1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)






