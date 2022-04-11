'''
You are given a 0-indexed string s that you must perform k replacement operations on. 
The replacement operations are given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.

To complete the ith replacement operation:

Check if the substring sources[i] occurs at index indices[i] in the original string s.
If it does not occur, do nothing.
Otherwise if it does occur, replace that substring with targets[i].
For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this replacement will be "eeecd".

All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other. 
The testcases will be generated such that the replacements will not overlap.

For example, a testcase with s = "abc", indices = [0, 1], 
and sources = ["ab","bc"] will not be generated because the "ab" and "bc" replacements overlap.
Return the resulting string after performing all replacement operations on s.

A substring is a contiguous sequence of characters in a string.

 

Example 1:


Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
Output: "eeebffff"
Explanation:
"a" occurs at index 0 in s, so we replace it with "eee".
"cd" occurs at index 2 in s, so we replace it with "ffff".
Example 2:


Input: s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
Explanation:
"ab" occurs at index 0 in s, so we replace it with "eee".
"ec" does not occur at index 2 in s, so we do nothing.
 

Constraints:

1 <= s.length <= 1000
k == indices.length == sources.length == targets.length
1 <= k <= 100
0 <= indexes[i] < s.length
1 <= sources[i].length, targets[i].length <= 50
s consists of only lowercase English letters.
sources[i] and targets[i] consist of only lowercase English letters.
'''

# First, create a dictionary that maps the index in indexes to its pair of strings in sources and targets.

# Iterate through S, looking up the current index i to see if we can perform a replacement. 
# Take a slice of S at our current index to see if it .startswith() the source string. 
# If so, we perform a "replacement" by adding the target string to our result and incrementing i by the length of the source string.

# If i isn't in indexes then just add a single character to result and move on.


# 刷題用這個, time complexity O(nm), space complexity O(n), n:len(s), m: len(average len of sources)
# 思路: 使用zip 把 indices, sources, targets 連在一起, 利用while loop, i指針 來建立replace 的 string
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        lookup = {i: (src, tgt) for i, src, tgt in zip(indices, sources, targets)}
        i, result = 0, ""
        while i < len(s):
            if i in lookup and s[i:].startswith(lookup[i][0]):
                result += lookup[i][1]
                i += len(lookup[i][0])  #sources will not overlap
            else:
                result += s[i]
                i += 1
        return result


# 重寫第二次, time complexity O(nm), space complexity O(n), n: len(s), m: len(average len of sources)
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        lookup = {idx:(source, target) for idx, source, target in zip(indices, sources, targets)}
        i, result = 0, ""
        while i < len(s):
            if i in lookup and s[i:].startswith(lookup[i][0]): 
                result += lookup[i][1]
                i += len(lookup[i][0])
            else:
                result += s[i]
                i += 1
        return result






