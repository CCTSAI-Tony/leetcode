'''

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


a=[[1,7],[2,6],[8,10],[15,18]]
sorted(a, key = lambda i: i[1])

[[2, 6], [1, 7], [8, 10], [15, 18]]

Both list.sort() and sorted() have a key parameter to specify a function to be called on each list element prior to making comparisons.

student_tuples = [
...     ('john', 'A', 15),
...     ('jane', 'B', 12),
...     ('dave', 'B', 10),
... ]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

'''

class Solution(object):
    def merge(self, intervals:List[List[int]]):
        out = []
        for i in sorted(intervals, key=lambda i: i[0]):
            if out and i[0]<=out[-1][-1]:        #a=[[1,7],[2,6],[8,10],[15,18]]= [[1, 7], [8, 10], [15, 18]] <=要注意！
                out[-1][-1] = max(out[-1][-1], i[-1])  #deal with overlaped 
            else: out+=[i]
        return out


# 自己重寫 time complexity O(n)
# 思路: 先排序intervals, 並對前一個區間尾比較看是否要被merge, 並看情況update merge後區間的尾
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return None
        intervals.sort(key = lambda x: (x[0], x[1]))  #這邊sort 可以不用sort到 x[1]
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res


