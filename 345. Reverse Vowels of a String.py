'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''

# 2 pointer, 自己想的
class Solution:
    def reverseVowels(self, s: str) -> str:
        p = list(s)
        temp = []
        vow = ["a","e","i","o","u","A","E","I","O","U"]
        for i, v in enumerate(p):
            if v in vow:
                temp.append(i)
        n = len(temp)
        for i in range(n//2):
            p[temp[i]], p[temp[-i-1]] = p[temp[-i-1]], p[temp[i]]
        
        return "".join(p)