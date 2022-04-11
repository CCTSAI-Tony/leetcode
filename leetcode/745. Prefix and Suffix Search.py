'''
Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. 
If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
 

Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
 

Constraints:

1 <= words.length <= 15000
1 <= words[i].length <= 10
1 <= prefix.length, suffix.length <= 10
words[i], prefix and suffix consist of lower-case English letters only.
At most 15000 calls will be made to the function f.
'''

# 刷題用這個, time complexity: O(NK^2 + QK), space complexity: O(NK), N: len(words), K: maximum len of a word, Q: number of query
# 思路: 建立insert string = suffix放前 再 prefix, 中間放 "#", prefix 是完整的word, suffix 則是切段, 之後search suffix + "#" + prefix
# 技巧: lamda 來快速建立trie
import collections
Trie = lambda: collections.defaultdict(Trie)
class WordFilter:
    def __init__(self, words):
        self.trie = Trie()
        
        for weight, word in enumerate(words):
            for i in range(len(word)+1):
                node = self.trie
                node['weight'] = weight
                word_to_insert = word[i:]+'#'+word
                for c in word_to_insert:
                    node = node[c]
                    node['weight'] = weight
    
    def f(self, prefix, suffix):
        node = self.trie
        for c in suffix + '#' + prefix:
            if c not in node: return -1
            node = node[c]
        return node['weight']

# 重寫第二次, time complexity: O(NK^2 + QK), space complexity: O(NK), N: len(words), K: maximum len of a word, Q: number of query
from collections import defaultdict
trie = lambda: defaultdict(trie)
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = trie()
        for idx, word in enumerate(words):
            for i in range(len(word)):
                node = self.trie
                word_insert = word[i:] + "#" + word
                for c in word_insert:
                    node = node[c]
                    node["idx"] = idx
                    

    def f(self, prefix: str, suffix: str) -> int:
        search_str = suffix + "#" + prefix
        node = self.trie
        for c in search_str:
            if c not in node:
                return -1
            node = node[c]
        return node["idx"]
