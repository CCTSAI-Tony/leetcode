'''
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: 
the number of passengers that must be picked up, and the locations to pick them up and drop them off.  
The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
 
 

Constraints:

trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000
'''

#自己想的, time complexity O(nlogn), space complexity O(n)
#思路: 先對trips 依照start_location 排序, 建立heap 會存放載人後 (end_location, num_passengers)
#遍歷trips, 依照trip人數 seats += 載人, 若有heap, 則用while loop check 是否有人的end_location <= end_location => seats -= 這些提早下車or在end_location 下車的人數
#確認目前車上人數 <= capacity, 若無 => return False => 若成功遍歷所有trip後 return True
import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        seats = 0
        heap = []
        trips.sort(key=lambda x: x[1])
        for trip in trips:
            seats += trip[0]
            while heap and heap[0][0] <= trip[1]:
                seats -= heapq.heappop(heap)[1]  
            if seats > capacity:
                return False
            heapq.heappush(heap, (trip[2], trip[0]))
        return True



















