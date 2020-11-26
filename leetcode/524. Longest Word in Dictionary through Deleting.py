'''
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. 
If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
'''

#  2 pointer 
#  The time complexity is very optimal too! check function uses O(N) time, where N is the size of s. 
#  Comparing cand < res is also O(N). In total O(NM) where M is the size of the dictionary.
#  time complexity, O(NM) where N is the size of s,  M is the size of the dictionary.
#  思路:  s針對字典每個字做指針比較動作, 若字相同則兩者指針同步向右, 若不相同s指針往右代表delete 該字, 若字典字的指針順利比對全部完成, 代表s是能刪除一些字串等於字典字的
#  注意! 題目說只能delete不能改變順序
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = ''
        for cand in d:
            if self.check(s, cand) and len(cand) > len(res) or (len(cand) == len(res) and cand < res):
                res = cand
        return res
    

    def check(self, s, t): #check s 是否能刪掉一些字串等於t
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                continue #重要, 很容易忘
            i += 1  #刪除該字, 但原順序是不變的
        return j == len(t)


 # (len(cand) == len(res) and cand < res) 相同長度比lexicographicall order


#自己重寫
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = ""
        for word in d:
            if self.check(s, word) and (len(word) > len(res) or (len(word) == len(res) and word < res)):
                res = word
        return res
    
    def check(self, s, word):
        i, j = 0, 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                i+=1
                j+=1
                continue
            i+=1
        return j == len(word)











