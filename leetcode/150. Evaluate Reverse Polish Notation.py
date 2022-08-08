'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''

#自己重寫, time complexity O(n)
#思路: 利用stack來暫存operand, 遇到operator 時, operand的左右順序要注意, 不然值會出錯 ex: 13//5 == 2, 5//13 == 0
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                a = int(stack.pop())
                b = int(stack.pop())
                c = b + a
                stack.append(c)
            elif i == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                c = b - a
                stack.append(c)
            elif i == "*":
                a = int(stack.pop())
                b = int(stack.pop())
                c = b * a
                stack.append(c)
            elif i == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                c = b // a
                if b % a != 0 and c < 0:
                    c += 1
                stack.append(c)
            else:
                stack.append(i)
        return stack.pop()


class Solution:
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    # here take care of the case like "1//-22",
                    # in Python, it returns -1, while in 
                    # Leetcode it should return 0 !! Division between two integers should truncate toward zero.
                    if l*r < 0 and l % r != 0:
                        stack.append(l//r+1) #// 向0取整
                    else:
                        stack.append(l//r)
        return stack.pop() #pop出最後結果





























