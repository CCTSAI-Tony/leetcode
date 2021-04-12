Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
# Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, 
# and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, 
# which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, 
# or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.

# Note:

# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
# If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
# Example 1:

# Input: "42"
# Output: 42
# Example 2:

# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.
# Example 3:

# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# Example 4:

# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical 
#              digit or a +/- sign. Therefore no valid conversion could be performed.
# Example 5:

# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.

#自己重寫, time complexity O(n) 32ms, 刷題用這個
#思路: 先使用lstrip() 來去除字串右邊空格, 遇到正負號看是否為字串第一個, 若是則紀錄sign, 不是就break, 剩下字串看是否isdigit(), 若是繼續 不是break
#相同技巧 遇到isdigit(), num = num* 10 + int(str[i]), 
class Solution:
    def myAtoi(self, str: str) -> int:
        sign = "+"
        num = 0
        str = str.lstrip()
        for i in range(len(str)):
            if not str[i].isdigit():
                if i == 0 and str[i] in ["+", "-"]:
                    sign = str[i]
                    continue
                break
            num = num * 10 + int(str[i])
        
        if sign == "-":
            num = num * -1
            return -2**31 if num < -2**31 else num
        return 2**31 -1 if num > 2**31 -1 else num

# a = "  yytt  rere  "
# a.lstrip()
# 'yytt  rere  '
# a = "  yytt  rere  "
# a.rstrip()
# '  yytt  rere'
# a = "  yytt  rere  "
# a.strip()
# 'yytt  rere'


#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        res = []
        for i in range(len(s)):
            if i == 0 and not s[i].isdigit():
                if s[i] in ["+", "-"]:
                    res.append(s[i])
                else:
                    return 0
            elif s[i].isdigit():
                res.append(s[i])
                
            elif not s[i].isdigit():
                break
        res = "".join(res)
        if not res or res in ["+", "-"]:
            return 0
        else:
            temp = int(res)
            if temp > 2**31-1:
                return 2**31-1
            elif temp < -2**31:
                return -2**31
            else:
                return temp

#重寫第三次, time complexity O(n), space complexity O(1)
class Solution:
    def myAtoi(self, s: str) -> int:
        value = 0
        sign = "+"
        s = s.strip()
        if not s:
            return 0
        idx = 0
        if not s[0].isdigit():
            if s[0] in ["+", "-"]:
                sign = s[0]
                idx += 1
            else:
                return 0
        while idx < len(s) and s[idx].isdigit():
            digit = s[idx]
            value = value * 10 + int(digit)
            idx += 1
        if sign == "-":
            value *= -1
            if value < -2**31:
                return -2**31
            return value
        else:
            if value > 2**31 - 1:
                return 2**31 - 1
            return value


class Solution:
    def myAtoi(self, str: str) -> int:
        import re
        m = re.search('^\s*[\-\+]?\d+', str)  #正則表達式
        if m:
            m = int(m.group(0)) #(0)no match argument = 0
            low = -pow(2, 31)
            high = pow(2, 31) - 1
            if m >= high:
                return high
            elif m <= low:
                return low
            else:
                return m
        else:
            return 0





# \s It indicates a single whitespace character           
# ^\s* 開頭的space 0 ~ 許多個
# \d is a digit (a character in the range 0-9), and + means 1 or more times. So, \d+ is 1 or more digits.
# re.search  Returns a Match object if there is a match anywhere in the string

# a = "-556"
# int(a)
# -556

# a = "      -556"
# int(a)
# -556


# import re

# m = re.search('(?<=abc)(d(e))f', 'abcdef')

# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# This prints:

# def de e
# what '?<=' does. This is a so called look-behind which means that it matches the part behind the expression that it bounds.

# No paranthesis are needed to form match group 0 since it locates the whole match object anyway.

# The opening bracket in front of the letter 'd' takes the last closing bracket in front of the letter 'f' to form matching group 1.

# The brackets that are around the letter 'e' define matching group 2.

# group(0) returns the full string matched by the regex. 
# It's just that abc isn't part of the match. (?<=abc) doesn't match abc - it matches any position in the string immediately preceded by abc.









