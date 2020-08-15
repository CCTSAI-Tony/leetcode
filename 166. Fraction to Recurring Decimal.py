'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
'''


class Solution:
# @return a string
    def fractionToDecimal(self, numerator, denominator):
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator*denominator < 0 else ''
        result = [sign+str(n), '.']
        stack = [] #處理小數
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))

        idx = stack.index(remainder)
        result.insert(idx+2, '(') #inx +2 因為原本result就有兩個元素
        result.append(')') #最後加上)
        return ''.join(result).replace('(0)', '').rstrip('.') #.replace('(0)', '').rstrip 是應付一開始就被整除的狀況 ex: 12/6 '2.(0)'



'''
The syntax of insert() method is

list.insert(index, element)
vowel = ['a', 'e', 'i', 'u']
vowel.insert(3, 'o')
print('Updated List: ', vowel)
Updated List:  ['a', 'e', 'i', 'o', 'u']

Remove spaces to the right of the string:

txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")

of all fruits     banana is my favorite

a = ['2','3','4']
''.join(a)
'25354'

string.replace(old, new, count)

string = "geeks for geeks geeks geeks geeks" 
   
# Prints the string by replacing geeks by Geeks  
print(string.replace("geeks", "Geeks"))  
  
# Prints the string by replacing only 3 occurrence of Geeks   
print(string.replace("geeks", "GeeksforGeeks", 3)) 

Geeks for Geeks Geeks Geeks Geeks
GeeksforGeeks for GeeksforGeeks GeeksforGeeks geeks geeks
'''sr

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        ans=""

        if numerator/denominator < 0:
            ans=ans+'-'

        numerator=abs(numerator)
        denominator=abs(denominator)
        
        quotient, remainder=divmod(numerator,denominator)

        ans=ans+str(quotient)
        retval=None

        remainders={}

        quotientall=""
        ind=0
        if(remainder==0): #一開始就被整除
            retval= ans
        else: #開始進入小數處理
            ans=ans+"."
            remainders[str(remainder)] = ind #記錄位置          hash table d ={'a':3,'b':3} key 要str化

            while(remainder!=0):
                remainder= remainder*10
                quotient, remainder =divmod(remainder,denominator)
                quotientall += str(quotient) #把每次remainder *10 得到的商加進去 
                if str(remainder) in remainders: # 出現循環小數, by the way 也可以寫成 if str(remainder) in remainders.keys():
                    ans = ans+ quotientall[:remainders[str(remainder)]] +"("+quotientall[remainders[str(remainder)]:]+")"

                    retval= ans
                    break
                elif (remainder==0): #被整除 a.fractionToDecimal(21,12) '1.75'
                    retval = ans+quotientall
                    break
                else:
                    ind += 1 #ind 會逐漸提高
                    remainders[str(remainder)] = ind #紀錄位置 注意remainder變數會一直換
        return retval

divmod(1,3)
(0, 1)

divmod(10,3)
(3, 1)

divmod(5,7)
(0, 5) remainders['5'] = 0

5/7

0.7142857142857143

a = Solution()
a.fractionToDecimal(5,7)

'0.(714285)'

1/6
0.16666666666666666
a.fractionToDecimal(1,6)

'0.1(6)'

'3' + '5'
'35'
'''
Idea is to put every remainder into the hash table as a key, and the current length of the result string as the value. 
When the same remainder shows again, it's circulating from the index of the value in the table.
'''










'''