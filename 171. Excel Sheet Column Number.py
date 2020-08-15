'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''
## use ord()
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in s:
            res = res*26 + ord(i) - 64   # 64 = ord('A') - 1
        return res
        
## use int()
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in s:
            res = res * 26 + int(i, 36) - 9
        return res
'''
int() function in Python and Python3 converts a number in given base to decimal.

Syntax :

int(string, base)

string : consists of 1's and 0's
base : (integer value) base of the number.
Returns :

Returns an integer value, which is equivalent 
of binary string in the given base. 
Errors :

TypeError : Returns TypeError when any data type other 
than string or integer is passed in its equivalent position.
# Example_2 
str = '100'
  
print("int('100') with base 2 = ", int(str, 2)) 
print("int('100') with base 4 = ", int(str, 4)) 
print("int('100') with base 8 = ", int(str, 8)) 
print("int('100') with base 16 = ", int(str, 16)) 

int('100') with base 2 =  4
int('100') with base 4 =  16
int('100') with base 8 =  64
int('100') with base 16 =  256


int('A',36)
10

其中:A~F相當於十進制的10~15，這些稱作十六進位數字
其中:A~Z相當於十進制的10~25，這些稱作36進位數字


'''
Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

class Solution:
    def titleToNumber(self, s: str) -> int:
        
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        power = 0
        res = 0
        
        for char in reversed(s):
            num =  letters.index(char) + 1
            res += num*(26**power)
            power += 1
        
        return res

class Solution:
    def titleToNumber(self, s: str) -> int:
        
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        res = 0
        for i in s:
            res = res*26 + letters.index(i)+1
        return res






















