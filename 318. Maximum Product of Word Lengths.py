'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. 
You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
'''
# Algorithm

# Simple brute force solution is to test if every pair for similarity and take the product if they are not similar. 
# Return the maximum product if several dissimilar pairs are found otherwise return 0.
# First optimization is to run the two for loops from** i = (0 to N-1) and j = (i+1, N-1)**. This is lesser than N^2.
# How do we find if two words are similar?

# First approach will be to take two words, put all characters into a set and test for membership in that set for the other words. 
# Can we do better? Can we pre-process somehow?
# Second approach will be to prepprocess each word and generate a unique sign for it. 
# Take a boolean array of 26. Mark the position for every character in this word as True. 
# Now traverse this array in order and generate a unique signature. runtime: O(26 + len(word)). Can we still do better?
# Can we use bit-wise manipulation? int32 is 32 bits. There are 26 letters. Set a bit for every character. 
# How do you test if two words have no similar letters? Just AND them. Testing them now becomes a constant time operation
# 00000000100010010010001000 >代表一個值
# zyxwvutsrqponmlkjihgfedcba

#bit manipulation, time complexity O(n^2), n: len(words)
#思路: 利用雙指針來回遍歷words來尋找pairs, 如何判斷這兩個字有無重疊letter, 利用bit 來模仿26的字母
#若該字母有出現在該字中, 則對應的bit 變成1, 兩個dissimilar 的字, 使用 AND == 0, 若!= 0, 則代表這兩字有共通letter
#技巧: 利用| or 來mark 出現的字母, 這樣一來重複的字母也不會改變出現的事實
class Solution(object):
    def maxProduct(self, words):
        signature = [self.sign(x) for x in words]  #儲存每個word的特徵值 list comprehension
        max_product, N = 0, len(words)
        for i in range(N):  
            for j in range(i+1, N):  # 最後 i = n-1, i+1 = (n-1)+1 = n, range(n,n) == None
                if signature[i] & signature[j] == 0: #兩者沒同時為1的bit, 兩者沒共通, 注意不要搞混!! 這裡不能是 if signature[i] != signature[j]: 不同的數字有可能有共通的1 bita
                    max_product = max(max_product, len(words[i])*len(words[j]))
        return max_product

    def sign(self, word):
        value = 0
        for c in word:
            value = value | (1 << (ord(c)-97))  #ord('a') == 97, |  OR  Sets each bit to 1 if one of two bits is 1
        return value

#自己重寫, 436ms, 刷題用這個
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        sign = [self.signed(i) for i in words]
        max_product = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if sign[i] & sign[j] == 0:
                    max_product = max(max_product, len(words[i])*len(words[j]))  
        return max_product
    
    def signed(self, word):
        sign = 0
        for w in word:
            sign |= (1 << (ord(w) - 97))
        return sign

#自己重寫TLE, 應該要先把所有字轉換成sign, 不然過多重複計算
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_product = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if self.signed(words[i]) & self.signed(words[j]) == 0:
                    max_product = max(max_product, len(words[i])*len(words[j]))  
        return max_product
    
    def signed(self, word):
        sign = 0
        for w in word:
            sign |= (1 << (ord(w) - 97))
        return sign




# Use set as a signature
# Yes another way is to use sets in an interesting manner.

# Use this for generating signatures: signature = {w:set(w) for w in words}
# Use this for testing: bool(signature[words[i]] & signature[words[j]]) == False
# https://docs.python.org/2/library/sets.html

#time complexity O(n^2)
#思路: 利用set交集來檢驗是否有共通字母
class Solution(object):
    def maxProduct(self, words):
        signature = {w:set(w) for w in words}  #dict comprehension
        max_product, N = 0, len(words)
        for i in range(N):
            for j in range(i+1, N):
                # Intersection of two sets
                if bool(signature[words[i]] & signature[words[j]]) == False:
                    max_product = max(max_product, len(words[i])*len(words[j]))
        return max_product   

a = {2,3,4}
b = {2,6,7}
a & b
{2}
bool(a & b)
True

a = {2,3,4}
b = {1,6,7}
bool(a & b)
False
a & b
set()
















