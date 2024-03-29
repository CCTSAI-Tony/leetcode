'''
A car travels from a starting position to a destination which is target miles east of the starting position.

There are gas stations along the way. 
The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. 
When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

 

Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).
Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
 

Constraints:

1 <= target, startFuel <= 109
0 <= stations.length <= 500
0 <= positioni <= positioni+1 < target
1 <= fueli < 109
'''

'''
Intuition

When driving past a gas station, let's remember the amount of fuel it contained. 
We don't need to decide yet whether to fuel up here or not - for example, there could be a bigger gas station up ahead that we would rather refuel at.

When we run out of fuel before reaching the next station, we'll retroactively fuel up: greedily choosing the largest gas stations first.

This is guaranteed to succeed because we drive the largest distance possible before each refueling stop, and therefore have the largest choice of gas stations to (retroactively) stop at.

Algorithm

pq ("priority queue") will be a max-heap of the capacity of each gas station we've driven by. We'll also keep track of tank, our current fuel.

When we reach a station but have negative fuel (ie. we needed to have refueled at some point in the past), 
we will add the capacities of the largest gas stations we've driven by until the fuel is non-negative.

If at any point this process fails (that is, no more gas stations), then the task is impossible.
'''

# 刷題用這個, time complexity O(nlogn), space complexity O(n)
# 思路: 使用priority queue 搭配 greedy 來解題, 經過加油站不管如何先放入priority queue, 等到沒油時再從裡面pop出最多油的, ans += 1
import heapq
class Solution(object):
    def minRefuelStops(self, target, tank, stations):
        pq = []  # A maxheap is simulated using negative values
        stations.append((target, float('inf')))

        ans = prev = 0
        for location, capacity in stations:
            tank -= location - prev
            while pq and tank < 0:  # must refuel in past
                tank += -heapq.heappop(pq)
                ans += 1
            if tank < 0: 
                return -1
            heapq.heappush(pq, -capacity)
            prev = location

        return ans


# 重寫第二次, time complexity O(nlogn), space complexity O(n)
import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        queue = []
        tank = startFuel
        prev = 0
        ans = 0
        stations.append([target, float("inf")])
        for location, fuel in stations:
            tank -= location - prev
            while queue and tank < 0:
                tank += -heapq.heappop(queue)
                ans += 1
            if tank < 0:
                return -1
            prev = location
            heapq.heappush(queue, -fuel)
        return ans

