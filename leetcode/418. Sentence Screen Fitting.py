'''
Given a rows x cols screen and a sentence represented as a list of strings, 
return the number of times the given sentence can be fitted on the screen.

The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. 
A single space must separate two consecutive words in a line.

 

Example 1:

Input: sentence = ["hello","world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.
Example 2:

Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
Output: 2
Explanation:
a-bcd- 
e-a---
bcd-e-
The character '-' signifies an empty space on the screen.
Example 3:

Input: sentence = ["i","had","apple","pie"], rows = 4, cols = 5
Output: 1
Explanation:
i-had
apple
pie-i
had--
The character '-' signifies an empty space on the screen.
 

Constraints:

1 <= sentence.length <= 100
1 <= sentence[i].length <= 10
sentence[i] consists of lowercase English letters.
1 <= rows, cols <= 2 * 104
'''


# Given [‘AB’, ‘CDE’, ‘F’, …, ‘YZ’]
# Width: w

# join the words with empty space
# get the index of the end of a screen line w - 1
# there are 3 cases:

# Case 1:
# “AB-CDE-F-….-YZ” (‘-’ denotes a space)
# reach to the space before F

# Case 2:
# “AB-CDE-F-…._YZ” (‘-’ denotes a space)
# reach to exactly E

# Case 3:
# “AB-CDE-F-….-YZ” (‘-’ denotes a space)
# reach to D

# case 1, I can count one more bit and go to next line
# case 2, I can count two more bits and go to next line
# case 3, I have to move the cursor back until it reach to some space, and go to next line

# When I go through all the rows, how many bits did I counted? Let’s say L, then the answer should be L / length of the string


# time complexity O(m), space complexity O(n), m: rows, n: len(sentence)
# 思路: 先對字串做預處理, 字與字之間要空格, 尾端也要加一個空格, 利用指針對字串移動來模擬塞滿col
# 塞滿col 有三種情況, 若指針對應的字右邊是" ", 代表完美塞滿 指針移動兩格來跨過空格, 若指針本身對應的是" ", 只要移動指針一格
# 若以上條件均不成立, 倒退指針直到指針對應的字左邊是" "
# 技巧: 循懷字串指針使用 % len(s)
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        s = ' '.join(sentence) + ' ' # pre-processing, 字與字中間, 頭與尾 都要加space
        start = 0
        for i in range(rows):
            start += cols - 1
            if s[start % len(s)] == ' ':
                start += 1
            elif s[(start + 1) % len(s)] == ' ':
                start += 2
            else:
                while start > 0 and s[ (start - 1) % len(s) ] != ' ':
                    start -= 1
        return start // len(s)


# 重寫第二次, time complexity O(m), space complexity O(n), m: rows, n: len(sentence)
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = " ".join(sentence) + " "
        i = 0
        for _ in range(rows):
            i += (cols - 1)
            if s[i % len(s)] == " ":
                i += 1
            elif s[(i + 1) % len(s)] == " ":
                i += 2
            else:
                while s[(i - 1) % len(s)] != " ":
                    i -= 1
        return i // len(s)












