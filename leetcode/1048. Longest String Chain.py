'''
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA 
without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, 
where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

 

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.
'''



'''
Initially, each word's longest chain is set to 1. Then, we loop the list of words to find out whether it has a predecessor in the list. 
If there is a predecessor, we know current word's longest chain could be predecessor's longest chain plus one.

There are two main points for this solution:

Sort the word list words by each length of the word.
As mentioned above, current word's longest chain is formed by predecessor's longest chain plus one. 
Therefore, we must calculate the predecessor's longest chain first, otherwise the answer would be incorrect.

Comparing the current word's chain with all its predecessor's longest chain plus one to find out the current word's longest chain.
This is because the current word's chain could possibly be formed in many different ways, so we need to compare them to find out the longest one.
'''


# 刷題用這個, time complexity O(N*K^2) Here, N - number of words, K - length of longest word
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        d = dict()
        for word in words:
            d[word] = 1
        longest = 1
        for word in sorted(words, key=len):
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                if prev in d:
                    d[word] = max(d[word], d[prev] + 1)
            longest = max(longest, d[word])
        return longest

# 重寫第二次, time complexity O(n*k^2), space complexity O(n)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        chain_map = {word:1 for word in words}
        longest_chain = 0
        for word in words:
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in chain_map:
                    chain_map[word] = max(chain_map[word], chain_map[prev] + 1)
                longest_chain = max(longest_chain, chain_map[word])
        return longest_chain













