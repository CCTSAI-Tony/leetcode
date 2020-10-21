'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''
# time complexity O(n ^ 3), n: len(wordDict), space complexity O(n^2)
# Time complexity: O(n^3). Size of recursion tree can go up to n^2. The creation of the 'res' List takes n time.
# memo recursive top down solution
# 思路: back tracking 利用memo {} 來記錄重複 sub problem 的結果, 利用startswith 來尋找candidate, 經典好題
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        memo = {}
        return self.helper(s, wordDict, memo)
        
    def helper(self, s, wordDict, memo):
        if s in memo: 
            return memo[s]
        if not s: #Given a non-empty string, 此題可以不用這行
            return []  

        res = []
        for word in wordDict:
            if not s.startswith(word):  #跳過s不能以自己開頭的字
                continue
            if len(word) == len(s):  #找到一個答案丟進res, 持續往下一個字遍歷, 雖然下一字不可能長度一樣, 但或許可以組合其他字
                res.append(word)
            else:  #開頭相符但len(s) > len(word)
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo) #s[len(word):] 略過word的字串, 切割subproblem
                for item in resultOfTheRest:  #若resultOfTheRest is [], this for loop just break
                    res.append(word + " " + item)  #string
        memo[s] = res #紀錄key:value pair, memo[s] 當下字串s 是可以被wordDict哪些字組成
        return res #list






str.startswith(search_string, start, end)
str = "GeeksforGeeks"
  
# startswith() 
print(str.startswith("Geeks")) => True
print(str.startswith("Geeks", 4, 10)) => False
print(str.startswith("Geeks", 8, 14)) => True


# 自己重寫
# Time complexity: O(n^3). Size of recursion tree can go up to n^2. The creation of the 'res' List takes n time.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        return self.helper(s, wordDict, memo)
    
    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(s) == len(word):
                res.append(word)
                continue
            word_of_res = self.helper(s[len(word):], wordDict, memo)
            for w in word_of_res:
                res.append(word + " " + w)
       
        memo[s] = res
        return res














