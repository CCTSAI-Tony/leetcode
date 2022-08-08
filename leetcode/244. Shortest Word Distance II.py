'''
Design a data structure that will be initialized with a string array, 
and then it should answer queries of the shortest distance between two different strings from the array.

Implement the WordDistance class:

WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.
 

Example 1:

Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]

Explanation
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding");    // return 1
 

Constraints:

1 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
At most 5000 calls will be made to shortest.
'''


# 刷屜用這個, time complexity O(n), space complexy O(n)
# 思路: 使用dict 來紀錄相同字詞所有的位置, 再遍歷兩個不同字詞的所有差距組合, 誰大 就優先移動較小的字詞
from collections import defaultdict
class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.locations = defaultdict(list)

        # Prepare a mapping from a word to all it's locations (indices).
        for i, w in enumerate(words):
            self.locations[w].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        loc1, loc2 = self.locations[word1], self.locations[word2]
        l1, l2 = 0, 0
        min_diff = float("inf")

        # Until the shorter of the two lists is processed
        while l1 < len(loc1) and l2 < len(loc2):
            min_diff = min(min_diff, abs(loc1[l1] - loc2[l2]))
            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1
        return min_diff

# 重寫第二次, time complexity O(n), space complexity O(n)
from collections import defaultdict
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.map = defaultdict(list)
        for i, v in enumerate(wordsDict):
            self.map[v].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        min_dis = float("inf")
        i1, i2 = 0, 0
        list1 = self.map[word1]
        list2 = self.map[word2]
        while i1 < len(list1) and i2 < len(list2):
            min_dis = min(min_dis, abs(list1[i1] - list2[i2]))
            if list1[i1] > list2[i2]:
                i2 += 1
            else:
                i1 += 1
        return min_dis