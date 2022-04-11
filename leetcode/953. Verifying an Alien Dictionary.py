'''
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. 
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, 
return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) 
According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
'''

Hash indexes of each character for better runtime
Compare every adjacent word
If any letter of former word is in higher order, return False
If current letter of former word is in lower order, forget the rest of word
If lenght of former word is longer and latter word is substring of former, return False (apple & app etc.)
Return True


#time complexity O(n*k) n:len(words), k: average len of word
#思路: 建立hash table 把新oder順序紀錄下來, 技巧: 利用zip 使前後兩兩一起比較, 若出現亂序則比較途中會發現 => ex: 5 < 9 < 11 > 2 途中比較若前者>後者 return False
#比較a, b 的每一個letter => 使用zip 兩兩相同位置letter 一起比較> 
#若前者letter order > 後者 letter order return False, 前者letter order < 後者 letter order => break the inner for loop => 換下一組word比對
#若前者letter order == 後者 letter order => 換下一對字符繼續比對
#特殊狀況, if len(a) > len(b) and a[:len(b)] == b, return False, 空字符 oder 是最前面的
class Solution:
    def isAlienSorted(self, words, order):
        ind = {c: i for i, c in enumerate(order)}
        for a, b in zip(words, words[1:]): #前一個word 配後一個word ex: words = ["word","world","row","terror"] => [('word', 'world'), ('world', 'row'), ('row', 'terror')]
            if len(a) > len(b) and a[:len(b)] == b: #apple & app
                return False
            for s1, s2 in zip(a, b):
                if ind[s1] < ind[s2]: #前者找到比後者小的letter, 後面letter也不用比較了
                    break
                elif ind[s1] > ind[s2]:
                    return False
        return True

# a = "abcd"
# b = "hi"
# print(list(zip(a,b)))
# [('a', 'h'), ('b', 'i')]

zip
zip() will zip 2 element one by one,
zip(words, words[1:]) here will combine first element(words[0]) in words with
words[1], so we can compare current element with next element: 0->1, 1->2

#自己重寫, time complexity O(n*k) n:len(words), k: average len of word
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx = {v:i for i, v in enumerate(order) }
        for a, b in zip(words, words[1:]):
            if len(a) > len(b) and a[:len(b)] == b:
                return False
            for x, y in zip(a, b):
                if idx[x] > idx[y]:
                    return False
                elif idx[x] < idx[y]: #break the inner for loop
                    break
        return True


# 重寫第三次, time complexity O(n*k), space complexity O(1), n:len(words), k: average len of word
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {d: i for i, d in enumerate(order)}
        for a, b in zip(words, words[1: ]):
            if len(a) > len(b) and a[:len(b)] == b:
                return False
            for s1, s2 in zip(a, b):
                if order_map[s1] > order_map[s2]:
                    return False
                elif order_map[s1] < order_map[s2]:
                    break
        return True



