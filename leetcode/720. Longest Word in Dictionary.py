'''
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. 
If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
'''

#刷題用這個
# Python: Trie + BFS
# time complexity O(nw), n is length of words, w is the longest length of word.
import collections
class TrieNode(object):
    def __init__(self):
        self.children=collections.defaultdict(TrieNode)
        self.isEnd=False
        self.word =''
        
class Trie(object):
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self, word):
        node=self.root
        for c in word:
            node =node.children[c]
        node.isEnd=True
        node.word=word
    
    def bfs(self):
        q=collections.deque([self.root])
        res=''
        while q:
            cur=q.popleft()  #bfs, 這邊一定要用popleft, 不然回過頭lenth 小的會蓋過lenth 大的, 因為 if len(n.word)>len(res) or n.word<res, res=n.word
            for n in cur.children.values():
                if n.isEnd:  #built one character at a time, 每過一個letter, 若該TrieNode.isEnd = True, 代表有連續字在words 則加進q裡
                    q.append(n)  #add TrieNode
                    if len(n.word)>len(res) or n.word<res:  #n.word < res for lexicographical order
                        res=n.word
        return res 
    
class Solution(object):
    def longestWord(self, words):
        trie = Trie()
        for w in words: 
            trie.insert(w)
        return trie.bfs()




"dog" < "elephant"

True


#修正 pop() and popleft() 都可以work, 修改 if n.is_end 的邏輯句
import collections
class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_end = False
        self.word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for w in word:
            cur = cur.child[w]
        cur.is_end = True
        cur.word = word
    
    def bfs(self):
        q = collections.deque([self.root])
        res = ""
        while q:
            cur = q.pop()  #popleft() 也可以
            for n in cur.child.values():
                if n.is_end:
                    q.append(n)
                    if len(n.word) > len(res):
                        res = n.word
                    elif len(n.word) == len(res) and n.word < res:
                        res = n.word
        return res

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.bfs()








