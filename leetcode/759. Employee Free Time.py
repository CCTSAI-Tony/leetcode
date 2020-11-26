'''
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. 
For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  
Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

 

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
 

Constraints:

1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8
'''

#自己想的, time complexity O(nlogn) n: total intervals
#利用min-heap 來對所有intervals 做排序, 初始選定時間最早的interval當作目前佔用period, heap pop 下一個區間, 若下一個區間的start <= 目前佔用區間的end
#代表此兩者之間是沒有空隙的, update 目前佔用區間的end, 若下一個區間的start > 目前佔用區間的end, 代表兩者之間有空隙 => 建立free interval 並放進答案裡
#此下一個區間變成目前佔用period => 重複以上直至所有工作區間都review完畢(heap empty)
import heapq
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        heap = []
        free_intervals = []
        for user in schedule:
            for interval in user:
                heapq.heappush(heap, [interval.start, interval.end])
        period = heapq.heappop(heap)
        while heap:
            new_period = heapq.heappop(heap)
            if new_period[0] > period[1]: #間隔大於0
                free_time = Interval(period[1], new_period[0])
                free_intervals.append(free_time)
                period = new_period #設為新的占用時間
            else:
                period[1] = max(period[1], new_period[1]) #若時間重疊且新佔用時間end > 佔用時間 end, 則update 佔用時間end 
        return free_intervals
