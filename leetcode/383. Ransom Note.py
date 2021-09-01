'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

# a = "12344"
# b = ",".join(a)
# b.split(",")
# ['1', '2', '3', '4', '4']

# ",".join(a).split(",")
# ['1', '2', '3', '4', '4']

#28ms
class Solution(object):  
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True



import collections 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        myM=collections.Counter(magazine)
        myR=collections.Counter(ransomNote)
        
        for char,count in myR.items():
            if myM[char]<count:
                return False
        return True


# 重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_map = {}
        for s in magazine:
            if s not in m_map:
                m_map[s] = 1
            else:
                m_map[s] += 1
        for s in ransomNote:
            if s not in m_map:
                return False
            else:
                m_map[s] -= 1
            if m_map[s] < 0:
                return False
        return True


# import collections
# a = "qwerrtorrjffm"
# aa = collections.Counter(a)
# aa
# Counter({'q': 1,
#          'w': 1,
#          'e': 1,
#          'r': 4,
#          't': 1,
#          'o': 1,
#          'j': 1,
#          'f': 2,
#          'm': 1})
# aa.items()
# dict_items([('q', 1), ('w', 1), ('e', 1), ('r', 4), ('t', 1), ('o', 1), ('j', 1), ('f', 2), ('m', 1)])



#參考別人想的  80ms
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = {}
        mag = {}
        for i in ransomNote:
            ran[i] = ran.get(i,0) + 1
        for i in magazine:
            mag[i] = mag.get(i,0) + 1
        
        for i in ransomNote:
            if ran.get(i,0) > mag.get(i,0):
                return False
        return True


#自己想的 超爛的 536ms
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if not ransomNote:
            return True
        
        ran = ",".join(ransomNote).split(",")
        mag = ",".join(magazine).split(",")
        for i in range(len(ran)):
            for j in range(len(mag)):
                if mag[j] == ran[i]:
                    mag[j] = "#"
                    break
        count = 0
        for i in mag:
            if i == "#":
                count += 1
        
        if count == len(ran):
            return True
        return False

       








