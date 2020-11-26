'''
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", 
or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, 
return True if and only if there exists a sequence of moves to transform one string to the other.

 

Example 1:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Example 2:

Input: start = "X", end = "L"
Output: false
Example 3:

Input: start = "LLR", end = "RRL"
Output: false
Example 4:

Input: start = "XL", end = "LX"
Output: true
Example 5:

Input: start = "XLLR", end = "LXLX"
Output: false
 

Constraints:

1 <= start.length <= 104
start.length == end.length
Both start and end will only consist of characters in 'L', 'R', and 'X'.
'''



#刷題用這個, time complexity O(n), space complexity O(n)
#思路: https://leetcode.com/problems/swap-adjacent-in-lr-string/discuss/217070/Python-using-corresponding-position-
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end): 
            return False
        
        A = [(s, idx) for idx, s in enumerate(start) if s == 'L' or s == 'R']
        B = [(e, idx) for idx, e in enumerate(end) if e == 'L' or e == 'R']
        if len(A) != len(B): 
            return False
        
        for (s, i), (e, j) in zip(A, B):
            if s != e: 
                return False
            if s == 'L':
                if i < j:
                    return False
            if s == 'R':
                if i > j:
                    return False
            
        return True


#自己重寫, time complexity O(n), space complexity O(n)
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        s_list = [(v, i) for i, v in enumerate(start) if v in ["L", "R"]]
        e_list = [(v, i) for i, v in enumerate(end) if v in ["L", "R"]]
        if len(s_list) != len(e_list):
            return False
        for s, e in zip(s_list, e_list):
            if s[0] != e[0]:
                return False
            if s[0] == "L":
                if s[1] < e[1]:
                    return False
            if s[0] == "R":
                if s[1] > e[1]:
                    return False
        return True








#naive dfs
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) == 1:
            return False
        visited = set()
        return self.dfs(start, end, visited)
    
    def dfs(self, s, e, visited):
        if s in visited:
            return False
        visited.add(s)
        if s == e:
            return True
        for i in range(1, len(s)):
            if s[i-1:i+1] in ["XL", "RX"]:
                temp = s[:i-1] + s[i-1:i+1][::-1] + s[i+1:]
                if self.dfs(temp, e, visited):
                    return True
        return False
