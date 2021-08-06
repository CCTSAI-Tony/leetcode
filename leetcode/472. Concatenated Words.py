'''
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.
'''


# 刷題用這個, Time: O(n*l^2), n: the length of words, l: the logest length of word, Space: O(N), N: the legth of total wordss
# 思路: top down dp
# If a word can be Concatenated from shorter words, then word[:i] and word[i:] must can also be Concatenated from shorter words.
# Build results of word from results of word[:i] and word[i:]
# Iterate i from range(1, len(word)) to avoid a word is Concatenated from itself. 重要!!
# Use memorization to avoid repeat calculation.
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        mem = {}
        words_set = set(words)
        return [w for w in words if self.check(w, words_set, mem)]
    
    def check(self, word, word_set, mem):
        if word in mem:
            return mem[word]
        mem[word] = False
        for i in range(1, len(word)):
            if word[:i] in word_set and (word[i:] in word_set or self.check(word[i:], word_set, mem)):
                mem[word] = True
                break  #out of for loop, 代表已經確認此字可以被concatenated
        return mem[word]


# 重寫第二次, time complexity O(n*l^2)
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        mem = {}
        words_set = set(words)
        return [w for w in words if self.check(w, words_set, mem, False)]
    
    def check(self, word, word_set, mem, concatenated):
        if word in word_set and concatenated:
            return True
        if word in mem:
            return mem[word]
        mem[word] = False
        for i in range(1, len(word)):
            if word[:i] in word_set and self.check(word[i:], word_set, mem, True):
                mem[word] = True
                break  #out of for loop, 代表已經確認此字可以被concatenated
        return mem[word]


# 重寫第三次
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        memo = {}
        res = []
        words = set(words)
        for word in words:
            if self.dfs(word, words, memo, False):
                res.append(word)
        return res
    
    def dfs(self, word, words, memo, concatenated):
        if word in words and concatenated:
            return True
        if word in memo:
            return memo[word]
        memo[word] = False
        for i in range(1, len(word)):
            if word[:i] in words and self.dfs(word[i:], words, memo, True):
                memo[word] = True
                break
        return memo[word]

# In the interview I was asked to return the words used for concatenation instead of concatenated words. How would the solution look like then?

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        mem = {}
        words_set = set(words)
        return [w for w in words if self.check(w, words_set, mem)]
    
    def check(self, word, word_set, mem):
        if word in mem:
            return mem[word]
        mem[word] = []
        for i in range(1, len(word)):
            if word[:i] in word_set and word[i:] in word_set:
                mem[word] = [word[:i], word[i:]]
                break
            elif word[:i] in word_set and self.check(word[i:], word_set, mem):
                mem[word] = [word[:i]]
                mem[word].extend(mem[word[i:]])
                break
        print(word, mem[word])
        return mem[word]

# a = []
# if a:
#     print("ok")

# no feedback

# a = [4]
# if a:
#     print("ok")

# ok


# A concatenated word is a word add other word(words) as prefix.

# We have to answer a question recursively: is a substring(word[x, word.length()-1]) prefixed with another word in words?

# That's natural to prefix tree(trie). 

# We can build a trie using words and search for concatenated words in the trie. 

# We have to make a decision when we meet a node that meets the end of a word (with en in the example below). We can
#   - either take the current node's associated word as prefix (and restart at root for another word) 
#   - or not take the current node's associated word as prefix (i.e. move further within the same branch).
# For example,
#     root           
#      /\
#     c  d
#     /   \
#     a    o
#    /      \
#   t(en)    g(en)
#   /         
#  s(en)    
 
# To concatenate catsdogcats using {cat, cats, dog}
# search tree: (-'s in the same vertical line are sibling nodes)
#     root - c - a - t(en)  - X [to take cat as prefix doesn't work]
#                           - s(en) - d - o - g(en) - c - a - t  - s(en) DONE!
#                                                   - X [not to take dog as prefix doesn't work]
#                                   -  [not to take cats as prefix doesn't work]

#刷題用這個, time complexity O(N), space complexity O(N), N: total length of string
#思路: 使用trie 結構來解題, 使用space_inserted 當作新的參數, 來代表目前是否有接字
import collections
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False

class Trie():
    def __init__(self, words):
        self.root = TrieNode()  #自動建立prefix tree
        for w in words:
            if w:  # 注意 words 裡面有可能為 empty string, 過濾空字串, 避免self.root.isEnd = True => self.dfs(self.trie.root, i, w, True) 無限迴圈
                self.insert(w)
    
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.isEnd = True

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.trie = Trie(words)  #建立prefix tree
        res = []
        for w in words:
            if self.dfs(self.trie.root, 0, w, False):
                res.append(w)
        return res

    def dfs(self, node, i, w, space_inserted):
            if i == len(w):
                return node.isEnd and space_inserted  #這裡的space_inserted 來判斷這個字是否有被其他字接過, 好招
            if node.isEnd:
                if self.dfs(self.trie.root, i, w, True):  #斷點, 回到最上層 TrieNode() 開始從頭搜尋, space_inserted 為True, 因為接了一個字
                    return True
            if w[i] not in node.children:
                return False
            else:
                return self.dfs(node.children[w[i]], i + 1, w, space_inserted)


#重寫第二次, time complexity O(N), space complexity O(N), N: total length of string
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isEnd = True
            
    
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            if word: #這句很重要, words 裡面有可能為 empty string, 過濾空字串, 避免自己接自己
                trie.insert(word)
        self.root = trie.root
        res = []
        for word in words:
            if self.helper(word, 0, self.root, res, False):
                res.append(word)
        return res
    
    def helper(self, word, i, node, res, isConcatenated): #有backtracking 的影子
        if node.isEnd:
            if i == len(word) and isConcatenated:
                return True
            else:
                if self.helper(word, i, self.root, res, True):
                    return True
        if i >= len(word) or not node.children.get(word[i]):
            return False
        node = node.children[word[i]]
        return self.helper(word, i+1, node, res, isConcatenated)











# why if self.dfs(self.trie.root, i, w, True), i 不是 i + 1, 因為回到最上層了重新搜索了, 所以i保持原樣

# In the interview I was asked to return the words used for concatenation instead of concatenated words. How would the solution look like then?
import collections
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False

class Trie():
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            if w:  # 注意 words 裡面有可能為 empty string
                self.insert(w)
    
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.isEnd = True

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.trie = Trie(words)  #建立prefix tree
        res = []
        sub = collections.defaultdict(set)
        for w in words:
            if self.dfs(self.trie.root, 0, w, False, "", sub):
                res.append(w)
        print(sub)
        return res 

    def dfs(self, node, i, w, space_inserted, path, sub):
            if i == len(w):
                if node.isEnd and space_inserted:
                    for substring in path.split():
                        sub["".join(path.split())].add(substring)
                    return True
                return False



#不用defaultdict
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie():
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            if w:  # 注意 words 裡面有可能為 empty string
                self.insert(w)
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.trie = Trie(words)
        res = []
        for w in words:
            if self.dfs(self.trie.root, 0, w, False):
                res.append(w)
        return res

    def dfs(self, node, i, w, space_inserted):
            if i == len(w):
                return node.isEnd and space_inserted
            if node.isEnd:
                if self.dfs(self.trie.root, i, w, True):
                    return True
            if w[i] not in node.children:
                return False
            else:
                return self.dfs(node.children[w[i]], i + 1, w, space_inserted)

            if node.isEnd:
                if self.dfs(self.trie.root, i, w, True, path + " ", sub):  
                    return True
            if w[i] not in node.children:
                return False
            else:
                return self.dfs(node.children[w[i]], i + 1, w, space_inserted, path + w[i], sub)


