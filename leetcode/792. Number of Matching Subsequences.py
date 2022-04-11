'''
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) 
deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
 

Constraints:

1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
'''

'''
I begin by creating a default dictionary of 'list' objects. 
The main benefit of a default dictionary is that when you access an entry that does not yet exist, 
the entry is created automatically (in this case, the value for the entry is an empty list when it is created). 
I then create a 'count' variable to keep track of the number of words that are subsequences of the given string.

The first thing I do with the dictionary is populate it with all the words in the list of words. 
The key for each entry is the first letter of the word. The value is the list of words that start with that letter. 
Using the example in the problem, the dictionary would look like the following:

{'a': ['a', 'acd', 'ace'], 'b': ['bb']}

The next step is to iterate through each character in the given string. For each character, 
I access the dictionary to retrieve the list of words that start with that character. 
I reset the value of the entry to an empty list and then iterate through the list of words I retrieved. 
If the word is only a single letter, 
then I conclude that we have successfully found a completed subsequence and increase our 'count' by one. Otherwise, 
I slice off the first character and add the sliced word back to the dictionary. 
This time, it is added to the entry for which the key is equal to the first letter of the sliced word.

This process continues until we have iterated through all characters in the string. At the end, I return the count.
'''

# 刷題用這個, time complexity O(n + m), space complexity O(m), n: len(S), m: all letters of words
# 思路: 利用dict 來存儲每個對應首字母的word, 再遍歷s每個字母來找尋對應的subsequences, 每次遍歷要存回扣掉首字母的剩餘字串, 直到只剩一個字母, count += 1
from collections import defaultdict
class Solution(object):
    def numMatchingSubseq(self, s, words):
        word_dict = defaultdict(list)
        count = 0
        
        for word in words:
            word_dict[word[0]].append(word)            
        
        for char in s:
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence! 
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        
        return count


# 刷題用這個, time complexity O(n + m), space complexity O(m), n: len(S), m: all letters of words
# 思路: 跟上面是一樣的, 只是使用iter 與 next 來取代word slicing
class Solution(object):
    def numMatchingSubseq(self, s, words):
        ans = 0
        heads = [[] for _ in range(26)]
        for word in words:
            it = iter(word)
            heads[ord(next(it)) - ord('a')].append(it)

        for letter in s:
            letter_index = ord(letter) - ord('a')
            old_bucket = heads[letter_index]
            heads[letter_index] = []

            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                if nxt:
                    heads[ord(nxt) - ord('a')].append(it)
                else:
                    ans += 1
        return ans

# 刷題用這個
# 重寫第二次, time complexity O(n + m), space complexity O(m), n: len(s), m: all letters of words
from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        match_map = defaultdict(list)
        for word in words:
            it = iter(word)
            match_map[next(it)].append(it)
        for c in s:
            old_match = match_map[c]
            match_map[c] = []
            for word_it in old_match:
                nxt = next(word_it, None)
                if not nxt:
                    count += 1
                else:
                    match_map[nxt].append(word_it)
        return count


