'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2
 

Constraints:

1 <= s.length <= 2000
s consits of lower-case and/or upper-case English letters only.
'''

#自己想的, time complexity O(n)
#思路: 設一個set 紀錄之前出現過的ch, 若之後遇到一樣的變成pair, 代表可以變成palindrom 的一部分, count + 2, set 刪掉該元素, 依照這邏輯遍歷整個s
#若遍歷完, set還有元素, 代表有沒法配對的元素, return count + 1, 因為中間元素可以為任一個, 若set無元素, return count, len(palindrom) => even
class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = set()
        count = 0
        for ch in s:
            if ch in letters:
                count += 2
                letters.remove(ch)
            else:
                letters.add(ch)
        if letters:
            return count + 1
        return count




        