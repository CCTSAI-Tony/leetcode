'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''

#刷題用這個
#字典用法 不需要int()
#思路: dfs top down dp + hash table, 中間要間隔所以return 前面要空一格, 
class Solution:
    def numberToWords(self, num: int) -> str:
        self.digits = {1:"One", 2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine", 10:"Ten", 11:"Eleven", \
        12:"Twelve",13:"Thirteen", 14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
        self.tens = {2:"Twenty",3:"Thirty",4:"Forty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety"}
    
        if num == 0:
            return "Zero"
        ans = self.int_to_string(num)
        return ans[1:]
    
    def int_to_string(self, num):
        if num >= 1e9:
            return self.int_to_string(num//1e9) +" Billion" + self.int_to_string(num%1e9)
        elif num >= 1e6:
            return self.int_to_string(num//1e6) +" Million" + self.int_to_string(num%1e6)
        elif num >= 1e3:
            return self.int_to_string(num//1e3) +" Thousand" + self.int_to_string(num%1e3)
        elif num >= 1e2:
            return self.int_to_string(num//1e2) +" Hundred" + self.int_to_string(num%1e2)
        elif num >= 20:
            return " " + self.tens[num//10] + self.int_to_string(num%10)
        elif num >= 1:
            return " " + self.digits[num//1]
        else:  #elif num == 0: 若不加這一行, string can't concatenate Nonetype
            return ""




class Solution:
    def numberToWords(self, num: int) -> str:
        self.digits = [
            'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
            'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen',
            'Eighteen', 'Nineteen' #zero 放在這只是為了index 需求
        ]
        self.tens = [
            'Zero', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'
        ]  #zero, ten 放在這只是為了index 需求
        if num == 0:
            return 'Zero'
        else:
            ans = self.int2String(num)
            return ans[1:] #avoid the space of first positio

    def int2String(self, num):
        if num >= 1e9: #3.32 * 9 = 29.88, 這題最大數值以Billion表示足以
            return self.int2String(num / 1e9) + ' Billion' + self.int2String(num % 1e9) #no need to round down, cause we have int(num), it has a space to split up
        elif num >= 1e6:
            return self.int2String(num / 1e6) + ' Million' + self.int2String(num % 1e6)  #' Million', don't forget to add space in the initial
        elif num >= 1e3:
            return self.int2String(num / 1e3) + ' Thousand' + self.int2String(num % 1e3)
        elif num >= 1e2:
            return self.int2String(num / 1e2) + ' Hundred' + self.int2String(num % 1e2)
        elif num >= 20:
            return " " + self.tens[int(num / 10)] + self.int2String(num % 10) #warning, it has a space to split between prenum and num and num >= 20 ex: 101
        elif num >= 1:
            return " " + self.digits[int(num)] #為什麼要用int, 因為list indices must use int not float
        else:
            return ""  #為了整除return, ex: input = 20, 不然 nonetype can't be concatenated




