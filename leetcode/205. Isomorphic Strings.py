'''
Given two strings s and t, determine if they are isomorphic.(同型的)

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''
class Solution:
    def isIsomorphic1(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i] #builds up 'character:index', []+[i] = [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values()) #因為字典無排序功能, 所以使用sorted排序


# class Solution:
#     def isIsomorphic1(self, s, t):
#         d1, d2 = {}, {}
#         for i, val in enumerate(s):
#             d1[val] = d1.get(val, []) + [i] 
#         for i, val in enumerate(t):
#             d2[val] = d2.get(val, []) + [i]
#         print( sorted(d1.values()))
#         print( sorted(d2.values()))

# a = Solution()
# s = 'book'
# t = 'cook'
# a.isIsomorphic1(s,t)

# [[0], [1, 2], [3]]
# [[0], [1, 2], [3]]

# a = (1, 11, 2)
# x = sorted(a)
# print(x)

# [1, 2, 11]

class Solution:
    def isIsomorphic2(self, s, t):
        d1, d2 = [[] for _ in range(256)], [[] for _ in range(256)]
        for i, val in enumerate(s):
            d1[ord(val)].append(i)
        for i, val in enumerate(t):
            d2[ord(val)].append(i)
        return sorted(d1) == sorted(d2)


# ord('A')
# 65

# d1 = [[] for i in range(6)]
# d1
# [[], [], [], [], [], []]

# d1[2].append(2)
# d1
# [[], [], [2], [], [], []]

# sorted(d1)
# [[], [], [], [], [], [2]]








