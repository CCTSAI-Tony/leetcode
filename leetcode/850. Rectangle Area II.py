'''
You are given a 2D array of axis-aligned rectangles. 
Each rectangle[i] = [xi1, yi1, xi2, yi2] denotes the ith rectangle where (xi1, yi1) are the coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner.

Calculate the total area covered by all rectangles in the plane. Any area covered by two or more rectangles should only be counted once.

Return the total area. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:


Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: A total area of 6 is covered by all three rectangales, as illustrated in the picture.
From (1,1) to (2,2), the green and red rectangles overlap.
From (1,0) to (2,3), all three rectangles overlap.
Example 2:

Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 1018 modulo (109 + 7), which is 49.
 

Constraints:

1 <= rectangles.length <= 200
rectanges[i].length == 4
0 <= xi1, yi1, xi2, yi2 <= 109
'''


# 刷題用這個, time complexity O(nlogn), space complexity O(n)
# 思路: segment tree(root node 從 index 1 開始), 搭配 sorted x 的 index => 每個node 對應 x軸的range
# 轉換成y軸掃描線的思路, L.sort() 就能從最底的y線 掃到最高的
class SegmentTree:
    def __init__(self, xs):
        self.cnts = collections.defaultdict(int)
        self.totals = collections.defaultdict(int)
        self.xs = xs
        self.xs_i = {x:i for i, x in enumerate(xs)}
    def update(self, node, low, high, start, end, diff):
        if low >= end or high <= start:  # l, r 都使用mid, 所以 high <= start 也return 0, 因為另一個node區間不會miss mid
            return 0
        if start <= low and high <= end:
            self.cnts[node] += diff
        else:
            mid = low + (high - low) // 2
            l = self.update(node*2, low, mid, start, end, diff)
            r = self.update(node*2+1, mid, high, start, end, diff)
        if self.cnts[node] > 0:  #就算update 左右子區間, 但自身 self.cnts[node] > 0, 可以無視左右子區間的結果, ex: 小矩形被大矩形包圍
            self.totals[node] = self.xs[high] - self.xs[low] # node 區間長度 => x寬度
        else:
            self.totals[node] = self.totals[node*2] + self.totals[node*2+1]  #若self.cnts[leaf_node] <= 0, leaf node 會再看空node = 0, leaf_node*2 & leaf_node*2+1
        return self.totals[node]

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        st = SegmentTree(xs)
        L = []
        for x1, y1, x2, y2 in rectangles:
            L.append([y1, 1, x1, x2])
            L.append([y2, -1, x1, x2])
        L.sort()  # 重要! 這樣才能y2 - y1, 底邊先出, 頂邊後出
        cur_y = cur_x_sum = area = 0
        
        for y, sig, x1, x2 in L:
            area += (y - cur_y) * cur_x_sum
            cur_y = y
            st.update(1, 0, len(st.xs)-1, st.xs_i[x1], st.xs_i[x2], sig)
            cur_x_sum = st.totals[1]
            
        return area % (10 ** 9 + 7)

