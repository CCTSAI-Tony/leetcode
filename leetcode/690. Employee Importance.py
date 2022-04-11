'''
You are given a data structure of employee information, which includes the employee's unique id, their importance value and their direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. 
They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], 
and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all their subordinates.

Example 1:

Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. 
They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
 

Note:

One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.
'''

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
#time complexity O(n), space complexity O(n), n is the number of employees
#思路: 經典dfs 遍歷, 首先要建立對應id 的 e_dict 才能順利遍歷
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        e_dict = {}
        self.res = 0
        for e in employees:
            e_dict[e.id] = e
        self.dfs(e_dict[id], e_dict)
        return self.res
    
    def dfs(self, e, e_dict):
        self.res += e.importance
        for s in e.subordinates:
            self.dfs(e_dict[s], e_dict)


# 重寫第二次, bfs, time complexity O(n), space complexity O(n)
from collections import deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        e_id = {}
        for employee in employees:
            e_id[employee.id] = employee
        queue = deque([id])
        ans = 0
        while queue:
            for _ in range(len(queue)):
                employee_id = queue.popleft()
                employee = e_id[employee_id]
                ans += employee.importance
                for subordinate_id in employee.subordinates:
                    queue.append(subordinate_id)
        return ans



