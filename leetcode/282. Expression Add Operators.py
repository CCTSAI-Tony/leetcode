'''
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, 
or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
'''

# 刷題用這個, time complexity O(n*3^n)
# 思路: dfs backtracking, last 就是後面遇到*時, 要跟val乘的數 => 先乘除後加減
# dfs() parameters:
# num: remaining num string
# temp: temporally string with operators added
# cur: current result of "temp" string
# last: last multiply-level number in "temp". if next operator is "multiply", "cur" and "last" will be updated
# res: result to return
class Solution(object):
    def addOperators(self, num, target):
        res, self.target = [], target
        for i in range(1,len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res) # this step put first number in the string
        return res

    def dfs(self, num, temp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return #這個不加也不影響答案, 但會影響runtime, 因為會繼續往下走for i in range(1, len(num)+1) 這一行, 判斷無可迭代則會自動返回

        for i in range(1, len(num)+1): #why len(num)+1, 因為要包含最後一個數 ex: n = len(num), for i in range(n), val = num[:i], 最大val = num[:n-1]->少掉最後一個數
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], temp + "+" + val, cur+int(val), int(val), res)
                self.dfs(num[i:], temp + "-" + val, cur-int(val), -int(val), res)
                self.dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val), res) #最重要是這個


#自己重寫, 典型dfs backtracking
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        self.target = target
        for i in range(1, len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"):
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res)
        return res
    
    def dfs(self, num, temp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            else:
                return
        for i in range(1, len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"):
                val = int(num[:i])
                self.dfs(num[i:], temp + "+" + num[:i], cur + val, val, res)
                self.dfs(num[i:], temp + "-" + num[:i], cur - val, -val, res)
                self.dfs(num[i:], temp + "*" + num[:i], (cur-last) + last*val, last*val ,res)






