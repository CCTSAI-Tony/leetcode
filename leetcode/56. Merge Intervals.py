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


# 自己重寫 time complexity O(nlogn)
# 思路: 先排序intervals, 並對前一個區間尾比較看是否要被merge, 並看情況update merge後該區間的尾
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return None
        intervals.sort(key = lambda x: (x[0], x[1]))  #這邊sort 可以不用sort到 x[1]
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if res[-1][1] >= interval[0]: #重疊到了
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res


#重寫第二遍, time complexity O(nlogn), space complexity O(1)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res




# Facebook Follow-Up
# Question: How do you add intervals and merge them for a large stream of intervals? (Facebook Follow-up Question)

# Inspired by https://leetcode.com/problems/merge-intervals/discuss/21452/Share-my-interval-tree-solution-no-sorting

# We need to have two functions for the tree (add interval and query tree).

# Implementation Details
# TreeNode - On top of the left child, right child, start boundary, and end boundary, 
# we have a middle field that determines whether a new interval goes to the left child, right right or merged with the current node.

# add - If the new interval touches or crosses the middle of the current node, we update the current node. Otherwise, 
# we put the new interval into the left subtree or right subtree.

# Why do we use middle for comparison and not start or end boundaries?
# The reason is that we can use merge-sort technique to query the merged intervals result when the left subtree does not overlap with the right subtree.
# query - Use merge-sort technique by retrieving the merged intervals of the left subtree (i.e. left_intervals) 
# and those of the right subtree (i.e. right_intervals). Because of the implementation of add, we can guarantee that

# if there's an interval in the left_intervals that overlaps with the current node, then we know that all the intervals after that interval overlaps with the current node.
# The first few intervals or zero intervals in the right_intervals overlap with the current node.
# Here's the visualization:

# left_res = [ (intervals that do not overlap), (intervals that overlap with current node) ]
# right_res = [ (intervals that overlap with current node), (intervals that do not overlap) ]
# Code

#不難懂, time complexity O(nlogn), space complexity O(n), or we can use heap method
class TreeNode:
    def __init__(self, start, end, middle):
        self.start = start
        self.end = end
        self.middle = middle
        self.left = self.right = None

class Solution:
    def __init__(self):
        self.root = None
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        for start, end in intervals:
            if not self.root:
                self.root = TreeNode(start, end, (start + end) // 2)
            else:
                self.add(self.root, start, end)
        
        return self.query(self.root)
    
    
    def add(self, node, start, end):     
        if end < node.middle:
            if node.left:
                self.add(node.left, start, end)
            else:
                node.left = TreeNode(start, end, (start + end) // 2)
        
        elif start > node.middle:
            if node.right:
                self.add(node.right, start, end)
            else:
                node.right = TreeNode(start, end, (start + end) // 2)
        
        else:
            node.start = min(node.start, start)
            node.end = max(node.end, end)
    
    def query(self, node):
        if not node:
            return []
        
        # merge-sort divide and conquer
        left_intervals = self.query(node.left)
        right_intervals = self.query(node.right)
        res = []
        
        inserted = False
        
        for lres in left_intervals:
            if lres[1] < node.start:
                res.append(lres)
            else:
                res.append([min(lres[0], node.start), node.end])
                inserted = True
                break
        
        if not inserted:
            res.append([node.start, node.end])
        
        for rres in right_intervals:
            if rres[0] <= node.end:
                res[-1][1] = max(node.end, rres[1])
            else:
                res.append(rres)
        
        return res







