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

#刷題用這個, postfix 通殺解法, time complexity O(n), space complexity O(n)
#可以同時解決 224, 227, 772
#思路: infix => postfix => evaluate
#技巧, 使用re 來轉化string to list
import re
class Solution:
    def __init__(self):
        self.precidence_out = {'+':1, '-':1, '*':3, '/':3, "^": 6, '(':7}
        self.precidence_in = {'+':2, '-':2, '*':4, '/':4, "^": 5, '(':0}
    
    def calculate(self, s: str) -> int:
        # parse the string using regex
        operations = re.findall('\d+|[+\-*/()]', s)
        postfix = self.create_postfix(operations)
        return self.eval_postfix(postfix)

    def create_postfix(self, eval_string):
        """
        Shunting yard algorithm
        """
        postfix = []
        operator_stack = []
        prev_op = ""
        for op in eval_string:
            if op in ["+", "-"] and prev_op in ("", "("):
                postfix.append("0")
            if op == ')':
                while operator_stack[-1] != '(':
                    postfix.append(operator_stack.pop())
                operator_stack.pop()
            elif op == "-" and prev_op == "-":
                operator_stack.pop()
                operator_stack.append("+")
                prev_op = "+"
                continue
            elif op == "+" and prev_op == "-":
                continue
            elif op == "-" and prev_op in ["*", "/", "^"]  and eval_string[i + 1].isdigit():
                eval_string[i + 1] = str(-1 * int(eval_string[i + 1]))
                continue
            elif op == '(':
                operator_stack.append(op)           

            elif op in self.precidence_out:
                while operator_stack and self.precidence_out[op] <= self.precidence_in[operator_stack[-1]]:
                    postfix.append(operator_stack.pop())
                operator_stack.append(op)
                
            else:
                postfix.append(op)
            prev_op = op
            

        while operator_stack:
            postfix.append(operator_stack.pop())

        return postfix

    def eval_postfix(self, postfix):
        """
        classic post fix evaluation
        """
        eval_stack = []

        for op in postfix:
            if op in ["+", "-", "*", "/", "^"]:
                b = int(eval_stack.pop())
                # if a negative number was encountered just subtract it from 0
                a = 0
                if eval_stack:
                     a = int(eval_stack.pop())
                eval_stack.append(self.eval(a, b, op))
            else:
                eval_stack.append(op)

        if len(eval_stack) == 1:
            return eval_stack[0]
       
    def eval(self, a, b, op):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            if a // b < 0 and a % b:
                return (a // b) + 1
            return a // b
        if op == '^':
            return a ** b

            

#use stack to store different result, if you meet '*' or '/', it will take the last element of stack to do some operation
#利用" 3 + 5 / 2 " 做logic run through 比較好搞懂
#  time complexity O(n), space complexity O(n)
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


#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    pre = stack.pop()
                    num = pre * num
                    stack.append(num)
                elif sign == "/":
                    pre = stack.pop()
                    num = int(pre / num)
                    stack.append(num)
                num = 0
                sign = s[i]
        return sum(stack)

# 重寫第三次, time complexity O(n), space complexity O(n)
class Solution:
    def calculate(self, s: str) -> int:
        stack, num, sign = [], 0, "+"
        for i, c in enumerate(s):
            if c.isdigit():
                num = num*10 + int(c)
            if (not c.isdigit() and not c.isspace()) or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                if sign == "-":
                    stack.append(-num)
                if sign == "*":
                    stack.append(stack.pop() * num)
                if sign == "/":
                    temp = stack.pop()
                    if temp/num < 0 and temp % num != 0:
                        stack.append(temp // num + 1)
                    else:
                        stack.append(temp // num)
                sign = c
                num = 0
        return sum(stack)
        