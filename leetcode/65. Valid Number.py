'''
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. 
However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, 
please click the reload button to reset your code definition.
'''

# We use three flags: met_dot, met_e, met_digit, mark if we have met ., e or any digit so far. 
# First we strip the string, then go through each char and make sure:

# If char == + or char == -, then prev char (if there is) must be e
# . cannot appear twice or after e
# e cannot appear twice, and there must be at least one digit before and after e
# All other non-digit char is invalid

#刷題用這個, time complexity O(n), 指針遍歷
#思路: first strip s, next go through each char and make sure, set met_dot, met_e, met_digit to record the visiting
#if meet +/-, prev char must be e
#there is no second . and can't not appear after e
#if we meet, there is no second e and there must be at least onde digit before and after e
#if we meet all other non-digit ch => return False
#warning: 3. and .2 can also be interpreted as a decimal number, +3 can also be interpreted as a decimal number, +2-5 false
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        met_dot = met_e = met_digit = False
        for i, char in enumerate(s):
            if char in ['+', '-']: # ex: 1e+10, 1e-10, 也可以1e10
                if i > 0 and s[i-1] != 'e':
                    return False
            elif char == '.':
                if met_dot or met_e: 
                    return False
                met_dot = True
            elif char == 'e':
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False #met_digit set to False, if there is no digit after e, ans will be False
            elif char.isdigit():
                met_digit = True
            else:
                return False
        return met_digit

#自己重寫, time complexity O(n)
class Solution:
    def isNumber(self, s: str) -> bool:
        met_dot, met_e, met_digit = False, False, False
        s = s.strip()
        for i in range(len(s)):
            if s[i] == ".":
                if met_dot or met_e:
                    return False
                met_dot = True
            elif s[i] == "e":
                if met_e or not met_digit:
                    return False
                met_e = True
                met_digit = False
            elif s[i] in ["+", "-"]:
                if i > 0 and s[i-1] != "e":
                    return False
            elif s[i].isdigit():
                met_digit = True
            else:
                return False
        return met_digit




