'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). 
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.

Example 1:
Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:
Input: 
asteroids = [8, -8]
Output: []
Explanation: 
The 8 and -8 collide exploding each other.
Example 3:
Input: 
asteroids = [10, 2, -5]
Output: [10]
Explanation: 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
Example 4:
Input: 
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
Note:

The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..
'''

#自己想的, time complexity O(2n) => O(n), 100ms
#思路: 利用stack 來儲存asteroids, 當目前asteroid < 0 and stackp[-1] > 0, 才會發生碰撞
#碰撞後設一變數 explode 來代表碰撞後asteroid是否消失, 若沒消失after while loop 加到stack, 若消失換下一個asteroid
#使用while loop 來連續碰撞stack裡面 > 0 的asteroid, 若stack[-1] < abs(asteroid) => stack.pop() 直到stack[-1] < 0 or asteroid 自爆 or stack is empty
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
                continue
            elif asteroid < 0:
                explode = False
                while stack and stack[-1] > 0:
                    if abs(asteroid) > stack[-1]:
                        stack.pop()
                    elif abs(asteroid) < stack[-1]:
                        explode = True
                        break
                    else:
                        stack.pop()
                        explode = True
                        break
                if not explode:
                    stack.append(asteroid)
        return stack



#別人的解法, time complexity O(N)
#思路: while else 的組合, 若不執行while loop 就執行else
class Solution(object):
    def asteroidCollision(self, asteroids):
        res = []
        for asteroid in asteroids:
            while res and asteroid < 0 and res[-1] > 0:
                if res[-1] == -asteroid: 
                    res.pop()
                    break
                elif res[-1] < -asteroid:
                    res.pop()
                    continue #到下一個while loop interation, 若不符合while 條件 就執行else
                elif res[-1] > -asteroid:
                    break
            else:
                res.append(asteroid)
        return res









