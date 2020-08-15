'''
You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

 

Example 1:

Input: sticks = [2,4,3]
Output: 14
Example 2:

Input: sticks = [1,8,3,5]
Output: 30
 

Constraints:

1 <= sticks.length <= 10^4
1 <= sticks[i] <= 10^4
'''

#自己想的, time complexity O(nlogn)
#思路: greedy, 都是挑目前最短的兩個貼紙合併, 因為一開始就挑比較長的貼紙, 之後這合併貼紙與其他貼紙合併還要再付一次比較長的錢, 比較長的貼紙留到最後合併比較划算
#注意: 合併完的貼紙要放回heap, 因為合併完的貼紙可能不再是最短的兩個貼紙之一
import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1 :
            stick_1 = heapq.heappop(sticks)
            stick_2 = heapq.heappop(sticks)
            res += (stick_1 + stick_2)
            heapq.heappush(sticks, stick_1 + stick_2)
        return res