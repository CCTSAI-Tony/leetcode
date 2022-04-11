'''
With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
word contains the first letter of puzzle.
For each letter in word, that letter is in puzzle.
For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage", while
invalid words are "beefed" (does not include 'a') and "based" (includes 's' which is not in the puzzle).
Return an array answer, where answer[i] is the number of words in the given word list words that is valid with respect to the puzzle puzzles[i].
 

Example 1:

Input: words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]
Explanation: 
1 valid word for "aboveyz" : "aaaa" 
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There are no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.
Example 2:

Input: words = ["apple","pleas","please"], puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
Output: [0,1,3,2,0]
 

Constraints:

1 <= words.length <= 105
4 <= words[i].length <= 50
1 <= puzzles.length <= 104
puzzles[i].length == 7
words[i] and puzzles[i] consist of lowercase English letters.
Each puzzles[i] does not contain repeated characters.
'''

# 刷題用這個, time complexity O(N, M * N), N: all letters in words, M: all letters in puzzles
# 思路: 此題利用trie 來計算valid words for specific puzzle
# words can have duplicate word, that's why we need self.count
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        node = self.root
        for w in word:
            node = node.child[w]
        node.count += 1
        
    def search(self, word) -> int:
        def dfs(node, found: bool = False) -> int:
            res = node.count * found
            for w in word:
                if w in node.child:
                    res += dfs(node.child[w], found or w == word[0])
            return res
        return dfs(self.root)
            

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.add(word)
        return [trie.search(word) for word in puzzles]

