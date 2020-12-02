'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
'''

#follow up, 刷題用這個, time complexity O(n), space complexity O(1)
class Solution(object):
    def backspaceCompare(self, S1, S2):
        r1 = len(S1) - 1 
        r2 = len (S2) - 1
        
        while r1 >= 0 or r2 >= 0:
            char1 = char2 = ""
            if r1 >= 0:
                char1, r1 = self.getChar(S1, r1)
            if r2 >= 0:
                char2, r2 = self.getChar(S2, r2)
            if char1 != char2:
                return False
        return True
        
    
    def getChar(self, s , r):
        char, count = '', 0
        while r >= 0 and not char:
            if s[r] == '#':
                count += 1
            elif count == 0:
                char = s[r]
            else:
                count -= 1
            r -= 1
        return char, r

#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        r1, r2 = len(S) - 1, len(T) - 1
        while r1 >= 0 or r2 >= 0:
            char1 = char2 = ""
            if r1 >= 0:
                r1, char1 = self.getChar(r1, S)
            if r2 >= 0:
                r2, char2 = self.getChar(r2, T)
            print(char1, char2)
            if char1 != char2:
                return False
        return True
    
    def getChar(self, r, s):
        count = 0
        char = ""
        while r >= 0 and not char:
            if s[r] == "#":
                count += 1
            elif count == 0: #切記這裏不能用if, logic是綁在一起的
                char = s[r]
            else:
                count -= 1
            r -= 1
        return r, char


#自己想的, time complexity O(n), space complexity O(n)
#思路: stack
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1 = []
        for i in range(len(S)):
            if S[i] == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(S[i])
        S_new = "".join(stack1)
        
        stack2 = []
        for i in range(len(T)):
            if T[i] == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(T[i])
        T_new = "".join(stack2)
        return S_new == T_new