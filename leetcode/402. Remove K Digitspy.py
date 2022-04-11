'''
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''


# The high-level logic is to get as small number as possible from the most siginificant digit (leftmost). 
# So using a stack, we just keep exchange digit if it's smaller than the previous one until k digits are already removed.
# Corner case is when the digits are non-decreasing. Add another loop or do slicing to remove k digits on the right.

#stack法, time complexity: O(n+k), 刷題用這個
#思路: greedy, leading digit變小才能最大程度變小, ex: 98765 => 9765 > 8765(leading變小), 若後面一個沒有比較小, 則stack.append 下一個digit, stack[-1] 就是 leading digit
#使用stack 存digit, 若後面digit < stack[-1]則pop掉stack[-1], k-=1, 使用while loop 連續去除比較大的leading digit
#return 的時候leading zero 要去掉, string.lstrip(), 若依照上面規則刪除digit還有剩餘k, 則stack.pop() 剩下的k
#ex: num = "1432219", k = 3 => "1219"
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) <= k:
            return '0'
        
        stack = []
        
        for digit in num:
            while k > 0 and stack and int(stack[-1]) > int(digit): #注意while 後面條件的順序, 若先接int(stack[-1]) > int(digit) 會產生 list index out of range
                stack.pop()  #pop出比較大的digit
                k -= 1
            stack.append(digit)
        
        while k > 0: #corner case 112 remove 2 when k = 1
            stack.pop()
            k -= 1
        return ''.join(stack).lstrip('0') or '0' #若沒有leading zeros 只剩"", return "0"

#自己重寫, time complexity O(n+k)
#技巧: "5" > "66" => False, "5" > "1" => True, "-1" > "5" => False, "6" > "-5" => True, string 也能比大小
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        stack = []
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        while k > 0:
            stack.pop()
            k -= 1
        
        return "".join(stack).lstrip("0") or "0"

# 重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"
        stack = []
        for digit in num:
            while k > 0 and stack and int(stack[-1]) > int(digit):
                stack.pop()
                k -= 1
            stack.append(digit)
        while k:
            stack.pop()
            k -= 1
        ans = "".join(stack).lstrip("0")
        return ans if ans else "0"
# a = "" or "0"
# a
# '0'
# a = "0" or "1"
# a
# '0'
# a = 0 or 1
# a
# 1




# This question is very similar to 316. Remove Duplicate Letters with little bit extra work

# the way to make number as small as possible is that make right most digit as small as possible

# then come back to question, we know we can remove at most k digit to generate new digit
# so we can add/remove until k == 0

# as example of "1432219"
# []
# ['1'] => since stack is empty , just add into stack
# ['1', '4'] => since 1 < 4, so we do not need to repalce
# ['1', '3'] => since 3 is less than 4, and we have k(3)-- times able to remove,so we can
# replace 4 with 3
# ['1', '2'] => 2 < 3, replace 3 with 2 k(2) --
# ['1', '2', '2'] => 2 == 2, continue
# ['1', '2', '1'] => since 1 < 2, replace it k(1)--
# ['1', '2', '1', '9'] => does not matter the next number is less or greater, since k is zero, we
# can not remove any more digit, so this is the end of program

# some case need to handle is avoid leading zero, which seems like the only different to 316. Remove Duplicate Letters


#此解法跟上面同工異曲之妙, 但是請看下面的例子來釐清while loop logic 
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in range(len(num)):
            
            while True:  #這種結構我稱為三明治
                if  k == 0 or not stack:  #如果不加這一行, 先過濾一些case, 下一行會 list index out of range
                    break  #out of the while loop
                
                if stack[-1] > num[i]:  #不停地滿前面大的替換小的
                    k -= 1
                    stack.pop()
                else:  #重要這邊一定要加else: break 不然有些狀況會陷入無限循環 ex: stack[-1] <= num[i], stack != None, etc..
                    break
            stack.append(num[i])
        while k != 0:  #corner case 112
            stack.pop()
            k -= 1
        for i in range(len(stack)):
            if stack[i] != "0":
                break
        stack = stack[i:]

        if not stack:
            return "0"
        return "".join(stack)


# for i in range(10):
#     if i == 7:
#         break
# i
# 7


i = 10
while True:
    if i >0:
        print(i,"ok")
    if i == 10:
        print(i,"i")
        i-=1
    if i == 11:
        print(i,"i")
        i-=1
    else: 
        print("else")
        break

# 只要那一輪 沒有達成else 前面if的條件 該輪就會進入else
10 ok
10 i
else

i = 10
while True:
    if i == 11:
        print(i,"i")
        i-=1
    if i >0:
        print(i,"ok")
    if i == 10:
        print(i,"i")
        i-=1
    else: 
        print("else")
        break
# 只要那一輪 有達成else 前面if的條件 就會進入下一輪
10 ok
10 i
9 ok
else

i = 10
while True:
    if i >0:
        print(i,"ok")
    if i == 10:
        print(i,"i")
        i-=1
    else: 
        print("else")
        break
# 只要那一輪 達成else 前面if 的條件 該輪就不會進入else
10 ok
10 i
9 ok
else


i = 10
while True:
    if i >0:
        print(i,"ok")
    elif i == 10:
        print(i,"i")
        i-=1
    else: 
        print("else")
        break
# 只要那一輪 有出現elif, 達成某一條件就直接進入下一輪, mutually exclusive
10 ok 無限循環









