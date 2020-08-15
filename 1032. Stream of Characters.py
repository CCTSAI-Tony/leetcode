'''
Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, 
including this letter just queried) spell one of the words in the given list.
 

Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
 

Note:

1 <= words.length <= 2000
1 <= words[i].length <= 2000
Words will only consist of lowercase English letters.
Queries will only consist of lowercase English letters.
The number of queries is at most 40000.
'''



Easily-implemented Python Trie Solution

#思路: 此題的問題是, 若query的當下字母與連續前幾次的query 構成一個字的話, 則當下query 則return True, 注意是連續前幾次喔, 不能斷掉!
#解題: 我們insert word的時候, 是倒序insert, 因為query要query每個字的最後一個字母才有機會加前幾次query可以拚出一個完整單字
#因此我們還要紀錄前幾次query的letter, 來方便執行回朔, 回朔到單字的第一個字則代表回朔成功, 剛好該節點 self.isEnd is True

# Time Complexity:
# waiting.size <= W, where W is the maximum length of words.
# So that O(query) = O(waiting.size) = O(W)
# We will make Q queries, the overall time complexity is O(QW)

# Space Complexity:
# Assume we have initially N words, at most N leaves in the trie.
# The size of trie is O(NW).

# We will make Q queries, the overall space complexity for query stack is O(Q)

import collections
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.isEnd = True

class StreamChecker:
    def __init__(self, words: List[str]):
        self.letters = []  #build up a query stack to store previous query letters
        self.trie = Trie()
        for w in words:
            self.trie.insert(w[::-1])  #倒序插入, 整題重點, 我們從一個字的最後一個字母回推建立prefix tree, 之後query letter, 搭配 query stack 若回朔成功則return True
        
    def query(self, letter: str) -> bool:
        self.letters.append(letter)  
        i = len(self.letters) - 1  #zero based index issue
        node = self.trie.root
        while i >= 0:  #避免index out of range
            if node.isEnd:
                return True
            if not node.children.get(self.letters[i]):
                return False
            node = node.children[self.letters[i]]
            i -= 1  #指針回朔
        return node.isEnd  #記得脫離while loop 還要 return node.isEnd, 這是當 node = node.children[self.letters[0]] 的情況


# StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
# streamChecker.query('a');          // return false
# streamChecker.query('b');          // return false
# streamChecker.query('c');          // return false
# streamChecker.query('d');          // return true, because 'cd' is in the wordlist
# streamChecker.query('e');          // return false
# streamChecker.query('f');          // return true, because 'f' is in the wordlist
# streamChecker.query('g');          // return false
# streamChecker.query('h');          // return false
# streamChecker.query('i');          // return false
# streamChecker.query('j');          // return false
# streamChecker.query('k');          // return false
# streamChecker.query('l');          // return true, because 'kl' is in the wordlist










