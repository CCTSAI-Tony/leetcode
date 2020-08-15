'''
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 

Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
'''

#time complexity O(n), 思路: 利用條件與stack 來忽視nonvalid parenthesis
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack, cur = [], ''
        for c in s:
            if c == '(':
                stack += [cur] #先把目前的result 存在stack, 且同時代表存了一個"(" 然後清空cur, 
                cur = ''
            elif c == ')':
                if stack:  #代表前面有"(", 若沒有則忽視它
                    cur = stack.pop() + '(' + cur + ')' 
            else:
                cur += c  #加入字串
        
        while stack:  #把還存在stack 加回cur, 發生在"(" 很多的情況 例如"a(bc(d(ef)" => abcd(ef), 因為沒有足夠的")"相配  而被忽視
            cur = stack.pop() + cur
        
        return cur


"a" + "b"
'ab'

Input: s = "a)b(c)d"
Output: "ab(c)d"

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"







