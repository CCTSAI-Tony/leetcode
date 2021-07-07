'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . 
The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
 

Note: Do not use the eval built-in library function.
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





# The idea is to compute each independent item of the expression and then sum them up. For example in 3 - 4 / (4* 6 ), 3 is an item and -4/(4*6) is also an item.

# We use num as the variable of the current operand, op as the operation of the partial expression not yet evaluated (the operation before num). 
# Then iterative go though each char, and check following condition:

# If char is a digit, we continue construct number with it.
# If char is (, we need to push the op in stack, and reset op to +
# If char is one of +, -, *, /, ), we have reached end of an partial expression. so we evaluate the result of the partial expression. 
# If the char is ), we have to pop all the items out until we reach the last op before (, and then evaluate the partial expression. We then set op as current char.
# Finally, after we reach the end of the string, we do another evaluation of the expression to include the last num.

# stack, time complexity O(n), 刷題用這個, 此題是I, II 的合體, 
# 思路: 遇到空格continue, 利用stack來存儲中間運算元與運算子, op 加減乘除個別處理, 特別的地方在於遇到")", 使用while loop 把括號內的值加總成num, 括號"(" 的前面一定是運算子
# 加總完 括號num後, 再pop出前面的運算子, 這樣就可以執行一次運算把中間值加到stack裡, 中間值or中間運算子加到stack裡後, 都要記得rest num, op => 0, "+"
# 運到"(" 則是把括號前的運算子加到stack, 這樣就可以專心應付括號裡面的值, 最後遇到最後一個數, 記得要再做一次計算把最後的num加到stack裡, sum up stack裡的值 => 答案
# 技巧: 使用isinstance 來確認物件的type, 因為int 沒有額外的method 來確認自身的type, 
# 技巧: The integer division should truncate toward zero => 使用int(num1/num2) 來執行, ex:int(-1/2) => 0

class Solution(object):
    def calculate(self, s):
        stack = []
        num, op = 0, '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in ['+', '-', '*', '/', ')']:
                self.update(op, num, stack)
                num = 0 #重要, 這裡記得num歸0, 因為之後要用while loop 相加stack 後面的數 到num => 括號裡的值
                if s[i] == ')':
                    while isinstance(stack[-1], int): #利用isinstance 來判斷stack[-1] 的屬性, 因為int 沒有 is.digit() 的method
                        num += stack.pop() 
                    op = stack.pop()
                    self.update(op, num, stack)
                num, op = 0, s[i]
            elif s[i] == '(':
                stack.append(op)
                num, op = 0, '+' #設回default, 不然進括號後舊op會干擾答案 ex:(1+2), 1前面沒有運算子 無法更新op
        self.update(op, num, stack) #若最後一個是純粹的int, 要把num加回stack, 若是")" 則什麼也沒做
        return sum(stack)


    def update(self, op, num, stack):
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            stack.append(stack.pop() * num)
        elif op == '/':
            stack.append(int(stack.pop() / num))


#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num, op = 0, "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in ["+", "-", "*", "/", ")"]:
                self.update(op, num, stack)
                num = 0
                if s[i] == ")":
                    while isinstance(stack[-1], int):
                        num += stack.pop()
                    op = stack.pop()
                    self.update(op, num, stack)
                num, op = 0, s[i]
            elif s[i] == "(":
                stack.append(op)
                num, op = 0, "+"
        self.update(op, num, stack)
        return sum(stack)
    
    def update(self, op, num, stack):
        if op == "+":
            stack.append(num)
        elif op == "-":
            stack.append(-num)
        elif op == "*":
            stack.append(stack.pop() * num)
        elif op == "/":
            stack.append(int(stack.pop() / num))  

# We should use int(stack.pop() // num).

# stack.pop() // num == floor(stack.pop() / num), which will round to the smaller int.
# (In C++, it will truncate to the int)

# e.g. in python3, -5//2 == -3 and int(-5/2) = -2.




#自己重寫, time complexity O(n)
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i] in ["+", "-", "*", "/", ")"]:
                self.update(num, op, stack)
                if s[i] == ")":
                    num = 0
                    while isinstance(stack[-1], int):
                        num += stack.pop()
                    op = stack.pop()
                    self.update(num, op, stack)
                op = s[i]
                num = 0
            elif s[i] == "(":
                stack.append(op)
                num = 0
                op = "+"
        self.update(num, op, stack)
        return sum(stack)
            
    
    def update(self, num, op, stack):
        if op == "+":
            stack.append(num)
        elif op == "-":
            stack.append(-num)
        elif op == "*":
            stack.append(stack.pop()*num)
        elif op == "/":
            stack.append(int(stack.pop()/num))




