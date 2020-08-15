'''
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, 
plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. 
Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
'''
#自己想的, dfs time complexity O(mn)
#思路: 往相同pixal 擴散, 被擴散的cell 改成 newColor, 這裡要注意的是以為改成newColo 就能充當visited 防止重複遍歷
#事實上不正確, 若newColor 跟origin_pixal 值一樣 則還是會重複遍歷
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = set()
        origin_p = image[sr][sc]
        self.dfs(sr,sc,newColor, origin_p, image, visited)
        return image
    
    def dfs(self, i, j, newColor, origin_p, image, visited):
        m, n = len(image), len(image[0])
        if 0 <= i < m and 0 <= j < n and image[i][j] == origin_p and (i, j) not in visited:
            visited.add((i, j))
            image[i][j] = newColor
            for x, y in [(i+1, j),(i-1, j),(i, j+1),(i, j-1)]:
                self.dfs(x, y, newColor, origin_p, image, visited)








