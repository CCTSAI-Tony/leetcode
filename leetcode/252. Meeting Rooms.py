'''
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106

'''

#自己想的, time complexity O(nlogn), space complexity O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True


# 重寫第二次, time complexity O(nlogn), space complexity O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        pre_end = -1
        for interval in intervals:
            start, end = interval[0], interval[1]
            if start < pre_end or end < pre_end:
                return False
            pre_end = end
        return True




def binary_search(array, target):           
    start, end = 0, len(array) - 1          
    while start + 1 < end:          
        mid = (start + end) / 2         
        if array[mid] == target:            
            start = mid         
        elif array[mid] < target:           
            start = mid         
        else:           
            end = mid           
            
    if array[start] == target:          
        return start            
    if array[end] == target:            
        return end          
    return -1           

