'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''



# Pure 1D-DP without using stack (python) with detailed explanation, time complexity O(n), space complexity O(n)
# 重點考慮 case 1: ()(), case 2: (()) 
# 思路: 利用dp, dp[i+1] 代表最大的valid lenth ending at s[i], 若s[i] == ")" and s[i-1] == "(", dp[i+1] == 2 + dp[i-1]
class Solution(object):
    def longestValidParentheses(self, s):
        dp = [0 for _ in range(len(s)+1)]  #dp[0] empty string == 0
        max_to_now = 0  #紀錄目前最大值
        for i in range(1,len(s)):  #重點 range(1,len(s)) range 從1開始
            if s[i] == ')':
                # case 1: ()()
                if s[i-1] == '(':
                    # add nearest parentheses pairs + 2
                    dp[i+1] = dp[i-1] + 2
                # case 2: (()) 
                # i-dp[i]-1 is the index of last "(" not paired until this ")" 超酷的這想法!
                elif i-dp[i]-1 >= 0 and s[i-dp[i]-1] == "(":  #if dp[i] = 0 => s[i-1] == "(", 被if condition 優先考慮掉了
                    # add nearest parentheses pairs + 2 + parentheses before last paired "("
                    dp[i+1] = dp[i] + 2 + dp[i-dp[i]-1]   
                    
                max_to_now = max(max_to_now, dp[i+1]) #這樣做可以避免 input = ""
        return max_to_now

#自己重寫, 36ms 96.67%, time complexity O(n), space complexity O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        max_valid = 0
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i+1] = dp[i-1] + 2
                else:
                    if i - dp[i] -1 >= 0 and s[i-dp[i]-1] == "(":
                        dp[i+1] = dp[i] + 2 + dp[i-dp[i]-1]
                max_valid = max(max_valid, dp[i+1])
            
        return max_valid


#重寫*2
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        max_len = 0
        dp = [0] * (len(s)+1)
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i+1] = dp[i-1] + 2
                elif i-dp[i]-1 >= 0 and s[i-dp[i]-1] == "(":
                    dp[i+1] = dp[i] + 2 + dp[i-dp[i]-1]
            max_len = max(max_len, dp[i+1])
        return max_len

#重寫第三次, time complexity O(n), space complexity O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i+1] = dp[i-1] + 2
                elif i - dp[i] - 1 >= 0 and s[i - dp[i] - 1] == "(":
                    dp[i+1] = dp[i] + 2 + dp[i - dp[i] - 1]
        return max(dp)

#重寫第四次, time complexity O(n), space complexity O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        max_to_now = 0
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i+1] = dp[i-1] + 2
                elif i - dp[i] - 1 >= 0 and s[i - dp[i] - 1] == "(":
                    dp[i+1] = 2 + dp[i] + dp[i - dp[i] - 1]
                max_to_now = max(max_to_now, dp[i + 1])
        return max_to_now

# list comprehension  兩種功能一樣
# [[0]*5 for _ in range(5)]

# [[0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0]]

# [[0 for _ in range(5)] for _ in range(5)]

# [[0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0]]






# python O(n) with stack, beat 93.66%
# 這題思路: 存"(", 之後遇到")" 則pair給他, 若empty stack, 沒有"(" 但遇到 ")"的話 則移動leftmost 略過它, 因為不能成為valid parenthesis, 若")" 不夠全部stack pair, 則pair相對應的數目
class Solution(object):
    def longestValidParentheses(self, s):
        if not s or len(s) < 2: 
            return 0
        stack = []
        leftmost = -1  #why -1, 因為zero based index
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else: # case ')'
                if not stack: # not valid parenthesis, update leftmost
                    leftmost = i
                else:
                    stack.pop()
                    if not stack: # stack is empty 配對完了, length is i - leftmost, 連續的substring
                        res = max(res, i - leftmost) 
                    else: # otherwise, length is i - last index of stack
                        res = max(res, i - stack[-1]) #這裡stack[-1] 是pop掉的前一個
        return res

#()()()() leftmost不會變
#(((())))
#(())(())

# "(()" 此case 若沒有 res = max(res, i - stack[-1]) 這行 則答案不正確








