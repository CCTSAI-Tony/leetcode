'''
There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.



After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', 
if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Note:

0 <= N <= 10^5
String dominoes contains only 'L', 'R' and '.'
'''

#刷題用這個
# [Python] O(N) solution. Go through array twice
# First pass, from left to right, only count distance of current index to previous 'R'. Save all distance in dist array
# Second pass, from right to left, count distance of current index to previous 'L'. 
# If lDist < rDist (dist[i]), current cell should be 'L', if lDist == rDist, current cell should be '.'


#  思路:  利用左到右遍歷與右到左遍歷, 來比較當下"."離誰比較近, 變成比較近的"L" or "R", 若一樣近則變成原樣 "."
#  注意 =, == 不能亂用, 容易出bug

class Solution(object):
    def pushDominoes(self, dominoes):
        lst = list(dominoes)
        dist = [0] * len(dominoes)
        rDist = None
        for i, val in enumerate(lst):
            if val == 'R':
                rDist = 0
            elif val == 'L':
                rDist = None  #  切忌不能 rDist == None
            elif rDist != None:  # "." => "R"
                rDist += 1
                dist[i] = rDist
                lst[i] = 'R'
        lDist = None
        for i in range(len(lst) - 1, -1, -1):
            if dominoes[i] == 'L':  #原序列 == "L"
                lDist = 0
            elif dominoes[i] == 'R':
                lDist = None
            elif lDist != None:
                lDist += 1
                if lDist < dist[i] or lst[i] == '.': #離L比較近, 原序列== "." 但之前被改成"R" or 之前沒被動過依舊是"." => 改成"L"
                    lst[i] = 'L'
                elif lDist == dist[i]:  #離L or R 一樣近
                    lst[i] = '.'
        return ''.join(lst)






Intuition:
Whether be pushed or not, depend on the shortest distance to 'L' and 'R'.
Also the direction matters.
Base on this idea, you can do the same thing inspired by this problem.
https://leetcode.com/problems/shortest-distance-to-a-character/discuss/125788/

Here is another idea that focus on 'L' and 'R'.
'R......R' => 'RRRRRRRR'
'R......L' => 'RRRRLLLL' or 'RRRR.LLLL'
'L......R' => 'L......R'
'L......L' => 'LLLLLLLL'

Time Complexity: O(N) 
Two Pointers
# sliding window, 這種解法不易想
class Solution:
    def pushDominoes(self, d):
        d = 'L' + d + 'R' #前後多加一組"L","R"
        res = []
        i = 0
        for j in range(1, len(d)):
            if d[j] == '.': 
                continue
            middle = j - i - 1
            if i: 
                res.append(d[i])
            if d[i] == d[j]: 
                res.append(d[i] * middle)
            elif d[i] == 'L' and d[j] == 'R': 
                res.append('.' * middle)
            else: 
                res.append('R' * (middle // 2) + '.' * (middle % 2) + 'L' * (middle // 2))
            i = j
        return ''.join(res)

















