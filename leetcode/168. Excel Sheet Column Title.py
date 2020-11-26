'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''

class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ''
        nums = []

        while n > 0:
            t = n % 26
            if t == 0: # charecter is 'Z'
                nums.append(26)
                n = int(n / 26) - 1 #702/26 = 27.0 所以要int(),之後-1 是因為扣掉26 for 第一個字母Z生成, 也可以 n//26 -1
            else:
                nums.append(t)
                n //= 26 #向下取整

        for i in nums[::-1]:
            ans += chr(64 + i)
        return ans

'''
we get charecters number for the string from end to start:

last charecter is reminder of dividing by 26
save charecter No. and divide n by 26
repeat for next charecter
2nd loop: build the string and return it
it was a fun problem, but i dont think my explanation is that clear!

cheers
'''
'''
chr(65)
'A'
chr(66)
'B'
chr(90)
'Z'
'''


class Solution:
    def convertToTitle(self, n: int) -> str:
        ans= ''
        nums = []
        while n > 0:
            t = n % 26
            if t == 0:
                nums.append(26)
                n = n//26 -1
            else:
                nums.append(t)
                n //= 26
        for i in nums[::-1]:
            ans += chr(64+i)
        return ans








