'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, 
it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
'''
#use dict, time complexity O(n)
class Solution:
    def findRepeatedDnaSequences(self, s):
        res, dic = [], {}
        for i in range(len(s)-9): #十個字
            if s[i:i+10] not in dic:
                dic[s[i:i+10]] = 1
            elif dic[s[i:i+10]] == 1: #若第一次遇到相同的
                res.append(s[i:i+10])
                dic[s[i:i+10]] = 2 #+1 避免重複
        return res


#use two sets, 消除重複, time complexity O(n)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        repeated, recorded = set(), set()
        for i in range(len(s)-9):
            substring = s[i:i+10]
            if substring in recorded: 
                repeated.add(substring)
            else: 
                recorded.add(substring)
        return list(repeated)


# a = set()
# a.add("AAAAACCCCC")
# a
# a.add("CCCCCAAAAA")
# a
# {'AAAAACCCCC', 'CCCCCAAAAA'}
# list(a)
# ['AAAAACCCCC', 'CCCCCAAAAA']


# 能成為dict的 key, type 有哪些限制
# All of Python’s immutable built-in objects are hashable, while no mutable containers (such as lists or dictionaries) are. 
# Objects which are instances of user-defined classes are hashable by default; they all compare unequal, and their hash value is their id().

# A tuple is immutable

# however list inside a tuple in not ok

# dicked[(1,[3])] = 'qux'  # oops, not allowed



# This method translates a 10-letter-long sequence to a 20-bit long integer, if integer is 4 bytes, then the space needed is O(4n). 
# This method operate one pass, so time complexity is O(n).

# Time O(n) one pass, Space O(4*n) 
# 思路: num = (num*4 + dic[s[i]]) & 0XFFFFF, 每乘4, 最大的值就會進位, 導致 & 0XFFFFF, 直接被filter掉, 模仿固定10 letters window

class Solution:
    def findRepeatedDnaSequences(self, s):
        res = []
        dic = {"A":1, "C":2, "G":3, "T":4}
        dicDNA = {}
        num = 1
        for i in range(len(s)):
            num = (num*4 + dic[s[i]]) & 0XFFFFF #每乘4, 最大的值就會進位, 導致 & 0XFFFFF, 直接被filter掉, 模仿固定10 letters window
            if i < 9:
                continue
            if num not in dicDNA:
                dicDNA[num] = 1
            elif dicDNA[num] == 1:
                res.append(s[i-9:i+1])
                dicDNA[num] = 2
        return res

# Hi. Why use 0XFFFFF ? Thanks!
# the maximum value will be 4 ** 10 - 1 = 0XFFFFF, 4**10-1 => 16**5-1

#自己重寫 time complexity O(n)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dna = {"A":0, "C":1,"G":2,"T":3}
        record = {}
        repeat = []
        num = 0
        for i in range(len(s)):
            num = (num*4 + dna[s[i]]) & 0XFFFFF
            if i < 9:
                continue
            elif num not in record:
                record[num] = 1
            elif record[num] == 1:
                repeat.append(s[i-9:i+1])
                record[num] += 1
        return repeat




