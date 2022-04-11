'''
There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:

positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
speedi is the initial speed of the ith car in meters per second.
For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. 
Once a car collides with another car, they unite and form a single car fleet. 
The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.

Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. 
Answers within 10-5 of the actual answers are accepted.

 

Example 1:

Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]
Explanation: After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. 
After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.
Example 2:

Input: cars = [[3,4],[5,4],[6,3],[9,1]]
Output: [2.00000,1.00000,1.50000,-1.00000]
 

Constraints:

1 <= cars.length <= 105
1 <= positioni, speedi <= 106
positioni < positioni+1
'''

'''
Sample:
If we have: [[1,2],[2,1],[4,3],[7,2]]:
Iterate from the end:

Consider car [7, 2]. It will never collide with its next car, because there is no car.

stack: [(7, 2, math.inf)] (third element in the tuple is the collision time)
result: [-1]
Consider car [4, 3]. 3 > 2 (current car and head of the stack speeds), so they will collide. Find collision time as (7 - 4) / (3 - 2) = 3. 3 < math.inf , 
so it will collide sooner than head of the stack. Add current car to the stack.

stack: [(7, 2, math.inf), (4, 3, 3)]
result: [-1, 3]
Consider [2, 1].
3.1. 1 < 3 (current car and head of the stack speeds), they won't collide. Discard head of the stack.

stack: [(7, 2, math.inf)]
result: [-1, 3]
3.2. 1 < 2 (current car and head of the stack speeds), they won't collide. Discard head of the stack. Stack will be empty, so add current car to it with no collision time.

stack: [(2, 1, math.inf)]
result: [-1, 3, -1]
Consider [1, 2]. 2 > 1. They will collide. Collision time: (2 - 1) / (2 - 1) = 1. 1 < math.inf , so add current car to the stack.

stack: [(2, 1, math.inf), (1, 2, 1)]
result: [-1, 3, -1, 1]

The last base case sample:
stack: [(5, 1, math.inf), (3, 3, 1)]
current car: (1, 4)
Collision time: (3 - 1) / (4 - 3) = 2 . But 2 > 1 (more than collision time of the head), so we can discard the head.

This results into O(N) time complexity and O(N) space complexity.
(The internal while cycle runs at most N times, because we do stack.pop() there)
'''


# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: 使用stack, 從後面遍歷, 解題似monotonous queue 
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        result = []
        # cars that might collide with current car
        stack = []
        for position, speed in cars[::-1]:
            # if current car speed is less than the head of the stack then there won't be a collision
            # or if c1 collides with c2 after c2 collides with c3, we can ignore c2 and find collision time of c1 and c3 instead
            # (where c1 is current car, c2 is the head of the stack and c3 is the car that c2 will collide with)
            # (if we have [[x1, s1], [x2, s2]], then collision time is (x2 - x1) / (s1 - s2))
            while stack and (speed <= stack[-1][1] or (stack[-1][0] - position) / (speed - stack[-1][1]) >= stack[-1][2]):
                stack.pop()
            # if stack is empty, then current car will never collide with the next car
            if not stack:
                stack.append((position, speed, math.inf))
                result.append(-1)
            # find collision time and add the car to the stack
            else:
                collideTime = (stack[-1][0] - position) / (speed - stack[-1][1])
                stack.append((position, speed, collideTime))
                result.append(collideTime)
        result.reverse()
        return result

# 重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        stack = []
        res = []
        for pos, speed in cars[::-1]:
            while stack and (speed <= stack[-1][1] or (stack[-1][0] - pos) / (speed - stack[-1][1]) >= stack[-1][2]):
                stack.pop()
            if not stack:
                stack.append((pos, speed, float("inf")))
                res.append(-1)
            else:
                coll_time = (stack[-1][0] - pos) / (speed - stack[-1][1])
                stack.append((pos, speed, coll_time))
                res.append(coll_time)
        return res[::-1]








