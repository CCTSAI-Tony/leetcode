'''
A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

Given the array reservedSeats containing the numbers of seats already reserved, 
for example, reservedSeats[i] = [3,8] means the seat located in row 3 and labelled with 8 is already reserved.

Return the maximum number of four-person groups you can assign on the cinema seats. 
A four-person group occupies four adjacent seats in one single row. 
Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent, 
but there is an exceptional case on which an aisle split a four-person group, in that case, 
the aisle split a four-person group in the middle, which means to have two people on each side.

 

Example 1:



Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows the optimal allocation for four groups, 
where seats mark with blue are already reserved and contiguous seats mark with orange are for one group.
Example 2:

Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output: 2
Example 3:

Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4
 

Constraints:

1 <= n <= 10^9
1 <= reservedSeats.length <= min(10*n, 10^4)
reservedSeats[i].length == 2
1 <= reservedSeats[i][0] <= n
1 <= reservedSeats[i][1] <= 10
All reservedSeats[i] are distinct.
'''

'''
We use three numbers to record whether the left, the middle or the right is occupied or not.
First, we record whether the left, middle or right is occupied or not using a set as the value in the dictionary.
For n rows, the maximum number of families that can sit together are 2*n.
Then we iterate through the dictionary, if all three positions in the row was blocked, the total cnt should -2.
If less than 3 positions was blocked, the total cnt should -1.
'''

# 刷題用這個, time complexity O(mn), space complexity O(mn)
# 思路: 分左 中 右 group, 紀錄是否有人先占位, 若沒占位 一個row 最多可以有兩個家庭坐進去, 但是若有人佔位在左中右group, 依個別情況來減少家庭數量
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = collections.defaultdict(set)

        for i,j in reservedSeats:
            if j in [2,3,4,5]:
                seats[i].add(0)  # mark
            if j in [4,5,6,7]:
                seats[i].add(1)
            if j in [6,7,8,9]:
                seats[i].add(2)
        res = 2*n
        for i in seats:
            if len(seats[i]) == 3:
                res -= 2
            else: #只要有人佔位左中右 就要-1, 最多只能坐滿一個family
                res -= 1

        return res


# 重寫第二次, time complexity O(mn), space complexity O(mn)
from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        groups = defaultdict(set)
        for i, j in reservedSeats:
            if j in [2, 3, 4, 5]:
                groups[i].add(0)
            if j in [4, 5, 6, 7]:
                groups[i].add(1)
            if j in [6, 7, 8, 9]:
                groups[i].add(2)
        res = 2 * n
        for i in groups:
            if len(groups[i]) == 3:
                res -= 2
            else:
                res -= 1
        return res































