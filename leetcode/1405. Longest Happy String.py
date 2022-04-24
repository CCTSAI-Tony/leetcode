'''
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. 
If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0
'''

# The algorithm is as follows:

# At each step, sort {a, b, c}.
# Append the largest valid character (if there're more than one choice, pick any of them) to the answer. 
# "Valid" means appending the character won't form three repeating characters.
# Update remaining {a, b, c}.
# Repeat step 1-3 until there's no valid character that can be appended.

# 刷題用這個, time complexity O(nlog3), space complexity O(n)
# 思路: greedy, 2. 都選count 最多的letter, 若已連續兩個相同, 再選count次多的, count都等於0 無法選了, 立即return ans
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = [[a, 'a'], [b, 'b'], [c, 'c']]
        ans = []
        while True:
            s.sort()
            i = 1 if len(ans) >= 2 and ans[-2] == ans[-1] == s[2][1] else 2
            if s[i][0]:
                ans.append(s[i][1])
                s[i][0] -= 1
            else:
                break
        return ''.join(ans)


# 重寫第二次, time complexity O(nlog3), space complexity O(n)
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = [[a, "a"], [b, "b"], [c, "c"]]
        ans = []
        while True:
            s.sort()
            i = 1 if len(ans) >= 2 and s[-1][1] == ans[-1] == ans[-2] else 2
            if s[i][0]:
                ans.append(s[i][1])
                s[i][0] -= 1
            else:
                break
        return "".join(ans)








