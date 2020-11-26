'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. 
Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

# Python solutions, O(n) space and O(1) space, 2 pointers

# The water we trapped depends on the left side and right side which has the max height,
# We keep the left side and right side until we find a higher side


#  刷題用這個,參考別人自己重寫, 此題的monotonic queue 可以存在相等元素且不會刪除裡面的元素, 
#  但其他的monotonic題可能不存在相等元素, 且會從尾or頭刪除不適合元素, 跟著239一起服用
#  O(n) time, O(n) space
#  Given n non-negative integers, 題目有說height 不會是負數, 所以left, right 初始為0即可
#  思路: 先從左邊往右邊建立monotonic queue => height_left, height_left[i] 理解為 height[i] 往左邊遇到最高的牆
#  一樣從右邊往左邊建立monotonic queue => height_right, 最後遍歷height[i], 取左右牆較小的 - height[i] 就是該點能儲的儲水量
class Solution:
    def trap(self, height: List[int]) -> int:
        height_left = []
        height_right = []
        left, right = 0,0
        water = 0
        for i in range(len(height)):
            left = max(left, height[i])
            height_left.append(left)
        for j in range(len(height)-1,-1,-1):
            right = max(right, height[j])
            height_right.append(right)
        height_right.reverse()  #記得height_right 要reverse()
        for i, v in enumerate(height):
            water += min(height_left[i], height_right[i]) - v
        return water

#自己重寫
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = [], []
        max_left = 0
        max_right = 0
        water = 0
        for i in range(len(height)):
            max_left = max(max_left, height[i])
            left.append(max_left)
        for j in range(len(height)-1, -1, -1):
            max_right = max(max_right, height[j])
            right.append(max_right)
        right.reverse()
        for i in range(len(height)):
            water += min(left[i], right[i]) - height[i]
        return water

#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = [], []
        max_left = 0
        max_right = 0
        for i in range(len(height)):
            max_left = max(max_left, height[i])
            left.append(max_left)
        for i in range(len(height)-1, -1, -1):
            max_right = max(max_right, height[i])
            right.append(max_right)
        right.reverse()
        water = 0
        for i in range(len(height)):
            water += min(left[i], right[i]) - height[i]
        return water

class Solution:
# @param A, a list of integers
# @return an integer
    def trap(self, height):
        height_window, left, right, water = [], 0, 0, 0
        for i in arr:
            left = max(left, i)
            height_window.append(left)  #monotonic queue
        height_window.reverse()  #這個重要, 這樣之後倒序height計算right, 就能同步使用
        for n, i in enumerate(reversed(height)):  #從右邊數過來, 倒序
            right = max(right, i)  #右邊牆
            water += min(height_window[n], right) - i  #這裡height_window[n] 當作左邊的牆
        return water






這個有空再看,不難懂 比上面直覺
# O(n) time, O(1)space
class Solution:
# @param A, a list of integers
# @return an integer
    def trap(self, arr):
        left = right = water = 0
        i, j = 0, len(arr)-1
        while i <= j:
            left, right = max(left, arr[i]), max(right, arr[j])
            while i <= j and arr[i] <= left <= right:  #注意是<= 不然都是平面 or 一邊傾斜 則無法進行下去
                water += left - arr[i]
                i += 1
            while i <= j and arr[j] <= right <= left:
                water += right - arr[j]
                j -= 1
        return water