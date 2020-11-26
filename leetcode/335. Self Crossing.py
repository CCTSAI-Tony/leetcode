'''
You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, 
then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. 
In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

 

Example 1:

┌───┐
│   │
└───┼──>
    │

Input: [2,1,1,2]
Output: true
Example 2:

┌──────┐
│      │
│
│
└────────────>

Input: [1,2,3,4]
Output: false 
Example 3:

┌───┐
│   │
└───┼>

Input: [1,1,1,1]
Output: true 
'''

# The basic idea is like this:

# When expanding, we never collide.

# When shrinking, we collide when we go back too far. For example, if two steps ago, we went upward for 8, 
# this time we can't go down for more than 7 or it is a collision.

# The tricky part is when transitioning from expanding to shrinking, we may get an early collision!!

class Solution(object):
    def isSelfCrossing(self, x):
        n = len(x)
        x.append(0.5)        # let x[-1] = 0.5, 其實不只0.5 只要任一小於1正數即可, 因為input array 給的都是正整數
        if n < 4: 
            return False
        grow = x[2] > x[0]  #return True
             
        for i in range(3,n):
            if not grow and x[i] >= x[i-2]:  #注意這裡的i從3開始, 不能懂自己畫圖, >= 意思就是剛好碰在線上也算
                return True
            elif grow and x[i] <= x[i-2]:  #注意是<=
                grow = False
                if x[i] + x[i-4] >= x[i-2]:  #當i=3, x[i-4] = x[-1] = 0.5
                    x[i-1] -= x[i-3]  #使下一迴圈return true
        return False


Graph

                                          +------------+
    +---------+                           |            |
    |         |                           |            |
    |         |                           |            |
    |         |                           |            |
    |       i-4  <----+                   |            |
i-2 |         |       |                   |            +
    |         |       |                   |
    |                 |i                  |
    |                 |                   |         <---------------+
    |                 |                   |                         |
    +---------+-------+                   |                         |
              ^                           |                         |
              |                           +-------------------------+
              |


    x[i] + x[i-4] >= x[i-2]                  x[i] + x[i-4] < x[i-2]
    Then, possible early collision,          nothing has to be changed
    pretend we have started from.            however, this time, grow becomes False
    the plus sign point

# when x[3] == x[1], we have to deal with a very special case. 
# So we pretend we have started from a point 0.5 to the left of the origin making this case identical to what we have discussed above.

        1
  +------------+
  |            |
  |            |
  |            |0
  |            |
  |            |
2 |            |
  |            +
  |
  |
  |            ^
  |            |
  |            |
  +------------+
        3


















