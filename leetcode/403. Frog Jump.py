'''
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. 
The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. 
Initially, the frog is on the first stone and @@ assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. 
Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.
'''

# Dynamic programming bottom-up:

# Use a dictionary dic which maps the position of a stone in stones to the set of stepsizes that can jump onto the stone. 
# We initialize dic = {0:{0}}, meaning that we start with the stone at position 0. 
# Next, we iterate i over range(len(stones)), and check if stones[i] is in dic, if it is, 
# it means that there are previous jumps that land on this stone, and we can continue jumping ahead, 
# in which case we iterate over all val in dic[stones[i]], and for each val, 
# we can continue jumping ahead with three stepsizes (val-1, val, and val+1). 
# Therefore, we add val-1 to dic[stones[i]+val-1], val to dic[stones[i]+val], and val+1 to dic[stones[i]+val+1]. 
# Finally, we check if stones[-1] is in dic, if it is, we return True; Else we return False.

# Time complexity: O(n^2), space complexity: O(n^2).
# 思路: 使用hashmap 來紀錄當前石塊是從多少jump跳過來的, 再以該值跳到之後的石塊, 若該值 <= 1, 則不能選擇少跳一步這個選項, 若最後在hashmap出現最後一個石塊, 代表成功
# Note that the frog can only jump in the forward direction. 所以 stepsize.val < 1 是不行的
import collections
class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dic = collections.defaultdict(set)  #好招
        dic[0].add(0)
        for i in range(len(stones)):
            if stones[i] in dic:
                for val in dic[stones[i]]:
                    if val > 0:  #val > 0 除了初始0 其他都可以加上本次jump size的 value, 
                        dic[stones[i]+val].add(val)  #這裡用set 避免重複, add(val) 代表到達這一格時是跳val step 來的, 這樣從那塊石頭跳時, 就知道要跳多少
                    if val > 1:  #  val > 1 還可以選擇跳少一格的選擇, the frog can only jump in the forward direction
                        dic[stones[i]+val-1].add(val-1)
                    dic[stones[i]+val+1].add(val+1)  #跳多一格不管任何值都可以, 0也可以
        return stones[-1] in dic

# a = [1,2,3]
# 4 in a
# False

#自己重寫, time complexity O(n^2) Two nested loops are there, space complexity O(n^2) 
from collections import defaultdict
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dic = defaultdict(set)
        dic[0] = {0}
        for i in range(len(stones)):
            if stones[i] not in dic:
                continue
            for val in dic[stones[i]]:
                if val > 0:
                    dic[stones[i] + val].add(val)
                if val > 1:
                    dic[stones[i] + (val - 1)].add(val - 1)
                dic[stones[i] + (val + 1)].add(val + 1)
        if stones[-1] in dic:
            return True
        return False

 
#重寫第二次, time complexity O(n^2), space complexity O(n^2)
from collections import defaultdict
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dic = defaultdict(set)
        dic[0] = {0}
        for i in range(len(stones)-1):
            if stones[i] not in dic:
                continue
            for jump in dic[stones[i]]:
                if jump > 0:
                    dic[stones[i] + jump].add(jump)
                if jump > 1:
                    dic[stones[i] + (jump-1)].add(jump-1)
                dic[stones[i] + (jump+1)].add(jump+1)
        if stones[-1] in dic:
            return True
        return False

# 重寫第三次, time ccomplexity O(n^2), space complexity O(n^2)
from collections import defaultdict
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        jumps = defaultdict(set)
        jumps[0].add(0)
        for stone in stones:
            if stone not in jumps:
                continue
            for val in jumps[stone]:
                if val > 0:
                    jumps[stone + val].add(val)
                if val > 1:
                    jumps[stone + val - 1].add(val - 1)
                jumps[stone + val + 1].add(val + 1)
        return stones[-1] in jumps


# Dynamic programming top-down:

# We first construct a dictionary mapping the position of each stone in stones to its index in stones. 
# Now suppose we reach stones[i] with a jump of stepsize step. Can we reach the last stone (stones[-1])? 
# We define a function dfs(i, step) which returns True if we can, 
# and returns False if we cannot. We can define dfs(i, step) recursively by jumping one more step from stones[i]. 
# We can jump from stones[i] with stepsizes step-1, step, step+1, for each possible stepsize, 
# we check if stones[i]+stepsize is in dic, if it is, it means that we are jumping onto a stone, 
# and it is a valid jump, so we can recursively call dfs(dic[stones[i]+stepsize], stepsize), 

@@
# if it returns True, we return True; Else we try other stepsizes. If no recursive call returns True, 
# it means that we cannot reach the last stone starting with state (i, step), and we return False.

# The base case for the recursive function dfs(i, step) is if step == 0 or i >= len(stones), we return False; if i == len(stones)-1, we return True.

# We can also make use of a dictionary to store the values of dfs(i, step) for each tuple (i, step), so that we can avoid making the same computation multiple times.

# Time complexity: O(n^2), space complexity: O(n^2).

class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        def dfs(i, step, first = False):
            if step == 0:  #if step == 0, step 不能為0 因為要一直向前跳
                return False
            if i == len(stones)-1:
                return True
            if (i, step) in rec:
                return rec[(i, step)]
            if first:
                steps = {step}  #這邊寫法是一個set, 但是也可以steps = [step], if first, step = 1
            else:
                steps = {step-1, step, step+1}
            for s in steps:
                if stones[i]+s in dic:
                    if dfs(dic[stones[i]+s], s):  #注意first 參數空白, 因為已經不是第一個 所以默認false,  dic[stones[i]+s] 回報index
                        rec[(i, step)] = True  #只要return True or False 留下紀錄是多餘的,若要回推跳躍路徑則是必要, 一旦return True, 一路return True 至最頂層
                        return True
            rec[(i, step)] = False #留下紀錄
            return False
        
        rec = {}
        dic = {stones[i]:i for i in range(len(stones))} #builds up a key: value pair by dic comprehension
        return dfs(0, 1, True)


# Now suppose we reach stones[i] with a jump of stepsize step. Can we reach the last stone (stones[-1])? 

Example 2:

[0,1,2,3,4,8,9,11]

dic: {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 8: 5, 9: 6, 11: 7}
 




























