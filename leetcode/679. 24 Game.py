'''
You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, 
the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
'''

#刷題用這個, time complexity O(1) => there is a hard limit of 9216 possibility, space complexity O(1)
#思路: Backtracking 使用combination and set(inter) 來recursion
#技巧: 記得要用round => 因為除號有可能導致誤差
#技巧, 為何要用enumerate(nums), 因為nums 裡有可能出現相同num, 所以使用index(unique) 來做比對是否相同
import itertools as it
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return round(nums[0], 4) == 24 #這裡記得要用round, 因為除號有可能導致誤差
        else:
            for (i, m), (j, n) in it.combinations(enumerate(nums), 2): #combinations 也是一個iterator
                    new_nums = [x for t, x in enumerate(nums) if i != t != j] #排除 m, n
                    inter = {m+n, abs(m-n), n*m} #abs(m-n) => In particular, we cannot use - as a unary operator. 不會有負號
                    if n != 0: 
                        inter.add(m/n)
                    if m != 0: 
                        inter.add(n/m)
                    
                    if any(self.judgePoint24(new_nums + [x]) for x in inter):
                        return True
            
            return False



#自己重寫一次, time complexity O(1), space complexity O(1)
from itertools import combinations
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return round(nums[0], 4) == 24 # 取到小數點第四位
        for (i, v), (j, w) in combinations(enumerate(nums), 2):
            new_nums = [k for t, k in enumerate(nums) if t != i and t != j]
            inters = {v+w, abs(v-w), v*w} # 用set 來去重
            if v != 0:
                inters.add(w/v)
            if w != 0:
                inters.add(v/w)
            if any(self.judgePoint24(new_nums + [x]) for x in inters):
                return True
        return False


#重寫第二次, time complexity O(1), space complexity O(1)
from itertools import combinations
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return round(nums[0], 4) == 24
        for (i, m), (j, n) in combinations(enumerate(nums), 2):
            inner = {m*n, m+n, abs(m-n)}
            if m != 0:
                inner.add(n/m)
            if n != 0:
                inner.add(m/n)
            new_nums = [v for k, v in enumerate(nums) if i != k != j]
            if any([self.judgePoint24(new_nums + [x]) for x in inner]):
                return True
        return False


# 重寫第三次, time complexity O(1), space complexity O(1)
from itertools import combinations
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if len(cards) == 1:
            return round(cards[0], 4) == 24
        for (i, v), (j, w) in combinations(enumerate(cards), 2):
            new_cards = [num for k, num in enumerate(cards) if k != i and k != j]
            inters = {v+w, abs(v-w), v*w}
            if w != 0:
                inters.add(v/w)
            if v != 0:
                inters.add(w/v)
            if any(self.judgePoint24(new_cards + [x]) for x in inters):
                return True
        return False







