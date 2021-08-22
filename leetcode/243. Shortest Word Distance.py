'''
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, 
return the shortest distance between these two words in the list.

 

Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
 

Constraints:

1 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2

'''

# time complexity O(n), space complexity O(n)
# 思路: greedy and hash table, 不斷刷新該字的最新index
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index_map = {}
        min_distance = float("inf")
        for i, v in enumerate(wordsDict):
            if v == word1 and word2 in index_map:
                min_distance = min(min_distance, i - index_map[word2])
            elif v == word2 and word1 in index_map:
                min_distance = min(min_distance, i - index_map[word1])
            index_map[v] = i
        return min_distance

# 重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index_map = {}
        min_distance = float("inf")
        for i, word in enumerate(wordsDict):
            if word == word1:
                if word2 in index_map:
                    min_distance = min(min_distance, i - index_map[word2])
            elif word == word2:
                if word1 in index_map:
                    min_distance = min(min_distance, i - index_map[word1])
            index_map[word] = i
        return min_distance

