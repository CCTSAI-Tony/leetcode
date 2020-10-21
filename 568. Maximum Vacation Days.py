'''
LeetCode wants to give one of its best employees the option to travel among N cities to collect algorithm problems. But all work and no play makes Jack a dull boy, 
you could take vacations in some particular cities and weeks. Your job is to schedule the traveling to maximize the number of vacation days you could take, 
but there are certain rules and restrictions you need to follow.

Rules and restrictions:
You can only travel among N cities, represented by indexes from 0 to N-1. Initially, you are in the city indexed 0 on Monday.
The cities are connected by flights. The flights are represented as a N*N matrix (not necessary symmetrical), 
called flights representing the airline status from the city i to the city j. If there is no flight from the city i to the city j, flights[i][j] = 0; 
Otherwise, flights[i][j] = 1. Also, flights[i][i] = 0 for all i.
You totally have K weeks (each week has 7 days) to travel. You can only take flights at most once per day and can only take flights on each week's Monday morning. 
Since flight time is so short, we don't consider the impact of flight time.
For each city, you can only have restricted vacation days in different weeks, given an N*K matrix called days representing this relationship. 
For the value of days[i][j], it represents the maximum days you could take vacation in the city i in the week j.
You're given the flights matrix and days matrix, and you need to output the maximum vacation days you could take during K weeks.

Example 1:
Input:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]
Output: 12
Explanation: 
Ans = 6 + 3 + 3 = 12. 

One of the best strategies is:
1st week : fly from city 0 to city 1 on Monday, and play 6 days and work 1 day. 
(Although you start at city 0, we could also fly to and start at other cities since it is Monday.) 
2nd week : fly from city 1 to city 2 on Monday, and play 3 days and work 4 days.
3rd week : stay at city 2, and play 3 days and work 4 days.
Example 2:
Input:flights = [[0,0,0],[0,0,0],[0,0,0]], days = [[1,1,1],[7,7,7],[7,7,7]]
Output: 3
Explanation: 
Ans = 1 + 1 + 1 = 3. 

Since there is no flights enable you to move to another city, you have to stay at city 0 for the whole 3 weeks. 
For each week, you only have one day to play and six days to work. 
So the maximum number of vacation days is 3.
Example 3:
Input:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[7,0,0],[0,7,0],[0,0,7]]
Output: 21
Explanation:
Ans = 7 + 7 + 7 = 21

One of the best strategies is:
1st week : stay at city 0, and play 7 days. 
2nd week : fly from city 0 to city 1 on Monday, and play 7 days.
3rd week : fly from city 1 to city 2 on Monday, and play 7 days.
Note:
N and K are positive integers, which are in the range of [1, 100].
In the matrix flights, all the values are integers in the range of [0, 1].
In the matrix days, all the values are integers in the range [0, 7].
You could stay at a city beyond the number of vacation days, but you should work on the extra days, which won't be counted as vacation days.
If you fly from the city A to the city B and take the vacation on that day, the deduction towards vacation days will count towards the vacation days of city B in that week.
We don't consider the impact of flight hours towards the calculation of vacation days.
'''


Thought process
Recursive backtracking

def backtrack(week, city):

backtrack(week, city) = max(stay: days[city][week] + backtrack(week+1, city), fly: max(backtrack(week+1, other) + days[other][week]) for flights[city][other] == 1)
flights can be optimized using adjacency list
base case: week == N, return 0
because there is no state change, we can use memoization

be careful that even if working in a city all week, it can still provide more opportunites for more vacation in future 
(because maybe you can only fly to other city and cannot come back, but future weeks in this city may have many vacations)

just try everything possible!

Iterative solution is also simple

Top-down DP


#刷題用這個, time complexity: O(m*n) space complexity: O(m*n), m:len(week), n: len(cities), 3184ms
#思路: 先建立每個city 的 adjacent list, dp = max(選擇這週待在原城市並下週從原城市計畫, 這週到其他城市並下週從其他城市計畫)
#會出現重複子問題 => 使用memo
#這個不是backtracking, 是dp, 因為同時考慮多個子問題, 並取最好的
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        m, n = len(days), len(days[0])
        cities = [[i for i, v in enumerate(canFly) if v] for canFly in flights] #get avalible cities of a specific city => adjacency list
        memo = {}
        return self.dfs(0, 0, cities, m, n, days, memo)
    
    
    def dfs(self, week, city, cities, m, n, days, memo):
        if week == n: #已過k week, zero index issue
            return 0
        if (week, city) in memo:
            return memo[(week, city)]
        stay = days[city][week] + self.dfs(week+1, city, cities, m, n, days, memo)
        fly = max([days[other][week] + self.dfs(week+1, other, cities, m, n, days, memo) for other in cities[city]], default=0)
        memo[(week, city)] = max(stay, fly)
        return memo[(week, city)]



#也可用 lru_cache => 搭配inner func 比較好使用, 因為可以避免def parameter is not hashable
import functools
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        N, K = len(days), len(days[0])
        flights = [[i for i, can_fly in enumerate(city) if can_fly] 
                   for city in flights]
        @functools.lru_cache(None)
        def backtrack(week, city):
            if week == K:
                return 0
            stay = days[city][week] + backtrack(week+1, city)
            fly = max((days[other][week] + backtrack(week+1, other) 
                      for other in flights[city]), default=0)
            return max(stay, fly)
        return backtrack(0, 0)
















