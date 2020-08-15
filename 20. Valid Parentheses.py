# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop(): #取stack最後一個
                    return False
            else:  #不为key也不为value
                return False  
        return stack == []# ex: (({  return false

#為什麼配對成功stack還是空的 因為stack.pop()

'''
1.创建一个字典，把正括号存为value,反括号存为key--
2.遍历这个字符串：
--判断是否为value:
如果存在
保存value，
如果不存在判断是否为Key，
若为Key:
>若直接输入反括号且stack=[] 返回false
>若这个key与stack弹出值不相等 返回false
不为key也不为value:
>false
3.遍历结束后，判断是否为空”如果直接输入[/{/( ，只循环一次就结束循环，且stack不为空 ，所以只能用stack判断“
'''

#自己重寫, time complexity O(n), 刷題用這個, 指針應用搭配stack
#思路: 遇到closoing bracket, 若stack.pop() 不是對應的另一半, 就return False, 因為不能([)] 一定要 ([{}]), 大包小, 對應的一定要優先pop出來
#最後若stack 有殘餘沒配對成功的 要return False
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack= []
        for i in range(len(s)):
            if s[i] == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif s[i] == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif s[i] == "]":
                if not stack or stack.pop() != "[":
                    return False
            else:
                stack.append(s[i])
        if not stack:
            return True




