'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''


#刷題用這個, time complexity O(n), space complexity O(n)
#思路: 利用Counter 來計算frequency, defaultdict(str) 來存儲相同frequency 的字串, 最後遍歷defaultdict 從frequency len(s) 遍歷到 1, 合成一字串return
from collections import Counter, defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        freq = defaultdict(str)
        for k, v in counts.items():
            freq[v] += k*v
        return "".join([freq[s] for s in range(len(s), 0, -1)])



#自己想的, time complexity O(nlogn), space complexity O(n)
#思路: 利用Counter 來計算frequency, 並利用sort 來排序, 相同的字要排在一起
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        temp = list(s)
        temp.sort(key=lambda x: (-counts[x], x))
        return "".join(temp)
