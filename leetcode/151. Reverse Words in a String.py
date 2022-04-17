'''
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.
'''


#自己重寫第二次, time complexity O(n), space complexity O(1), 刷題用這個
class Solution:
    def reverseWords(self, s: str) -> str:
        words = ""
        word = ""
        prev = ""
        for i in range(len(s)-1, -1, -1):
            if s[i] != " " and prev == " ":
                if word:  # 避免" w" leading space 的情況
                    words += word + " "
                word = s[i]
            elif s[i] != " " and prev != " ":
                word = s[i] + word
            prev = s[i]
        words += word
        return words

        
#自己想的, follow up, For C programmers, try to solve it in-place in O(1) extra space., TIME COMPLEXITY O(n)
#思路: 利用split(), 預設seperate 任何空格 => words list, 並reverse, 再用 " ".join 連結 reversed words list
class Solution:
    def reverseWords(self, s: str) -> str:
        
        return " ".join(s.split()[::-1])



#自己重寫 time complexity O(n), space complexity O(n)
#思路: 倒序連字時, 變成 s[i] + word
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        word = ""
        words = ""
        for i in range(len(s)):
            if s[i] != " " and word != "" and s[i-1] == " ": # and word != "" 因為有leading zero, 所以加這個條件
                words += (word + " ")
                word = s[i]
            elif s[i] != " ":
                word = s[i] + word  # 重要, 因為倒序
            else:
                continue
        words += word
        return words


#time complexty O(n), space complexity O(n)
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        # First reverse entire string, then iterate over reversed string
        # and again reverse order of characters within a word. Append each word to words.
        word = ""
        words = ""
        s = s[::-1] #重要! 先reverse
        for j, i in enumerate(s):
            # character is not space, a current word exists, 
            # and previous character is space, e.g. i=b in " a b":
            if i != " " and word != "" and s[j-1] == " ": #word != "" 是為了 第一個字前面有空格的情況, 此時word 還沒成字
                # add current word to words and append " " to later add this i
                words += (word + " ")
                word = i
            # character is not space, but it's either first character in string
            # or is part of current word, e.g. i=b in "b", " b" "ab", "a ab "
            elif i != " ":
                word = i + word #因為已經先reverse 所以這邊要 word = i + word
            else:
                continue #跳過空格

        words += word #記得加回最後一個字
        
        return(words)

'''
s = "  i am    hungry   "
for j, i in enumerate(s):
    print(j,i)

0  
1  
2 i
3  
4 a
5 m
6  
7  
8  
9  
10 h
11 u
12 n
13 g
14 r
15 y
16  
17  
18  

'''



"not accepted in interview"
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])

'''
Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
str = "00000003210Runoob01230000000"; 
print str.strip( '0' );  # 去除首尾字符 0
 
 
str2 = "   Runoob      ";   # 去除首尾空格
print str2.strip();

3210Runoob0123
Runoob

str = "123abcrunoob321"
print (str.strip( '12' ))
3abcrunoob3