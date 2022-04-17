'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique. !!只有單一解 所以取最低點
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
'''

# 重寫第二次, time complexity O(n)m space complexity O(1)
# 思路: greedy, 尋找油量最小值的點
# 走完一遍以后，油量增加 => 一定能找到解
# 走完一遍以后油量不变 => 这种情况下， 解存在，即 “周期函数一定有最大值和最小值。 只要从最小值出发，永远不会低于初值。”
# 走完一遍以后油量减少 => 一定无解
# input => gas [5], cost [4] => 就會導致 min_gas_loc = None, 因為走一圈回來, 油量增加了
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        min_gas, min_gas_loc = 0, 0  # 先預設起點油量最少
        tank = 0
        for i in range(len(gas)):
            tank += (gas[i] - cost[i])
            if tank <= min_gas:
                min_gas = tank
                min_gas_loc = i + 1
        return min_gas_loc % len(gas)




'''
横轴为加油站的序号，纵轴为油箱油量。允许油箱油量为负，假设走完一遍以后油量不变，那画出来的图就是周期函数，想像sine函數
每隔一定周期回到原点。如果从这个周期函数的最小值出发，可以保证油箱油量不为负，即有解。不知道这样说有没有说清楚。:)

假设把无穷多个加油站排在一起。 规定只能往右。从0开始计算这个无穷的序列上每个点的剩余油量，剩余量允许为负数。
有解的情况等价于， 从某个位置i开始， 连续n个位置的剩余量不小于位置i的剩余量。

会有三种情况：

走完一遍以后，油量增加 => 一定能找到解
走完一遍以后油量不变 => 这种情况下， 解存在，即 “周期函数一定有最大值和最小值。 只要从最小值出发，永远不会低于初值。”
走完一遍以后油量减少 => 一定无解
'''

class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        min_gas, min_gas_loc = 0, None
        for i in range(len(gas)):
            tank += gas[i] - cost[i] #位置i+1 初始油量
            if tank < min_gas: #注意這邊沒有等於
                min_gas = tank
                min_gas_loc = i + 1
        return 0 if min_gas_loc is None else (min_gas_loc ) % len(gas) #永遠取初始油量最低的, % len(gas) 防止在最後一個 => i + 1 >= n, circle

'''
First, you definitely cannot complete the trip if there is more gas required than gas given. That is pretty obvious.

The tricky part is to realize that if you plan carefully, you definitely can complete the trip if there is at least as much gas given as needed.

So how do you pick where to start? First, each station will either give you a gas surplus 
(if it requires less gas to go to the next station than it has at the station), or a gas deficit 
(if it's the other way around). So your total gas supply either rises or shrinks as you pass through each station 
(draw a curve yourself. It will look like a movement of a stock). The most difficult part of the trip is when your gas supply continues to shrink. 
Now assume your gas can go negative, and you have to start from station 0, the most difficult time is when your gas supply is the lowest (most negative). 
The trick is to pick the station right after the most difficult time. Then your gas always stays positive!


gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
tank = [0,-2,-4,-6,-3] 位置初始油量(未加油前)

備註: 有解狀況油量不為負, 所以取最低點, 其他點相對它都是正

'''
x = 4
x+= 5-3
x
6
























