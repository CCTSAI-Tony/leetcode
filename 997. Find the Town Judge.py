'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 

Constraints:

1 <= N <= 1000
0 <= trust.length <= 10^4
trust[i].length == 2
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
'''

#自己想的 time complexity O(n), n = len(trust), space complexity O(N)
#This is equivalent to |Vertices| + |Edges| in graph terms, if we consider each person as a vertex and each trust relationship as a directed edge.
#思路: judge 不會認識人-> 刪除t[0], 建立map 紀錄每個人被誰trust, 最後應該只剩一個人是True 因為不相信任何人, 若不是return -1, 
#對那個人check, 若他被除了自己以外的人信任, 他就是judge
from collections import defaultdict
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_map = defaultdict(set)
        judge = [True] * N
        for t in trust:
            judge[t[0]-1] = False
            trust_map[t[1]].add(t[0])
        if judge.count(True) != 1:
            return -1
        true_judge = judge.index(True) + 1
        if len(trust_map[true_judge]) == N-1:
            return true_judge
        return -1