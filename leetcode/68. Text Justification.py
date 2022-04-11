'''
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; 
that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''
#  time complexity 比較複雜因為難計算divmod, 若忽略它 O(n) n: len(words), m: len(maxWidth)
#  思路: 利用字與字之間至少空一格, 加新word前可先確認是否超過maxWidth, 若是則用divmode對當下一行字與字間隔平分空格, 新word放到下一行
#  最後一行題目說字與字只要空一格就行, 剩下空格全部塞到右邊, 因此使用 ljust(maxWidth)
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        line, width = [], 0
        
        for word in words: 
            if width + len(line) + len(word) > maxWidth: #why len(line), 字與字至少要空1格, 發現若加這字與空格就超過maxWidth, 則先不加此字, 先處理這行空格分配問題
                                                          #len(line)是加此字前有幾個word, 也可以代表若加此字後有多少字與字的空隙
                n, k = divmod(maxWidth - width, max(1, len(line)-1))  #開始調整未加此字的line, 希望字與字空格大小平均, 左邊空格大小優先, 
                                                                      #len(line)-1目前有多少字與字的空隙, 若字只有一個, divmod 一樣除1, 字與邊界空隙, 不然除0會error 
                for i in range(max(1, len(line)-1)):   #len(line)-1, 只有最後一個字以前的word有資格加空格
                    line[i] += " " * (n + (i < k)) # (n + (i < k)) => n+1 or n+0, n是每個空格至少有幾格 trick: (n + (i < k)) , 使得先滿足左邊空格, 餘數一個一個優先拿去填左邊
                ans.append("".join(line))
                line, width = [], 0  #back to default
            line.append(word)
            width += len(word)
            
        ans.append(" ".join(line).ljust(maxWidth)) #最後一行靠左邊對齊
        return ans 

# For the last line of text, it should be left justified and no extra space is inserted between words.
a= "fff"
a.ljust(5)
'fff  '

#刷題用這個, 重寫第二次, time complexity  O(n) , space complexity O(n), n: len(words), m: len(maxWidth)
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        line, width = [], 0
        for word in words:
            if len(line) + len(word) + width > maxWidth:
                n, k = divmod(maxWidth - width, max(1, len(line) - 1))
                for i in range(max(1, len(line)-1)):
                    line[i] += " " * (n + (i < k))
                ans.append("".join(line))
                line, width = [], 0
            line.append(word)
            width += len(word)
        
        temp = " ".join(line)
        temp += " " * (maxWidth - len(temp))
        ans.append(temp)
        return ans

# 重寫第三次, time complexity O(n), space complexity O(n), n: len(words)
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        line = []
        width = 0
        for word in words:
            if len(line) + width + len(word) > maxWidth:
                n, k = divmod(maxWidth - width, max(1, len(line) - 1))
                for i in range(max(1, len(line) - 1)):
                    line[i] += " " * (n + (i < k))
                ans += ["".join(line)]
                line, width = [], 0
            
            line.append(word)
            width += len(word)
        temp = " ".join(line)
        temp += " " * (maxWidth - len(temp))
        ans.append(temp)
        return ans




