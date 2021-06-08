'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''

Easy to Understand Python Solution, 2 pointer time complexity O(n)

We can use the standard two-pointer approach that starts at the left and right of the string and move inwards. 
Whenever there is a mismatch, we can either exclude the character at the left or the right pointer. 
We then take the two remaining substrings and compare against its reversed and see if either one is a palindrome.

#time complexity O(n)
#思路: 利用2 pointers 比較, 若左右遇到不相符的, 左邊往右跳一格, or 右邊往左跳一格, 再個別比較剩下的字串是否是palindrom
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        left, right = 0, len(s) - 1
        while left < right: # <= 也可以, 但不必要
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1] 
                return one == one[::-1] or two == two[::-1]  #只能刪一字 所以若刪左or 刪右 都不是palindrom 則return False
            left, right = left + 1, right - 1
        return True #原本字串就是palindrom 不需刪任何一個字

#abcdedcbha one: bcdedcb  two: cdedcbh

#這題利用到 inward string of a palindrom 依舊是個palindrom 的特性, 還有palindrome = palindrome[::-1]

#time complexity O(n), space complexity O(1)
#注意s[3:-1:-1] => "", 為什麼, 因為在string index, -1 = len(s) - 1
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return (s[l+1: r+1] == s[l+1: r+1][::-1]) or (s[l:r][::-1] == s[l:r])
            l += 1
            r -= 1
        return True










