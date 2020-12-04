'''
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
'''

#time complexity O(nlogn), space complexity O(1)
#思路: 這跟oa university career fair 一模一樣, greedy => 針對end time 做排序即可, 下一個interval start time > 前一 end time, interval count += 1 => 達成最多non-overlap intervals 
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])
        non_over = 0
        end = float("-inf")
        for interval in intervals:
            if interval[0] >= end:
                non_over += 1
                end = interval[1]
        return n - non_over







        