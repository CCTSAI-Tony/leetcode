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

# 刷題用這個, time complexity O(n^2 + 2^n + w), space complexity O(2^n*n + w), N: the length of the input string, W:  the number of words in the dictionary
# 思路: top down dp 利用memo {} 來記錄重複 sub problem 的結果
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        # table to map a string to its corresponding words break
        # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
        memo = defaultdict(list)

        #@lru_cache(maxsize=None)    # alternative memoization solution
        def _wordBreak_topdown(s):
            """ return list of word lists """
            if not s:
                return [[]]  # list of empty list

            if s in memo:
                # returned the cached solution directly.
                return memo[s]

            for endIndex in range(1, len(s)+1):
                word = s[:endIndex]
                if word in wordSet:
                    # move forwards to break the postfix into words
                    for subsentence in _wordBreak_topdown(s[endIndex:]):
                        memo[s].append([word] + subsentence)
            return memo[s]

        # break the input string into lists of words list
        _wordBreak_topdown(s)

        # chain up the lists of words into sentences.
        return [" ".join(words) for words in memo[s]]

#刷題用這個! Top down dp
#重寫第二次, time complexity O(n^2 + 2^n + w), space complexity O(2^n*n + w), N: the length of the input string, 
# W:  the number of words in the dictionary
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = {}
        return [" ".join(words) for words in self.helper(s, wordDict, memo)]
    
    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return [[]]
        res = []
        for i in range(1, len(s) + 1):
            if s[:i] in wordDict:
                for rest in self.helper(s[i:], wordDict, memo):
                    res.append([s[:i]] + rest)
        memo[s] = res
        return memo[s]



# time complexity O(N^2 + 2^N + W^2), N: the length of the input string, W:  the number of words in the dictionary, space complexity O(N^2 + 2^N*N + W^2)
# memo recursive top down solution
# 思路: top down dp 利用memo {} 來記錄重複 sub problem 的結果, 利用startswith 來尋找candidate, 經典好題
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


# 重寫第四次, time complexity O(N^2(recursion) + 2^N(每個字斷點與不斷點) + W(construct the set)), space complexity O(N^2 + 2^N*N + W)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = {}
        return [" ".join(words) for words in self.dfs(s, wordDict, memo)]
    
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return [[]]
        res = []
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                remain = self.dfs(s[i+1:], wordDict, memo)
                for words in remain:
                    res.append([s[:i+1]] + words)
        memo[s] = res
        return memo[s]


# 重寫第五次, O(N^2 + 2^N + W^2), N: the length of the input string, W:  the number of words in the dictionary, space complexity O(N^2 + 2^N*N + W^2)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        def dfs(string):
            if not string:
                return [[]]
            if string in memo:
                return memo[string]
            res = []
            for i in range(len(string)):
                word = string[:i+1]
                if word in wordDict:
                    remain = dfs(string[i+1:])
                    for item in remain:
                        res.append([word] + item)
            memo[string] = res
            return memo[string]
        return [" ".join(x) for x in dfs(s)]


str.startswith(search_string, start, end)
str = "GeeksforGeeks"
  
# startswith() 
print(str.startswith("Geeks")) => True
print(str.startswith("Geeks", 4, 10)) => False
print(str.startswith("Geeks", 8, 14)) => True


# 自己重寫
# time complexity O(N^2 + 2^N + W^2), N: the length of the input string, W:  the number of words in the dictionary, space complexity O(N^2 + 2^N + W^2)
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
        return memo[s]

#重寫第二次, time complexity O(N^2 + 2^N + W^2), N: the length of the input string, W:  the number of words in the dictionary, space complexity O(N^2 + 2^N + W^2)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        return self.helper(s, wordDict, memo)
    
    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        res = []
        for word in wordDict:
            if s.startswith(word):
                if len(s) == len(word):
                    res.append(word)
                    continue
                else:
                    restWords = self.helper(s[len(word):], wordDict, memo)
                    for r in restWords:
                        res.append(word + " " + r)
        memo[s] = res
        return memo[s]

#重寫第三次, time complexity O(N^2 + 2^N + W^2), space complexity O(N^2 + 2^N + W^2)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        return self.helper(s, wordDict, memo)
        
    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        res = []
        for word in wordDict:
            if s.startswith(word):
                if len(word) == len(s):
                    res.append(word)
                    continue
                n = len(word)
                rest = self.helper(s[n:], wordDict, memo)
                for r in rest:
                    res.append(word + " " + r)
        memo[s] = res
        return memo[s]









