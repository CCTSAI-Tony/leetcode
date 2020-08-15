'''
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, 
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 

Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
'''

# The basic idea is to check each word for prefixes (and suffixes) that are themselves palindromes. 
# If you find a prefix that is a valid palindrome, then the suffix reversed can be paired with the word in order to make a palindrome. 
# It's better explained with an example.

# words = ["bot", "t", "to"]
# Starting with the string "bot". We start checking all prefixes. If "", "b", "bo", "bot" are themselves palindromes. 
# The empty string and "b" are palindromes. We work with the corresponding suffixes ("bot", "ot") 
# and check to see if their reverses ("tob", "to") are present in our initial word list. If so (like the word to"to"), 
# we have found a valid pairing where the reversed suffix can be (prepended) to the current word in order to form "to" + "bot" = "tobot".

# You can do the same thing by checking all suffixes to see if they are palindromes. 
# If so, then finding all reversed prefixes will give you the words that can be (appended) to the current word to form a palindrome.

# The process is then repeated for every word in the list. 
# Note that when considering suffixes, we explicitly leave out the empty string to avoid counting duplicates. 
# That is, if a palindrome can be created by appending an entire other word to the current word, 
# then we will already consider such a palindrome when considering the empty string as prefix for the other word. @@重要不難懂

# hash table, 上面解釋很棒, 刷題用這個
# Worst case time complexity takes O(n * m * m) where n is the length of words and m is the length of word(每個字的長度). why n*m*m 因為還要計算 is_palindrome
# 思路: 若prefix是palindrom, prefix前面加上 suffix[::-1] 就會變成組合palindrom, 若suffix是palindrom, suffix後面加上 prefix[::-1] 就會變成組合palindrom
# 還要排除加到自己的情況ex: [1,1], [2,2], 另外還要避免重複組合, 留下back + word when prefix[:0], 但沒有 word + back when suf[n:], 不然就用set
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words = {word: i for i, word in enumerate(words)}  #build index: word pair
        valid_pals = []
        for word, k in words.items():
            n = len(word)
            for j in range(n+1):  #range(n+1) 才有包含n
                pref = word[:j]  #word[:n] 整段序列, word[:0] empty string
                suf = word[j:]  #perf所對應的suf
                if self.is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words:  #if back != word, 注意不能選自己, 規定要跟別人配對
                        valid_pals.append([words[back],  k])
                if j != n and self.is_palindrome(suf):  #if j != n, 避免重複組合
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        return valid_pals

    def is_palindrome(self, check):
            return check == check[::-1]

# [] == [][::-1], empty string 也是palindrom
# True

# Worst case time complexity takes O(n * m * m) where n is the length of words and m is the length of wordlist(每個字的長度). why n*m*m 因為還要計算 is_palindrome

# Average case time complexity takes O(n * m). As in the average case, the dictionary (aka hashmap) takes a search of O(1) 常數 on average case time complexity.

  
# dict = {1:10,2:20,3:30}
# dict.items()

# dict_items([(1, 10), (2, 20), (3, 30)])

# x = '222'
# x[:100]
# '222'
# len(x)
# 3
# x[:3]
# '222'
# x[3:]
# ''











