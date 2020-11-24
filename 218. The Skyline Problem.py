'''
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. 
Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), 
write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], 
where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, 
and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. 
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] 
that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, 
where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. 
Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. 
For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; 
the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
'''
# time complexity O(n^2), n: len(buildings) => heapq.heapify
# 思路: 此題利用heap 來紀錄目前skyline的高度, max_heap
# 並使用sort 來對starts, ends, 進行個別排序, 都是x 越小排愈前, 相同x: starts => 愈高排愈前, ends => 愈矮排愈前 (都是為了維持天際線)
# 合併start, end, x 越小排愈前, 相同x: start 優先ends, 利用指針遍歷合併triplets, 來更新heap(高度)
# 矮的房子end, 但天際線還在, 所以不recor點, 高的房子start 超越現有天際線, record點, 若高的房子end, 導致heap的最高點變矮, record點
import heapq 
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        starts = []
        ends = []
        for x,y,h in buildings: #拆分starts, ends
            starts.append((x,h,'s'))
            ends.append((y,h,'e'))
        # sort starts by x and -1*height
        starts.sort(key=lambda x : (x[0], -1*x[1])) #x小的優先,h高的優先
        # sort ends by x and height
        ends.sort(key=lambda x:(x[0],x[1])) #x小的優先,h矮的優先(這樣才能使得最高的最後一個remove, 不然最後結束那條垂直線會有很多點)
        # combine the 2 and sort by x but starts has priority to ends
        temp = sorted(starts+ends, key = lambda x: (x[0], -1 *ord(x[2])))# x小的優先, -1 *ord(x[2] start 優先 end
        
        heap = [0] #起始高度為0
        output=[]
        for i, (x, h, t) in enumerate(temp):
            max_heap = -1*heap[0] #heap[0]會回傳最小的,所以heapq.heappush(heap, -1*h), -1*h 來使最高h會被優先回傳, *-變正值
            if t == 's':
                if h>max_heap:
                    output.append([x,h])
                heapq.heappush(heap, -1*h) #heapq.heappush 自動幫你調整heap 排序
            else:
                heap.remove(-1*h) #remove one element of the same height for the start,不要搞混 不會消除全部值相同的element 只消除list裡離左邊最近的
                heapq.heapify(heap) #重新heap排序一下
                if -1*heap[0]!=max_heap: #前一個building end 後高度有變化, record 該點
                    output.append([x,-1*heap[0]])
        return output


#自己重寫, time complexity O(n^2)
import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        starts = []
        ends = []
        for start, end, h in buildings:
            starts.append([start, h, "s"])
            ends.append([end, h, "e"])
        starts.sort(key=lambda x: (x[0], -x[1]))
        ends.sort(key=lambda x: (x[0], x[1]))
        
        temp = sorted(starts + ends, key=lambda x: (x[0], -ord(x[2])))
        res = []
        heap = [0]
        for x, h, t in temp:
            max_heap = -heap[0]
            if t == "s":
                if h > max_heap:
                    res.append([x, h])
                heapq.heappush(heap, -h)
            elif t == "e":
                heap.remove(-h)
                heapq.heapify(heap)
                if max_heap != -heap[0]:
                    res.append([x, -heap[0]])
        return res


#重寫第二次, time complexity O(n^2), space complexity O(n)
import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        start, end = [], []
        for s, e, h in buildings:
            start.append((s, h, "s"))
            end.append((e, h, "e"))
        start.sort(key=lambda x: (x[0], -x[1]))
        end.sort(key=lambda x: (x[0], x[1]))
        temp = sorted(start + end, key=lambda x: (x[0], -ord(x[2])))
        heights = []
        res = []
        for t, h, w in temp:
            max_h = -heights[0] if heights else 0
            if w == "s":
                if h > max_h:
                    res.append((t, h))
                heapq.heappush(heights, -h)
            elif w == "e":
                heights.remove(-h)
                heapq.heapify(heights)
                new_height = -heights[0] if heights else 0
                if max_h > new_height:
                    res.append((t, new_height))
        return res





# my implementation of the idea explianed here: https://www.youtube.com/watch?v=GSBLe8cKu0s

# a = [9,8,7,6,5,4,3,2,1]
# a.sort()
# a
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a.sort(key = lambda x: -x)
# a
# [9, 8, 7, 6, 5, 4, 3, 2, 1]

# import heapq 
# heap = [0]
# heapq.heappush(heap, 2)
# heap
# [0, 2]

# a = [1,4,3,2,5,7,6,8,9]
# heapq.heapify(a)
# a
# [1, 2, 3, 4, 5, 7, 6, 8, 9]

# b = [1,1,1,1,1,1,1,1]
# b.remove(1)
# b
# [1, 1, 1, 1, 1, 1, 1]


# 当待排序列表的元素由多字段构成时，我们可以通过sorted(iterable，key，reverse)的参数key来制定我们根据那个字段对列表元素进行排序。
# 　　key=lambda 元素: 元素[字段索引]
# 　　例如：想对元素第二个字段排序，则
# 　　key=lambda y: y[1] 备注：这里y可以是任意字母，等同key=lambda x: x[1]
# 看几个简单的例子。

# listA = [3, 6, 1, 0, 10, 8, 9]
# print(sorted(listA))

# listB = ['g', 'e', 't', 'b', 'a']
# print(sorted(listB))
# print(sorted(listB, key=lambda y: y[0]))

# listC = [('e', 4), ('o', 2), ('!', 5), ('v', 3), ('l', 1)]
# print(sorted(listC, key=lambda x: x[1]))
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# #结果一
# [0, 1, 3, 6, 8, 9, 10]
# #结果二
# ['a', 'b', 'e', 'g', 't']
# ['a', 'b', 'e', 'g', 't']
# #结果三
# [('l', 1), ('o', 2), ('v', 3), ('e', 4), ('!', 5)]





