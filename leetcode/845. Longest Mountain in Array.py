'''
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
'''
# Follow up

# Can you solve this problem with only one pass?
# Can you solve this problem in O(1) space?

# In this solution, I count up length and down length. 刷題用這個
# Both up and down length are clear to 0 when A[i - 1] == A[i] or down > 0 && A[i - 1] < A[i](下坡又上升).
# time complexity O(n), space complexity O(1), one pass solution
#  思路: 先上升再下降才能成為山, 利用指針向右遍歷元素, 若前一個比自己小, up + 1, 比自己大 down - 1, 若跟前一個一樣, up,down 歸0, 若已經下坡但又比前一個大, up,down 歸0

class Solution:
    def longestMountain(self, A):
        res = up = down = 0
        for i in range(1, len(A)):
            if down and A[i - 1] < A[i] or A[i - 1] == A[i]:  #若已經down了, 又上升 or 遇到相等的元素, back to default 重新計算
                up = down = 0
            up += A[i - 1] < A[i]  # A[i - 1] < A[i] => True = 1
            down += A[i - 1] > A[i]
            if up and down:  #若同時有上升還有下降 計算山的長度, 記得+1 山峰要算進去
                res = max(res, up + down + 1)
        return res

# a = 0
# a += (4<5)
# a
# 1
# a += (4<5)
# a
# 2

#自己重寫
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        up = 0
        down = 0
        max_len = 0
        for i in range(1, len(A)):
            if A[i] == A[i-1] or (down and A[i] > A[i-1]):
                up = 0
                down = 0
            if A[i] > A[i-1]:
                up += 1
            
            if A[i] < A[i-1]:
                down += 1
                
            if up and down:
                max_len = max(max_len, up+down+1)
        return max_len



#自己想的 Time complexity O(n), space complexity O(n), 3 Passes O(2N) Space
#  思路: 利用雙指針從左到右, and 從右到左 分別建立A[i] 左邊or 右邊 有多少連續遞增or 遞減的元素, 左邊加右邊加自己就是山的長度
#  注意, 若其中一邊連續遞增or遞減元素是0, 那A[i]就不能成為山峰
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        ascToRight = [0] * len(A)
        ascToLeft = [0] * len(A)
        for right in range(1, len(A)):
            if A[right] > A[right-1]:
                ascToRight[right] = ascToRight[right-1] + 1
        
        for left in range(len(A)-2,-1,-1):
            if A[left] > A[left + 1]:
                ascToLeft[left] = ascToLeft[left+1] + 1
        max_len = 0
        
        for i in range(len(A)):
            if ascToRight[i] == 0 or ascToLeft[i] == 0:
                continue
            mountLength = ascToRight[i] + ascToLeft[i] + 1
            max_len = max(max_len, mountLength)
        return max_len




 

#相同想法, 人家精煉解法, 利用zip
class Solution:
    def longestMountain(self, A):
        up, down = [0] * len(A), [0] * len(A)
        for i in range(1, len(A)):
            if A[i] > A[i - 1]: 
                up[i] = up[i - 1] + 1
        for i in range(len(A) - 1)[::-1]:
            if A[i] > A[i + 1]: 
                down[i] = down[i + 1] + 1
        return max([u + d + 1 for u, d in zip(up, down) if u and d] or [0])

# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# c = [x for x in zip(a,b)]
# c
# [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
# c = [i+j for i,j in zip(a,b) if i < 9 and j < 9]
# c
# [7, 9, 11]













