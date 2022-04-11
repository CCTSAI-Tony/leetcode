'''
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, 
causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
 

Constraints:

1 <= s.length <= 105
2 <= k <= 104
s only contains lower case English letters.
'''

# 刷題用這個, time complexity O(n)
# 思路: 使用stack 
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []  # pair of (character, frequence)
        for c in s:
            if st and st[-1][0] == c:
                st[-1][1] += 1  # Increase the frequency
            else:
                st.append([c, 1])
            if st[-1][1] == k:  # If reach enough k duplicate letters -> then remove
                st.pop()
        return "".join(c * f for c, f in st)


# 
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][-1] += 1
                if stack[-1][-1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return "".join([c * k for c, k in stack])


















