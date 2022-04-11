'''
This is an interactive problem.

You are given an array of unique strings wordlist where wordlist[i] is 6 letters long, and one word in this list is chosen as secret.

You may call Master.guess(word) to guess a word. 
The guessed word should have type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, 
representing the number of exact matches (value and position) of your guess to the secret word. 
Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have exactly 10 guesses to guess the word. 
At the end of any number of calls, if you have made 10 or fewer calls to Master.guess and at least one of these guesses was secret, 
then you pass the test case.

 

Example 1:

Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"], numguesses = 10
Output: You guessed the secret word correctly.
Explanation:
master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
Example 2:

Input: secret = "hamada", wordlist = ["hamada","khaled"], numguesses = 10
Output: You guessed the secret word correctly.
 

Constraints:

1 <= wordlist.length <= 100
wordlist[i].length == 6
wordlist[i] consist of lowercase English letters.
All the strings of wordlist are unique.
secret exists in wordlist.
numguesses == 10
'''

# Same as other solutions - repeatedly choose a word to guess and eliminate all words that do not have the same number of matches as the
# chosen word.

# To choose a word, calculate a matrix counting the number of words where each char is in each position. 
# Then score each word by adding the number of words that have the same chars in the same positions.

# So this is O(n * 10) = O(n) time and not O(n^2) because I don't check all pairs.
# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: repeatedly choose most_overlap_word, 這樣可以有效過濾大部分不適合的candidates, 只留下與guess結果相同match的word
class Solution:
    def findSecretWord(self, wordlist, master):

        def pair_matches(a, b):        
            return sum(c1 == c2 for c1, c2 in zip(a, b))

        def most_overlap_word():
            counts = [collections.defaultdict(int) for _ in range(6)]  # dict for every position
            for word in candidates:
                for i, c in enumerate(word):
                    counts[i][c] += 1
            return max(candidates, key=lambda x:sum(counts[i][c] for i, c in enumerate(x)))

        candidates = wordlist[:]        
        while candidates:
            s = most_overlap_word()     
            matches = master.guess(s)  # 呼叫超過10次, leetcode 會直接停止
            if matches == 6:
                return
            candidates = [w for w in candidates if pair_matches(s, w) == matches]   # filter words with same matches

# 重寫第二次, time complexity O(n * 10) = O(n), space complexity O(n)
from collections import defaultdict
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        candidates = wordlist[:]
        while candidates:
            s = self.most_overlap_word(candidates)
            match = master.guess(s)
            if match == 6:
                return
            candidates = [word for word in candidates if self.pair_matches(word, s) == match]
    
    
    def pair_matches(self, a, b):
        return sum(c1 == c2 for c1, c2 in zip(a, b))
    
    def most_overlap_word(self, candidates):
        counts = [defaultdict(int) for _ in range(6)]
        for word in candidates:
            for i, ch in enumerate(word):
                counts[i][ch] += 1
        return max(candidates, key=lambda x: sum(counts[i][c] for i, c in enumerate(x)))






