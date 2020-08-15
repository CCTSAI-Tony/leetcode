# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

# You're given the startTime , endTime and profit arrays, 
# you need to output the maximum profit you can take such that there are no 2 jobs in the subset with overlapping time range.

# If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

# Example 1:



# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job. 
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
# Example 2:




# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job. 
# Profit obtained 150 = 20 + 70 + 60.
# Example 3:



# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6
 

# Constraints:

# 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
# 1 <= startTime[i] < endTime[i] <= 10^9
# 1 <= profit[i] <= 10^4

# Explanation
# Sort the jobs by endTime.

# dp[time] = profit means that within the first time duration,
# we cam make at most profit money.
# Intial dp[0] = 0, as we make profit = 0 at time = 0.

# For each job = [s, e, p], where s,e,p are its start time, end time and profit,
# Then the logic is similar to the knapsack problem.
# If we don't do this job, nothing will be changed.
# If we do this job, binary search in the dp to find the largest profit we can make before start time s.
# So we also know the maximum cuurent profit that we can make doing this job.

# Compare with last element in the dp,
# we make more money,
# it worth doing this job,
# then we add the pair of [e, cur] to the back of dp.
# Otherwise, we'd like not to do this job.


# Complexity
# Time O(NlogN) for sorting
# Time O(NlogN) for binary search for each job
# Space O(N)


Python:

    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])  #sorted by endtime, 這很重要
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1 
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]

# 注意 i = bisect.bisect(dp, [s + 1]) - 1, 為什麼是[s + 1], 因為若我們插入比較的時候是[s], 但dp裡面元素是 [[e,p]], tuple的第二個元素是空, 導致sort的過程中
# 會被插入在同為一樣的[e, ] 的最左邊, 且之後再-1 就會得到錯誤的i, 因此選擇插入[s+1], 會插在[s,] 的右邊, 但在[s+1,x] 的最左邊, 這樣一來 -1 的index就是 [s,max]
# 但這有bug, 若起始與初始時間不是int, 而是 float, 那 s + 1, 則有可能跳過一些元素, 因此選擇插入 [s, float("inf")] 會更保險一點
# 為什麼一開始jobs 要sorted by endtime, 因為 dp[i][1] + p > dp[-1][1], 若不sorted by endtine, dp[-1][0] 可能不是相等或小於的end time, 比較會錯亂
# 還有我們建立dp時是要依照end time 排序的, 不然之後 i = bisect.bisect(dp, [s + 1]) - 1 會錯亂

# 這個在floating point 可以work才是對的
# 思路 dp[time][-1] = profit means that within the time duration, we cam make at most profit money, 隨著endtime 上升的buttom up
class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])  #sorted by endtime, 這很重要
        dp = [[0, 0]]
        for (s, e, p) in jobs:
            i = bisect.bisect(dp, [s, float("inf")]) -1  
            if dp[i][1] + p > dp[-1][1]:   # dp[i][1] 代表 the previous largest profit we can make 
                dp.append([e, dp[i][1] + p])  #不斷append 的 dp, endtime 回逐步增加, 因為依照此排序
        return dp[-1][1]



# 1. bisect(list, num, beg, end) :- This function returns the position in the sorted list, 
# where the number passed in argument can be placed so as to maintain the resultant list in sorted order. 重要
# If the element is already present in the list, the right most position where element has to be inserted is returned. 
# This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, 
# ending position which has to be considered.

# 2. bisect_left(list, num, beg, end) :- This function returns the position in the sorted list, 
# where the number passed in argument can be placed so as to maintain the resultant list in sorted order. 
# If the element is already present in the list, the left most position where element has to be inserted is returned. 
# This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, 
# ending position which has to be considered.

# 3. bisect_right(list, num, beg, end) :- This function works similar to the “bisect()” and mentioned above.


import bisect 
  
# initializing list 
li = [1, 3, 4, 4, 4, 6, 7] 
  
# using bisect() to find index to insert new element 
# returns 5 ( right most possible index ) 
print ("The rightmost index to insert, so list remains sorted is  : ", end="") 
print (bisect.bisect(li, 4)) 
  
# using bisect_left() to find index to insert new element 
# returns 2 ( left most possible index ) 
print ("The leftmost index to insert, so list remains sorted is  : ", end="") 
print (bisect.bisect_left(li, 4)) 
  
# using bisect_right() to find index to insert new element 
# returns 4 ( right most possible index ) 
print ("The rightmost index to insert, so list remains sorted is  : ", end="") 
print (bisect.bisect_right(li, 4, 0, 4)) 

print ("The rightmost index to insert, so list remains sorted is  : ", end="") 
print (bisect.bisect_right(li, 4)) 

Output:

The rightmost index to insert, so list remains sorted is  : 5
The leftmost index to insert, so list remains sorted is  : 2
The rightmost index to insert, so list remains sorted is  : 4
The rightmost index to insert, so list remains sorted is  : 5














