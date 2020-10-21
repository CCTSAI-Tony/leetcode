'''
A conveyor belt has packages that must be shipped from one port to another within D days.

The i-th package on the conveyor belt has a weight of weights[i].  
Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 
We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

 

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: 
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, 
so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 
Example 2:

Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation: 
A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:

Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation: 
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
 

Note:

1 <= D <= weights.length <= 50000
1 <= weights[i] <= 500
'''

# Python Binary search with detailed explanation

# The intuition for this problem, stems from the fact that

# a) Without considering the limiting days D, if we are to solve, the answer is simply max(a)
# b) If max(a) is the answer, we can still spend O(n) time and greedily find out how many partitions it will result in.

# [1,2,3,4,5,6,7,8,9,10], D = 5

# For this example, assuming the answer is max(a) = 10, disregarding D, (忽視 disregard)
# we can get the following number of days:
# [1,2,3,4] [5] [6] [7] [8] [9] [10]

# So by minimizing the cacpacity shipped on a day, we end up with 7 days, by greedily chosing the packages for a day limited by 10.

# To get to exactly D days and minimize the max sum of any partition, we do binary search in the sum space which is bounded by [max(a), sum(a)]

# Binary Search Update:
# One thing to note in Binary Search for this problem, is even if we end up finding a weight, that gets us to D partitions, 
# we still want to continue the space on the minimum side, because, there could be a better minimum sum that still passes <= D paritions.

# In the code, this is achieved by:

# if res <= d:
#      hi = mid
# With this check in place, when we narrow down on one element, lo == hi, we will end up with exactly the minimum sum that leads to <= D partitions.

class Solution:
    def shipWithinDays(self, a: List[int], d: int) -> int:
            lo, hi = max(a), sum(a)   
            while lo < hi:
                mid = (lo + hi) // 2
                tot, res = 0, 1  #注意一開始 res = 1, 初始當天運完, 超過運量則增加一天
                for wt in a:
                    if tot + wt > mid:
                        res += 1  #partition off one day
                        tot = wt
                    else:
                        tot += wt
                if res <= d:
                    hi = mid
                else:
                    lo = mid+1
            return lo




#模板2, time complexity O(nlogN), N: the range of (max(weights), sum(weights)), n: the length of weights
#思路: 利用binary search 來找尋最小capacity to ship stuff within d days
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lo, hi = max(weights), sum(weights) #capacity, lo = max(weights) 確保船可以運算任何物品
        while lo + 1 < hi:
            mid = lo + (hi - lo)//2
            if self.days(weights, mid) <= D:
                hi = mid
            else:
                lo = mid
        if self.days(weights, lo) <= D:
            return lo
        else:
            return hi
    
    def days(self, weights, capacity): #check how many days it need to ship
        tot, res = 0, 1
        for wt in weights:
                if tot + wt > capacity:
                    res += 1
                    tot = wt
                else:
                    tot += wt
        return res
































