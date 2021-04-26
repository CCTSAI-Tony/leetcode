'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
'''

#自己想的, time complexity O(n), space complexity O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for string in s.split():
            res.append(string[::-1])
        return " ".join(res)

#自已想的, time complexity O(n), space complexity O(n), sliding window
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        temp = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " and temp:
                res.append(temp)
                temp = ""
            else:
                temp += s[i]
        if temp:
            res.append(temp)
        return " ".join(res[::-1])

