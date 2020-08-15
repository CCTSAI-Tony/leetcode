'''
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
'''


https://leetcode.com/problems/minimum-time-difference/discuss/474787/Python3-O(nlogn)-time-with-detailed-explanation-%3A)


'''
This problem is actually quite a brain teaser if you haven't worked much with circular algorithms. It's actually a really fun problem!

Let's consider the distances of all the points here. The distance from p1 to p3 is equal to abs(24:00 - 22:04 + 1:30). 
The distance from p1 to p2 is equal to abs(1:30 - 10:46). The distance from p2 to p3 is abs(10:46 - 22:04). In general, 
if we consider two points that are within (including) 12 hours of eachother and there's no crossing over the 0th hour, 
the calculation is straight forward and just abs (a-b). It gets complicated though in the other events. 
So how do we account for a distance greater than 12? Well, it means from the point which is larger, 
we need to do 24:00 - max(a,b) + min(a,b). The 24:00 - max(a,b) part offsets the max point back to 0, 
and then the min(a,b) part will get you to the destination. 
Therefore, we can conclude the general formula, dist(a,b) = min(abs(a - b), abs(24 - max(a,b) + min(a,b)). 
    We can just now, for each point compare it to every other point and calculate the distance, getting the min. 
    This would be a operation performed (n-1) + (n-2) + (n-3) + ... + 1 times, and thus, total time compelxity is O(n^2)

As you probably guessed, we can do better! There's a serious flaw with what what we're doing. For each point, 
we are barbarically looking at every single point and calculating the distance, but there's a good fact we can take advantage of. 
Consider the diagram. Suppose we wanted to find the minimum distance between p1, p2, and p3. 
For each given point, we can find the closest point for each by looking both left and right and selecting the first element we see. 
To better illustrate this, consider this instead.


The closest point, is always, no matter what, is either the first elment looking clockwise or counter clockwise. 
Looking at any other point is redundant, because they cannot possibly be the closest. Furthermore, 
we can reduce this to just have every element look clockwise, because the element behind it will calculate the distance in it's ccw direction when it looks cw.

However, we can only guarantee this will work if we have our points sorted, and this is where the O(nlogn) complexity comes from. So, our new algorithm is:

1. Convert each time to minutes. O(n).
2. Sort the list of minutes. O(nlogn).
3. Calculate the distance from p[i] to p[i+1] for all i except p[n-1] where n is the length of the times array. O(n).
4. Calculate the distance of the final point to it's first CW element, which will cross 0. This is the point in which there would be a revolution loop. O(1).

At each step between 3 and 4, minDist = min(current, new).
'''

# https://leetcode.com/problems/minimum-time-difference/discuss/474787/Python3-O(nlogn)-time-with-detailed-explanation-%3A)
# time complexity O(nlogn), n: len(timePoints)
# 思路: 先把每個時間轉化成分鐘, 然後排序! 除了第一個-最後1個時間另外算(circular), 其他時間點間隔都可以從下一個時間點-前一個時間點
# 這題很棒! The input time is legal and ranges from 00:00 to 23:59. 每個點都是順時鐘到下一點, 因此只有最後一點需要特別處理
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i, time in enumerate(timePoints):
            timePoints[i] = self.toMin(time)  #in-place modify
        
        res = sys.maxsize  #最大值
        timePoints.sort() #重要! 排序
        for i in range(0, len(timePoints) - 1): #calculate the closest CW distance of each element except last
            res = min(res, (timePoints[i+1] - timePoints[i]))
        
        res = min(res, 60* 24 - timePoints[-1] + timePoints[0]) #calc final point
        
        return res

    def toMin(self, time):
        time = time.split(':')
        res = (60*int(time[0])) + int(time[1])
        return res





































