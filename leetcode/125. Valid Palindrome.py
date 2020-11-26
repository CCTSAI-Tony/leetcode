'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

'''
#Python in-place two-pointer solution
#time complexity O(n)
#思路: 利用 isalnum() 來過濾非數字or字母字串, 設左右指針遇到字母or數字=>左右比對是否相等, 若是就再左右內縮check
class Solution:
    def isPalindrome(self, s):
        if not s: 
            return True
        l, r = 0, len(s)-1
        while l <= r: #l = r palindrom pivotal character
            while l < r and not s[l].isalnum(): # 若s[l]不是字母與數字 也就是空格, 其他符號等
                l += 1
            while l < r and not s[r].isalnum(): # ex: s = ".," 答案是 True 注意這邊不能 <=, 不然下面 s[l].lower() or s[r].lower() 會 string index out of range
                r -= 1
            if s[l].lower() != s[r].lower(): #按順序比對
                return False
            l +=1; r -= 1
        return True

'''
Python isalnum() 方法检测字符串是否由字母和数字组成。
返回值
如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False