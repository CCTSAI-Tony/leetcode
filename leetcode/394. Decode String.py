'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

#自己重寫 time complexity O(n)
#思路: 利用stack 來存放 [ 之前的string, 與 [ 前面的數字, reset num, string , 然後進入括號內, 直到遇到 ], 再從stack.pop出 [ 前面的數字與strimg, 
#把內括號裡面的字母乘上括號前面的數字一起變為有效字串(解碼) 再跟前面字串連起來
#數字後面一定有"[" 幫忙reset
#python stack 裡面可以放不同type的物件
class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        string = ""
        stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == "[":  #要reset num & string 因為 裡面說不定有樓中樓情況, ex: "ab3[a2[c3[b]5[a]]]" ex 2[2[2[b]]]=>bbbbbbbb
                stack.append(string) 
                stack.append(num) #先存string 再存num 
                num = 0
                string = ""
            elif s[i] == "]":  #不需要再reset num, 因為[] 裡面只有字母或已轉化成字母(若有樓中樓), 在前面 "[" num 已reset過了, 之後遇到新num不怕疊加到舊num, 不會有[3] 的情況, 只有3[a3[a]]
                string = string * stack.pop()
                string = stack.pop() + string
            else:
                string += s[i]
        return string



#stack 
class Solution(object):
    def decodeString(self, s):
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)  #append 順序很重要
                curString = ''  #set back to default
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString  #串連起來
            elif c.isdigit():
                curNum = curNum*10 + int(c) # ex: 12[a]
            else:
                curString += c
        return curString

# s = "3[a2[c]]", return "accaccacc".

# s = "3[a]2[bc]", return "aaabcbc".

# a = []
# a.append("")
# a.pop()
# ''
# 技巧: list append "" 避免 pop from empty list

