'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''
#time time complexity O(nlogn)
#思路: 先對intervals 依start time 做排序, 並依此順序來check heap 裡面是否有空房, 若沒有就push 該endtime 進 heap, 代表開新房間
#利用heap 來存放每個room 的end time, 若有新會議就查看heap[0]的會議結束時間是否能在新會議開始前結束, 若可以就能把這個會議室讓給新會議使用, 不需額外開房間
#若無法就開新房間,並push end time to heap, 因為minheap, heap[0] 會回報最小的 endtime, 最後return len(heap) 代表總共開新幾個房間
#技巧: heapq.heapreplace 取代heap 最top的item
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        heap = []  # stores the end time of intervals
        for i in intervals:
            if heap and i[0] >= heap[0]:  #new meeting start time is >=  the earlist end time of rooms in heap
                # means two intervals can use the same room
                heapq.heapreplace(heap, i[1]) #也可以 heapq.heappushpop(heap, i[1]), 因為 i[0] >= heap[0]
            else:
                # a new room is allocated
                heapq.heappush(heap, i[1])
        return len(heap)


#自己重寫 time complexity O(nlogn)
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort(key=lambda x: x[0])
        for i in intervals:
            if heap and i[0] >= heap[0]:
                heapq.heapreplace(heap, i[1])
            else:
                heapq.heappush(heap, i[1])
        return len(heap)

#重寫第二次, time complexity O(nlogn), space complexity O(n)
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        heap = []
        for interval in intervals:
            if not heap or interval[0] < heap[0]:
                heapq.heappush(heap, interval[1])
            else:
                heapq.heapreplace(heap, interval[1])
        return len(heap)


# heapq.heapreplace(heap, item)
# Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change. If the heap is empty, IndexError is raised.

# This one step operation is more efficient than a heappop() followed by heappush() and can be more appropriate when using a fixed-size heap. 
# The pop/push combination always returns an element from the heap and replaces it with item.

# The value returned may be larger than the item added. If that isn’t desired, consider using heappushpop() instead. 
# Its push/pop combination returns the smaller of the two values, leaving the larger value on the heap.