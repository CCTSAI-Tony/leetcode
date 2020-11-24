'''
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  
It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

 

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
 

Note:

1 <= paragraph.length <= 1000.
0 <= banned.length <= 100.
1 <= banned[i].length <= 10.
The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
There are no hyphens or hyphenated words.
Words only consist of letters, never apostrophes or other punctuation symbols.
'''
https://youtu.be/xwwYAP_Y4PA

I added a shortcut with MAX

# time complexity O(n)
#思路: 利用string.punctuation and s.replace(" "), 來把字串的符號變成" ", 以利之後split()
#技巧: max(d, key=d.get)
import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]):
        d = {}  #dict    
        lower_paragraph = paragraph.lower()  #轉小寫
        
        for c in string.punctuation: #針對每種標點符號
            lower_paragraph = lower_paragraph.replace(c,' ') #用space 取代標點符號, 注意一定要留space 不然字會黏在一起
            
        list_paragraph = lower_paragraph.split()  #default split(" "), 分開list 化

        for word in list_paragraph:
            if word not in banned:
                d[word] = d.get(word,0) + 1
                    
        return max(d, key=d.get) # retrieve key thanks to the highest value, key=d.get => callable func

#重寫第二次, time complexity O(n), space complexity O(n)
from collections import Counter
import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for c in string.punctuation:
            paragraph = paragraph.replace(c, " ")
        paragraph_list = paragraph.split()
        dic = Counter(paragraph_list)
        return max([word for word in dic.keys() if word not in banned], key=lambda word: dic[word])




# import string
# string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# a = "fihsefi  seflijlsef esfefs   sefef"
# a.split()
# ['fihsefi', 'seflijlsef', 'esfefs', 'sefef']
# a.split()[1]
# 'seflijlsef'







