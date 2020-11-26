'''
Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
'''

Here I used helper to convert left and right equations into the coef and const which represent the coefficient of x and remaining constant.

#題目規定: f there is exactly one solution for the equation, we ensure that the value of x is an integer. => output 是 int
#思路: 分開等號兩邊, 分別計算多少個x, num多少 => 若兩邊x一樣多, num不一樣多 => no solution, 若都不一樣 => 'x=' 整數, 若ｘ不一樣多 num相等 => 'x=0', 若ｘ一樣多 num相等 => Infinite solutions
class Solution(object):
    def solveEquation(self, equation):
        left, right = equation.split('=') #分開計算左右兩邊 多少個x, num
        k1, b1 = self.helper(left)
        k2, b2 = self.helper(right)
        # k1x + b1 = k2x + b2
        ans = 'x=' + str((b2 - b1) // (k1 - k2)) if k1 != k2 and b1 != b2 \
              else "Infinite solutions" if k1 == k2 and b1 == b2 \
              else "No solution" if b2 != b1 else 'x=0' #最後的else 不能加if
        return ans
    

    def helper(self, s):
        sign, n = 1, len(s)
        # i, coef, const stand for current index, and accumulative 'x' coefficient and constant
        i = coef = const = 0
        while i < n:
            if s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i].isdigit():
                j = i #j 臨時指針
                while j < n and s[j].isdigit():
                    j += 1
                tmp = int(s[i:j])
                if j < n and s[j] == 'x':
                    coef += tmp * sign
                    j += 1
                else:
                    const += tmp * sign
                i = j-1
            else:
                coef += 1 * sign
            i += 1
        return coef, const


#自己重寫 helper, time complexity O(n), 24ms, 96.2%
class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split("=")
        c1, v1 = self.helper(left)
        c2, v2 = self.helper(right)
        return "x=" + str((v2-v1)//(c1-c2)) if c1 != c2 and v1 != v2 \
        else "Infinite solutions" if c1 == c2 and v1 == v2 \
        else "No solution" if c1 == c2 and v1 != v2 \
        else "x=0" #最後的else 不能加if
    
    def helper(self, s):
        num = 0
        sign = "+"
        const = 0
        coef = 0
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i] in ["+", "-"]:
                if sign == "+":
                    const += num
                else:
                    const -= num
                num = 0
                sign = s[i]
            elif s[i] == "x":
                if num == 0:
                    if i != 0 and s[i-1] == "0": #ex: "0x=0"
                        pass
                    else:    
                        if sign == "+":
                            coef += 1
                        else:
                            coef -= 1
                else:
                    if sign == "+":
                        coef += num
                    else:
                        coef -= num
                num = 0
                sign = "+"
        if num: #加回殘留num
            if sign == "+":
                const += num
            else:
                const -= num
        return (coef, const)






