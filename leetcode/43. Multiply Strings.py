# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:

# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


#刷題用這個, time complexity O(m*n), space complexity O(m+n)
#思路: 先建立佔為符[0]*(m+n), 再建立兩個指針, position & tempPos, position指的是起始乘法最小的位數, tempPos則是當下乘法最小的位數,  相乘的值放在對應的product[tempPos] 裡
#每做一次乘法運算, 就要想到進位, tempPos 則是往左shift(因為nums2指針往左移了)
#最後答案要去除leading zero, 若全部去除只剩"", 代表該原始值為"0"   
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = [0] * (len(num1) + len(num2)) 
        position = len(product)-1 
        for n1 in num1[::-1]: 
            tempPos = position
            for n2 in num2[::-1]: 
                product[tempPos] += int(n1) * int(n2) 
                product[tempPos-1] += product[tempPos]//10 
                product[tempPos] %= 10 
                tempPos -= 1 
            position -= 1 
        num_str = ''.join(map(str, product)).lstrip("0")
        return num_str if num_str != "" else "0"


#自己重寫, time complexity O(m*n), space complexity O(m+n)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = [0]*(len(num1)+len(num2))
        pos = len(product) - 1
        for n1 in num1[::-1]:
            temPos = pos
            for n2 in num2[::-1]:
                product[temPos] += int(n1) * int(n2)
                product[temPos-1] += product[temPos] // 10
                product[temPos] %= 10
                temPos -= 1
            pos -= 1
        num = "".join(map(str, product)).lstrip("0")
        return num if num != "" else "0"







class Solution:
    def multiply(self, num1, num2):
        product = [0] * (len(num1) + len(num2)) #placeholder(佔位符) for multiplication ndigit by mdigit result in n+m digits
        position = len(product)-1 # position within the placeholder

        for n1 in num1[::-1]: #reverse iterate
            tempPos = position
            for n2 in num2[::-1]: 
                product[tempPos] += int(n1) * int(n2) # ading the results of single multiplication
                product[tempPos-1] += product[tempPos]//10 # bring out carry number to the left array
                product[tempPos] %= 10 # remove the carry out from the current array
                tempPos -= 1 # first shifting the multplication to the end of the first integer
            position -= 1 # then once first integer is exhausted, shifting the second integer and starting 


        # once the second integer is exhausted we want to make sure we are not zero padding  
        pointer = 0 # pointer moves through the digit array and locate where the zero padding finishes
        while pointer < len(product)-1 and product[pointer] == 0: # if we have zero before the numbers shift the pointer to the right, 只保留最後一個0
            pointer += 1

        return ''.join(map(str, product[pointer:])) # only report the digits to the right side of the pointer

        

    #   想想手動乘法怎麼做    
    #   123
    #   456
    # -------
    #   56088




        
