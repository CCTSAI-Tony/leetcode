# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

 



# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

# Example:

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49


class Solution(object):
    def maxArea(self, height):
        l,area, r = 0, 0, len(height) - 1
        while l < r:  
            if height[l] < height[r]: 
                area = max(height[l] * (r - l), area)
                l += 1
            else: 
                area = max(height[r] * (r - l), area)
                r -= 1
        return area


#  自己想重新寫, time complexity O(n), 刷題用這個
#  思路: 利用左右2 pointer, 來移動左右長度比較短的一邊, 期望移動後長度變長, 原長邊變短邊計算後的水體積才會變多
#  why 不移動大邊, 移動大邊結果一定不會比之前結果來得大, 移動小邊體積才有可能增加
#  兩邊長度都一樣, 此時先移右還是左, 都不會影響最後結果, 畫個圖就清楚
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        water = 0
        while left < right:
            water = max(water, min(height[left],height[right])*(right-left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return water


#自己重寫, 概念一樣
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        water = 0
        left, right = 0, len(height) - 1
        left_height, right_height = height[0], height[len(height)-1]
        while left < right:
            water = max(water, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                while left < right and height[left] <= left_height:
                    left += 1
                left_height = height[left]
            else:
                while left < right and height[right] <= right_height:
                    right -= 1
                right_height = height[right]
                
        return water





