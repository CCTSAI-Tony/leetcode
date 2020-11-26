'''
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

Example 1:

Input: "())"
Output: 1
Example 2:

Input: "((("
Output: 3
Example 3:

Input: "()"
Output: 0
Example 4:

Input: "()))(("
Output: 4
 

Note:

S.length <= 1000
S only consists of '(' and ')' characters.
'''

#自己想的, time complexity O(n), space complexity O(n)
#思路: greedy + stack, 遇到"(" 存到stack, 遇到")" 若not stack => 則此時要加一個"(" count += 1
#最後count加上所有stack 裡面無法配對的"("
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        if not S:
            return 0
        stack = []
        count = 0
        for p in S:
            if p == "(":
                stack.append("(")
            elif p ==")":
                if not stack:
                    count += 1
                else:
                    stack.pop()
        if stack:
            count += len(stack)
        return count



