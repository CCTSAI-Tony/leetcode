'''
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, 
if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
 

Note:

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.
'''

#自己想的, time complexity O(nlogn), space complexity O(n)
#思路: 使用hash table 來建立sort orfer, 若letter not in S => 排序放最後面
from collections import defaultdict
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        dic = defaultdict(int)
        for i, v in enumerate(S):
            dic[v] = i
        for i , v in enumerate(T):
            if v not in dic:
                dic[v] = float("inf")
        T_list = list(T)
        T_list.sort(key=lambda x: dic[x])
        return "".join(T_list)

#思路: 使用heap, hash table 來排序 time complexity O(nlogn), space complexity O(n)
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        m = {c: idx for idx, c in enumerate(S)}
        queue = []
        for c in T:
            heapq.heappush(queue, (m.get(c, sys.maxint), c))
        ret = ''
        while queue:
            _, v = heapq.heappop(queue)
            ret += v
        return ret


