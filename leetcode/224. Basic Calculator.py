'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
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
        self.precidence_in = {'+':2, '-':2, '*':4, '/':4, "^": 5, '(':0}  # 不能取self.in => invalid syntax, cause "in" is build in syntax
    
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
        for i, op in enumerate(eval_string):
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
                # if a negative number was encountered, we would have sequencial op in postfix, there is only one element in eval_stack 
                a = 0
                if eval_stack:
                     a = int(eval_stack.pop())
                eval_stack.append(self.eval(a, b, op))
            else:
                eval_stack.append(op)

        if eval_stack:
            return eval_stack[0]
        return 0
       
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

        # raise exception

#重寫第二次, 刷題用這個, time complexity O(n), space complexity O(n)
import re
class Solution:
    def __init__(self):
        self.out_hash = {"+": 1, "-": 1, "(": 3}
        self.in_hash = {"+": 2, "-": 2, "(": 0}
        
    def postfix(self, string):
        op_stack = []
        postfix = []
        pre_op = ""
        for i, op in enumerate(string):
            if op in ["+", "-"] and pre_op in ["", "("]:
                postfix.append("0")
            if op == "+" and pre_op == "-":
                continue
            elif op == "-" and pre_op == "-":
                op_stack.pop()
                op_stack.append("+")
                pre_op = "+"
                continue
            elif op == ")":
                while op_stack[-1] != "(":
                    postfix.append(op_stack.pop())
                op_stack.pop()
            elif op in self.out_hash:
                while op_stack and self.out_hash[op] < self.in_hash[op_stack[-1]]:
                    postfix.append(op_stack.pop())
                op_stack.append(op)
            else:
                postfix.append(op)
            pre_op = op
        while op_stack:
            postfix.append(op_stack.pop())
        return postfix
    
    def evaluate(self, postfix):
        eval_stack = []
        for op in postfix:
            if op in ["+", "-"]:
                b = int(eval_stack.pop())
                a = 0
                if eval_stack:
                    a = int(eval_stack.pop())
                eval_stack.append(self.unit_eval(a, b, op))
            else:
                eval_stack.append(op)
        if eval_stack:
            return eval_stack[0]
        return 0
        
        
    def unit_eval(self, a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        
    def calculate(self, s: str) -> int:
        string = re.findall("\d+|[+\-()]", s)
        postfix = self.postfix(string)
        return self.evaluate(postfix)

# 刷題用這個  ex: "(1+(4+5+2)-3)+(6+8)"
# 自己重寫 time complexity O(n)
# 思路: 因為有parenthesis, 因此設立res來紀錄目前所處位置的值, 不管是括號內還是括號外, 可以看成 舊res+(新res+(新新res)) 樓中樓的概念
# 若進入到一個新的parenthesis, 先存目前的res與括號前的符號到stack 並res歸0 來計算新的parenthesis裡面的值, 直到該parenthesis結束, 
# 之後呼叫stack.pop(), 第一個取出來的是括號前的正負號, res*=sign, 之後stack.pop() 加回括號外的值
# 最後到字串最後一個字時, 跳出for loop, 要手動加回還在num裡的值
# 跟227一樣, 遇到運算子先結算之前的結果, 與227不一樣的是結算後的結果放進res裡, 此題stack主要紀錄括號外的值與符號
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        num = 0
        sign = "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i] in ["+", "-"]:
                if sign == "+":
                    res += num
                else:
                    res -= num
                num = 0
                sign = s[i]
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                res = 0   #因為進入新的parenthesis, 記得res歸0
                sign = "+"
            elif s[i] == ")":
                if sign == "+":
                    res += num
                else:
                    res -= num
                sign = stack.pop()
                if sign == "+":
                    res *= 1
                else:
                    res *= -1
                res += stack.pop()
                num = 0 #記得num 要歸0,因為之後遇到+ or -, res 會+num ex: (2+3) +5 +7
                
        if sign == "+":
            res += num
        else:
            res -= num
        return res
        
#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sumNum = 0
        sign = "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            else:
                if s[i] in ["+", "-"]:
                    if sign == "+":
                        sumNum += num
                    elif sign == "-":
                        sumNum -= num
                    sign = s[i]
                    num = 0
                elif s[i] == "(":
                    stack.append(sumNum)
                    stack.append(sign)
                    sign = "+"
                    sumNum = 0
                elif s[i] == ")":
                    if sign == "+":
                        sumNum += num
                    elif sign == "-":
                        sumNum -= num
                    sign = stack.pop()
                    prev = stack.pop()
                    if sign == "+":
                        sumNum = prev + sumNum
                    elif sign == "-":
                        sumNum =  prev - sumNum
                    num = 0
                    sign = "+"
        if num:
            if sign == "+":
                sumNum += num
            elif sign == "-":
                sumNum -= num
        return sumNum


#重寫第三次, time complexity O(n), space complexity O(n)
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = "+"
        curSum = 0
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            if s[i] in ["+", "-"]:
                if sign == "+":
                    curSum += num
                elif sign == "-":
                    curSum -= num
                num = 0
                sign = s[i]
            if s[i] == "(":
                stack.append(curSum)
                stack.append(sign)
                curSum = 0
                sign = "+"
                num = 0
            if s[i] == ")":
                if sign == "+":
                    curSum += num
                elif sign == "-":
                    curSum -= num
                sign = stack.pop()
                prev = stack.pop()
                if sign == "+":
                    curSum = prev + curSum
                elif sign == "-":
                    curSum = prev - curSum
                num = 0
                sign = "+"
        if num:
            if sign == "+":
                curSum += num
            elif sign == "-":
                curSum -= num
        return curSum

# 連同227一起服用
# 注意此題只有加減符號而已誒, 也不會有22-3(2+5) 這樣的情況, "("前沒有數字
# 與227不一樣的地方在, 為了parenthesis, 增加res變數 來紀錄括號裡的值
class Solution:
    def calculate(self, s):
    res, num, sign, stack = 0, 0, 1, []
        for ss in s:
            if ss.isdigit():
                num = 10*num + int(ss) #前一位數字乘10, 因為是10進位
            elif ss in ["-", "+"]:
                res += sign*num #把遇到"-", "+" 前的num乘上正負號存到res, 並歸0
                num = 0
                sign = [-1, 1][ss=="+"]  #[-1,1][0 or 1]
            elif ss == "(":     #() 要計算括號裡的res, 所以先把之前的res 放到stack裡
                stack.append(res) #ex: 遇到"("前 22-(2+5) stack.append(res) = 22, stack.append(sign) = - 
                stack.append(sign)
                sign, res = 1, 0 #sign, res back to default
            elif ss == ")":
                res += sign*num #ex: 遇到括號")"前 22-(2+5), 
                res *= stack.pop() #乘回括號前正負號
                res += stack.pop()
                num = 0 #num再次歸0
        return res + num*sign #別忘了到盡頭 res要加回最後的值 ex: 1+2, res = 1, num*sign = 2

# Python isdigit() 方法检测字符串是否只由数字组成
# str.isdigit()
# 如果字符串只包含数字则返回 True 否则返回 False。

# 以下实例展示了isdigit()方法的实例：

# #!/usr/bin/python

# str = "123456";  # Only digit in this string
# print str.isdigit();

# str = "this is string example....wow!!!";
# print str.isdigit();
# 以上实例输出结果如下：

# True
# False

# could someone please tell what does: sign = [-1, 1][ss=="+"] do?
# int(True) = 1, int(False) = 0. Hence,
if ss == "+":
    sign = 1
else:
    sign = -1




