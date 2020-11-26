'''
Design a data structure that is initialized with a list of different words. Provided a string, 
you should determine if you can change exactly one character in this string to match any word in the data structure.

Implement the MagicDictionary class:

MagicDictionary() Initializes the object.
void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
bool search(String searchWord) Returns true if you can change exactly one character in searchWord to match any string in the data structure, otherwise returns false.
 

Example 1:

Input
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
Output
[null, null, false, true, false, false]

Explanation
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // return False
magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello" so we return True
magicDictionary.search("hell"); // return False
magicDictionary.search("leetcoded"); // return False
 

Constraints:

1 <= dictionary.length <= 100
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case English letters.
All the strings in dictionary are distinct.
1 <= searchWord.length <= 100
searchWord consists of only lower-case English letters.
buildDict will be called only once before search.
At most 100 calls will be made to search.
'''

#刷題用這個, time complexity O(n), space complexity O(n)
#思路: 利用trie 來建構, 並遍歷searchWord, 初始remain = 1 當word結束時 看是否remain = 0 => return True
from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.isAend = False
        self.contains = defaultdict(TrieNode)

class MagicDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        r = self.root
        for chr in word:
            r = r.contains[chr]
        r.isAend = True

    def findWord(self, remain, r, word): #O(n)
        if not word:
            return True if remain == 0 and r.isAend else False
        for key in r.contains.keys():
            if key == word[0]:
                if self.findWord(remain, r.contains[key], word[1:]):
                    return True
            elif remain == 1:
                if self.findWord(0, r.contains[key], word[1:]):
                    return True
        return False

    def buildDict(self, dictionary):
        for word in dictionary:
            self.addWord(word)

    def search(self, searchWord):
        return self.findWord(1, self.root, searchWord)



#自己重寫, time complexity O(n), space complexity O(n)
from collections import defaultdict
class TrieNode:
    def __init__(self): 
        self.child = defaultdict(TrieNode)
        self.isWord = False
               
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.child[w]
        node.isWord = True  
        
        
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)
        
    def find(self, remain, node, word):
        if not word:
            if remain == 0 and node.isWord:
                return True
            return False
        
        for key in node.child:
            if key == word[0]:
                if self.find(remain, node.child[key], word[1:]):
                    return True
            elif remain == 1:  #記得要elif
                if self.find(0, node.child[key], word[1:]):
                    return True
        return False
        

    def search(self, searchWord: str) -> bool:
        node = self.trie.root
        return self.find(1, node, searchWord)














