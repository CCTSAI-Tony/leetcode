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
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

# Example 1:

# Input: "III"
# Output: 3
# Example 2:

# Input: "IV"
# Output: 4
# Example 3:

# Input: "IX"
# Output: 9
# Example 4:

# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 5:

# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.



#刷題用這個, time complexity O(n), space complexity O(1)
#思路: hash table, special case like IV= 4, 小的roman 出現在大的roman 前面時, 先扣掉小的值再加回大的值
class Solution:
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def romanToInt(self, s: str) -> int:
        num = 0
        for i in range(0, len(s) - 1):
            if self.dict[s[i + 1]] > self.dict[s[i]]: # next numeral is larger than the current numeral
                num -= self.dict[s[i]]
            else:
                num += self.dict[s[i]] # next numeral is smaller
        return num + self.dict[s[-1]] #加最後一個字

#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        cur_sum = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                cur_sum -= roman[s[i]]
            else:
                cur_sum += roman[s[i]]
        cur_sum += roman[s[-1]]
        return cur_sum


#自己想的 time compleixty O(n), space complexity O(n)
#思路: 利用dict 來存儲特定key, 並搜索s 若連續兩個字搭配有在dict, 就輸入該key值, 若沒有就輸入前一個字的key值
#跑出while loop 記得加回最後一個字, 若倒數兩個字不在dict裡
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V":5, "X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,
                "XC":90,"CD":400,"CM":900}
        num = 0
        i = 1
        while i < len(s):
            if s[i-1:i+1] not in roman:
                num += roman[s[i-1]]
                i += 1
            else:
                num += roman[s[i-1:i+1]]
                i += 2
        if i == len(s) + 1:
            return num
        elif i == len(s):
            num += roman[s[i-1]]
            return num

# "MCMXCIV" = 1994

# We would calculate it as 1000 - 100 + 1000 - 10 + 100 - 1 + 5 = 1994

#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def romanToInt(self, s: str) -> int:
        romen = {"I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, \
               "XL": 40, "XC": 90, "CD": 400, "CM": 900 }
        res = 0
        i = 1
        while i < len(s):
            if s[i-1:i+1] in romen:
                res += romen[s[i-1:i+1]]
                i += 2
            else:
                res += romen[s[i-1]]
                i += 1
        if i == len(s):
            res += romen[s[i-1]]
        return res

#重寫第三次, time complexity O(n), space complexity O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4,
                "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        cur_sum = 0
        i = 1
        while i < len(s):
            if s[i-1:i+1] in roman:
                cur_sum += roman[s[i-1:i+1]]
                i += 2
            else:
                cur_sum += roman[s[i-1]]
                i += 1
        if i == len(s) + 1:
            return cur_sum
        cur_sum += roman[s[i-1]]
        return cur_sum





        '''
        The way this solution works is it parses the string left to right and considers the Roman numerals in pairs. If the numeral to the right is greater than the numeral to the left, we subtract the current numeral's value from the running total, otherwise we add the numeral's value. At the end we return the running total plus the value of the last numeral; since there can be no numeral to the right of the last numeral we always add it.

Thus to calculate the numeric value of

"MCMXCIV" = 1994

We would calculate it as 1000 - 100 + 1000 - 10 + 100 - 1 + 5 = 1994
'''