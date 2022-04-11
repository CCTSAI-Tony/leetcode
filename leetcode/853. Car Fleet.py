'''
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. 
The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

 

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.
Example 2:

Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, hence there is only one fleet.
Example 3:

Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
 

Constraints:

n == position.length == speed.length
1 <= n <= 105
0 < target <= 106
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 106
'''


# https://leetcode.com/problems/car-fleet/discuss/255589/Python-Code-with-Explanations-and-Visualization-Beats-95

'''
1. Sort the vehicles by the (pos, vel) pair.
2. Since the first vehicle will always lead a fleet, starting from the second vehicle, 
compare each vehicle's ideal arrival time with the arrival time of the fleet in front of it, 
i.e., stack[-1]. If its ideal arrival time is earlier, it will join the fleet in front of it. Otherwise, 
it will lead a new fleet and we append its arrival time into stack.
3. Finally, stack contains the arrival times of the fleets and the length of stack will be the number of distinct arrival times, i.e., the number of fleets.
'''

# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: 使用stack, 先對(position, speed) sort, 並從尾遍歷, 計算arrive 到終點的時間, 與stack[-1] 前一台車的抵達時間比較, 若比它早 就會相撞合併, 不納入stack, else, 加入stack
# 答案就是len(stack)
class Solutions:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for pos, vel in sorted(zip(position, speed))[::-1]:
            dist = target - pos
            if not stack:
                stack.append(dist / vel)
            elif dist / vel > stack[-1]:
                stack.append(dist / vel)
        return len(stack)

# 重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for pos, speed in sorted(zip(position, speed))[::-1]:
            dis = target - pos
            arrive_time = dis / speed
            if not stack:
                stack.append((pos, speed, arrive_time))
            else:
                prev_arrive_time = stack[-1][2]
                if arrive_time > prev_arrive_time:
                    stack.append((pos, speed, arrive_time))
        return len(stack)





































