'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''
#use stack to store different result, if you meet '*' or '/', it will take the last element of stack to do some operation
#利用" 3+5 / 2 " 做logic run through 比較好搞懂
#  time complexity O(n)
#  思路: 指針遍歷 利用stack 來存取相關計算元, 以isdigit, isspace 來區分計算元 or 計算子, 碰到下一個計算子or最後一個元素 就處理之前的expression
#  記得除法比較複雜要分除完是負數還是正數, 若是負數且有小數則要加1, 因為python // 是向下取整, 但題目是truncate toward zero, @@ 可以使用int() 來實現truncate toward zero 不論正負數
#  這題與224最大不同在於, 224有parenthesis 且沒有*/, 
class Solution:
    def calculate(self, s):
        if not s:
            return "0"
        stack, num, sign = [], 0, "+" #default is '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10+int(s[i])  #前一個數字自動進位
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1: #if it is the last word or operators(+,-,*,/), 這邊不能用elif,確保最後一個字能被啟動
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop()*num)#pop the last item of stack and multiply it to the num, then append it back to stack
                else:
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0: #-3//2 因為python 向下取整, 但因題意truncate toward zero 所以要加1, 若tmp 能被num整除 則不需要+1
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                sign = s[i] #change the operator to the current one, 遇到最後一個字元, sign會變成最後一個字元
                num = 0 #num back to default
        return sum(stack)

# The expression string contains only non-negative integers => 不會出現 5 * -37


#自己重寫的, time complexity O(n), 刷題用這個
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign ="+"
        digit = 0
        
        for i in range(len(s)):
            if s[i].isdigit():
                digit = digit * 10 + int(s[i])
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if sign == "+":
                    stack.append(digit)
                elif sign == "-":
                    stack.append(-digit)
                elif sign == "*":
                    num = stack.pop()
                    stack.append(digit*num)
                elif sign == "/":
                    num = stack.pop()
                    stack.append(int(num/digit))
                sign = s[i]
                digit = 0
        return sum(stack)





        