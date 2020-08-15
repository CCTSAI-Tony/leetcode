'''
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. 
Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Constraints:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
'''

Algorithm

This is an extremely tricky problem.
The main idea is to schedule the most frequent tasks as frequently as possible. Begin with scheduling the most frequent task. 
Then cool-off for n, and in that cool-off period schedule tasks in order of frequency, or if no tasks are available, then be idle.
Exampe: Say we have the following tasks: [A,A,A,B,C,D,E] with n =2
Now if we schedule using the idea of scheduling all unique tasks once and then calculating if a cool-off is required or not, 
then we have: A,B,C,D,E,A,idle,idle,A i.e. 2 idle slots.
But if we schedule using most frequent first, then we have:
2.1: A,idle,idle,A,idle,idle,A
2.2: A,B,C,A,D,E,A i.e. no idle slots. This is the general intuition of this problem.
3.The idea in two can be implemented using a heap and temp list. This is illustrated in the code below.
4.Time complexity is O(N * nlogN) where N is the number of tasks and n is the cool-off period.
5.Space complexity is O(1) => will not be more than O(26).



from heapq import heappush, heappop
from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        total_interval, heap = 0, []
        for k,v in Counter(tasks).items():
            heappush(heap, (-1*v, k))
        while heap:
            i, temp = 0, []
            while i < n + 1:  #why i < n + 1, 因為還要包含開頭元素ex; A INTERVAL INTERVAL, n = 2
                total_interval += 1
                if heap:
                    x,y = heappop(heap)
                    if x != -1:  #若x= -1 代表只剩最後一個count, 無需加入temp再push back 至heap
                        temp.append((x+1,y))  #用掉一個count, 因此x + 1
                #if-else 是一組的       
                if not heap and not temp:  #完成所有程序
                    break  #out of while i <= n loop
                else:
                    i += 1  #不管是否加idle還是拿其他元素塞, interval + 1
            if temp:  #這句多餘, 但為了好理解     
                for item in temp:
                    heappush(heap, item)  #push back to heap
        return total_interval

#  if not heap and temp 代表需要加入idle的時候, 就算not heap, 但冷凍期沒走完就要加入idle使其填滿



# Time complexity is O(N * nlogN) where N is the number of tasks and n is the cool-off period.
# Space complexity is O(1) => will not be more than O(26).
# 自己重寫, 刷題用這個
# 思路: 依頻率高低優先填入period, 若元素不夠則填入idle, 在period裡面元素都是不重複的
# 若count 相同, heap 預設以字母順序排序, 因此新period元素都會與舊period隔n個interval
from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        total_interval = 0
        for i, v in Counter(tasks).items():
            heapq.heappush(heap, (-v, i))
        
        while heap:
            period = 0  # task interval interval, n= 2, period = 3, 滿足period 則開啟新的period
            temp = []
            while (heap or temp) and period < n + 1:  #只要heap or temp 其中一個不為None 代表tasks 沒有完全執行完
                total_interval += 1
                period += 1
                if heap:  #若heap還有元素則pop元素填充period, 若沒有則用idle 填充
                    (i, v) = heapq.heappop(heap)
                    if i != -1:
                        temp.append((i+1, v))
            
            for item in temp:
                heapq.heappush(heap, item)
            
        return total_interval












