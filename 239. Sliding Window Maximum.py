'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
'''


# Solution Using Dequeue: O(N)

# Very similar code structure to heap solution
# http://yuanhsh.iteye.com/blog/2190852
# https://docs.python.org/2/library/collections.html#collections.deque
# Add to dequeue at tail using the rule where you pop all numbers from tail which are less than equal to the number. 
# Think why? 300->50->27 and say 100 comes. 50 and/or 27 can never be the maximum in any range.
# When you do the above, the largest number is at head. But you still need to test if front is within the range or not.
# Pop or push each element at-max once. O(N)
# *So, to maintain the queue in order,

# When moves to a new number, iterate through back of the queue, removes all numbers that are not greater than the new one, and then insert the new one to the back.
# findMax only need to take the first one of the queue.
# To remove a number outside the window, only compare whether the current index is greater than the front of queue. If so, remove it.*


#刷題用這個, monotonic queue, 搭配862服用
#自己重寫, time com[lexity O(n), 重點建立一個decreasing monotonic queue
# 思路: 此題最重要就是額外建立一個deque, 隨著window移動, 加入新的數字進去, 若新的數字大於前面已加入了, 就把前面已加入的pop掉, 因為他們沒機會變成此window的最大值
# 直到遇到比你大的, 這樣可以確保這個dq[0]是整個dq最大的值
# dq 裡面是紀錄index, 之後dq[0] 還要確認是否它的index還在window 裡, 若沒有則pop掉它, 換次小的變dq[0], 直到dq[0] 在window裡
# 使用此一操作可以以平均O(1)取得window裡最大的值, 而不像naice algorithm, 需要O(k)
# 每個數字被append, 與 pop掉 個別最多一次, 因此time complexity 為 O(n)
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        for i in range(k-1):
            self.helper(nums, i, dq)
        res = []
        start, end = 0, k-1
        for end in range(k-1, len(nums)):
            self.helper(nums, end, dq)
            while dq[0] < start:
                dq.popleft()
            res.append(nums[dq[0]])
            start += 1 #固定長度的slinding window 要隨著end 往右移
        return res
        
    
    def helper(self, nums, i, dq):
        while dq and nums[i] >= nums[dq[-1]]:  #記住這邊是>=, =的情況就是比較後面的index來update比較前面的
            dq.pop()
        dq.append(i)



#naive algorithm, O(nk)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return None
        res = []
        for i in range(k-1, len(nums)):
            window = nums[i-(k-1):i+1]
            res.append(max(window))
        return res






from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        dq = deque()
        for i in range(k):  #建立初始window for dq
            self.add_to_dq(dq, nums, i)
        result, start, end = [], 0, k-1
        while end < len(nums):
            while True: #while true 用法: 保持迴圈持續, 所以迴圈內需要break 來跳脫
                if dq[0] >= start:  #確認最大值的index是否在window裡
                    result.append(nums[dq[0]])
                    break #脫離while True 迴圈, 往下走
                else:
                    dq.popleft() #已離開window, 最大值換人
            start, end = start+1,end+1
            if end < len(nums):
                self.add_to_dq(dq, nums, end) #add new number
        return result

    def add_to_dq(self, dq, nums, i):
        while len(dq) and nums[dq[-1]] <= nums[i]: #pop all numbers from tail which are less than equal to the comming number, 確保deque第一個都是最大的
            dq.pop()
        dq.append(i) #append index
        return #return for 迭代, 其實有無這一行都不影響結果,只是為了readability, 預設: code跑完就會return









