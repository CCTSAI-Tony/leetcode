'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10
'''

# The stack maintain the indexes of buildings with ascending height. Before adding a new building pop the building who is taller than the new one. 
# The building popped out represent the height of a rectangle with the new building as the right boundary and the current stack top as the left boundary. 
# Calculate its area and update ans of maximum area. Boundary is handled using dummy buildings.

# 解釋超詳細
# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/452612/Thinking-Process-for-Stack-Solution
# https://abhinandandubey.github.io/posts/2019/12/15/Largest-Rectangle-In-Histogram.html

# time complexity O(n)
#刷題用這個, time complexity O(n), space complexity O(n)
#思路: 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) #這個重要, 遍歷完height 最後強迫回算留在stack 的遞增序列, stack pop的高度當作rectangle的高度
        stack = [-1] #python 技巧, 這個重要, 當作while loop 的終止條件 => heights[-1] = 0
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        return ans


#刷題用這個, stack, time complexity O(n), 比上面straightforward
#思路: 利用stack 來存遞增height, 直到指針遍歷到height[i] < height[stack[-1]] 代表之後無法以height[stack[-1]] 當作h 形成rectangle
#因此使用while loop 來處理stack 裡面的height, > height[i] 都要被pop 出來 計算以該值當作h的rectangle 的面積, w則是i 與 pop後 stack[-1] 中間的區域, 畫個圖就清楚了
#因為height[i] 比 heights[stack.pop()] 小, heights[stack[-1]] 比 heights[stack.pop()] 小(遞增序列), w的區間就是這樣計算出來的
#遍歷完heights後, 若還殘留stack 利用while loop 來回算stack裡面height 形成的面積, 因為後面沒有height了
#此時的height 都是以該stack[前一個] 到 len(height)可以用height來當作h形成rectangle, 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                if stack:
                    w = i-stack[-1]-1
                else:
                    w = i #zerobased index issue
                max_area = max(max_area, h*w)
            stack.append(i)
        if stack:
            while stack:
                h = heights[stack.pop()]
                if stack:
                    w = n-stack[-1]-1 #n, 因為已經超過array了
                else:
                    w = n
                max_area = max(max_area, h*w)
        return max_area











