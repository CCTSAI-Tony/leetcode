'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

#題目條件 Given a set of non-overlapping interval
#自己重寫 time complexity O(n)
#思路: 利用指針 來遍歷 intervals 是否有部分or全部 重疊 new interval [start, end], 若有就merge起來, 更新 [start, end]
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = newInterval[0]
        end = newInterval[1]
        res = []
        for i in range(len(intervals)):
            if intervals[i][1] < start:  #start > intervals[i][1] 代表 new interval 與 interval[i][1] 有gap, 不能merge
                res.append(intervals[i])
                continue
            elif intervals[i][1] >= start:
                if intervals[i][0] > end:  #代表 merged interval end 與 interval[i][0] 有gap, 無法merge, 提早結束
                    res.append([start, end]) #先append 到目前已經merged的 interval or new interval(無merged)
                    res += intervals[i:]  #加入剩下 無法merged 的 interval
                    return res
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
        res.append([start, end])  #重要! 一路merge 到最後, 記得要加回 merged interval
        return res








# O(n) Python solution
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = newInterval[0]
        end = newInterval[1]
        result = []
        i = 0
        while i < len(intervals):
            if start <= intervals[i][1]:
                if end < intervals[i][0]:  #代表 merged interval end 與 interval[i][0] 有gap, 不能merge了, break
                    break #out of while loop,
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
            else:  #start > intervals[i][1] 代表 newinterval 與 interval[i][1] 有gap, 不能merge
                result.append(intervals[i])
            i += 1
        result.append([start, end])  #加入merged interval
        result += intervals[i:]  #加入之後未merged 的interval
        return result