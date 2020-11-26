'''
There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. 
Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. 
There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. 
There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. 
The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
'''

Greedy, Python 
Sort intervals by ending value;
Only count valid intervals we need, and skip overlapping intervals => return the count

class Solution(object):
    def findMinArrowShots(self, points):
        points = sorted(points, key = lambda x: x[1])
        res, end = 0, -float('inf')
        for interval in points:
            if interval[0] > end:
                res += 1
                end = interval[1]
        return res


#自己重寫, time complexity O(nlogn) greedy
#思路: 此射箭問題其實就是排序後從左到右遍歷每個區間的end, 因為區間的end代表該區間最後能被箭射到的位置, 也是最後能與其他區間重疊的點(重疊最大化 greedy), 其他區間與之部分重疊都會因這end被射到
#先對points 的end 做排序, 初始設立 interval_end = float("-inf")  
#之後遍歷points, 若points[i][0] > interval_end => end += 1, 更新 interval_end = points[i][1]
#重要: 因為是對end做排序, 所以points[i][0] 沒有> interval_end 的話, 代表該points[i] 區間與interval_end區間依然有重疊
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        interval_end = float("-inf")
        count = 0
        for i in range(len(points)):
            if points[i][0] > interval_end:
                count += 1
                interval_end = points[i][1]
        return count





