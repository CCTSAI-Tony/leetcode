'''
Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, 
it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

 

Example 1:

Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
 

Note:

1 <= wordlist.length <= 5000
1 <= queries.length <= 5000
1 <= wordlist[i].length <= 7
1 <= queries[i].length <= 7
All strings in wordlist and queries consist only of english letters.
'''

#自己想的, time complexity O(n), space complexity O(n)
#思路: hash table 與set 來應付不同狀況 
from collections import defaultdict
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words = defaultdict(list)
        same_words = defaultdict(list)
        match_words = set(wordlist)
        for word in wordlist:
            same_words[word.lower()].append(word)
        vowes = ['a', 'e', 'i', 'o', 'u']
        for word in wordlist:
            word_list = list(word.lower())
            for i in range(len(word_list)):
                if word_list[i] in vowes:
                    word_list[i] = "_"
            temp = "".join(word_list)
            words[temp].append(word)
        res = []
        for query in queries:
            if query in match_words:
                res.append(query)
            elif query.lower() in same_words:
                res.append(same_words[query.lower()][0]) #return 相同字 case insensitive 第一個match的字
            else:
                query = list(query.lower())
                for i in range(len(query)):
                    if query[i] in vowes:
                        query[i] = "_"
                query = "".join(query)
                if query in words:
                    res.append(words[query][0]) #return 修改vowes 第一個match的字
                else:
                    res.append("")
        
        return res





















