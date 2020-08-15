# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. 
# The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
# Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

# Example 1:

# Input: 3
# Output: "III"
# Example 2:

# Input: 4
# Output: "IV"
# Example 3:

# Input: 9
# Output: "IX"
# Example 4:

# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# Example 5:

# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

#time complexity O(n)
#思路: hash table 大到小 建立pair, python 3, 預設dict 自帶 insertion ordered
class Solution:
    def intToRoman(self, num: int) -> str:
        numDict = {
            1000 : 'M',
            900 : 'CM',
            500 : 'D',
            400 : 'CD',
            100 : 'C',
            90 : 'XC',
            50 : 'L',
            40 : 'XL',
            10 : 'X',
            9 : 'IX',
            5 : 'V',
            4 : 'IV',
            1 : 'I',
        }
        romanNum = ''
        while num > 0:
            for i, r in numDict.items(): #tuple unpacking
                if i <= num:
                    romanNum += r
                    num -= i
                    break  #離開for loop 並再回for loop i,r 起始位置從頭跑
        return romanNum

# Python 3.7+
# In Python 3.7.0 the insertion-order preservation nature of dict objects has been declared to be an official part of the Python language spec. 
# Therefore, you can depend on it.

# Python 3.6 (CPython)
# As of Python 3.6, for the CPython implementation of Python, dictionaries maintain insertion order by default. 
# This is considered an implementation detail though; 
# you should still use collections.OrderedDict if you want insertion ordering that's guaranteed across other implementations of Python.






''' another method

def intToRoman(self, num: int) -> str:
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        for k in d:
            while num >= k:
                res += d[k]
                num -= k
        return res '''

'''
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        s=1000

        d = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}

        while num!=0:
            r, temp = divmod(num, s)

            if r==9:
                res+=d[s]+d[s*10]
            elif r==4:
                res+=d[s]+d[s*5]
            elif r>=5:
                res+=d[s*5] + d[s]*(r-5) 
            else:
                res += d[s]*r

            s=s//10
            num=temp

        return res
'''