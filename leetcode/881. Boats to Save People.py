'''
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
Note:

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000
'''

#自己想的, time complexity O(nlogn)
#思路: 先對people sort 使用雙指針, greedy, 小的配最大的, 若超過limit, 則最大的先用一艘船, 換次大的能不能跟最小配, 若可以配則雙指針同時內縮
#若最後雙指針指向同一個元素, 代表剩最後一個元素, 單獨+1艘船
#使用dict, 來map people[i] O(1), 不然get people[i] => O(n)
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        people_map = {}
        for i in range(len(people)):
            people_map[i] = people[i]
        count = 0
        i, j = 0, len(people)-1
        while i < j:
            while i < j and people_map[i] + people_map[j] > limit:
                count += 1
                j -= 1
            if i < j:
                count += 1
                i += 1
                j -= 1
        if i == j:
            count += 1
        return count



