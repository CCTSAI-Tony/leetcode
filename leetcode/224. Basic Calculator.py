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




