'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.
'''


# 刷題用這個
# bonus
# 思路: Manacher's Algorithm O(N) solution 其實不難懂
# 與一般manacher 不一樣在於 a = '@#' + '#'.join(s) + '#$' , 前後要新增不相同的符號來out of while loop, 避免index out of range
# https://medium.com/hoskiss-stand/manacher-299cf75db97e

class Solution:
    def countSubstrings(self, s):
        return sum((v+1)//2 for v in self.manachers(s)) #(v+1)//2 因為 "#"的關係

    def manachers(self, s):
            a = '@#' + '#'.join(s) + '#$' 
            z = [0] * len(a)
            center = right = 0
            for i in range(1, len(a) - 1):
                if i < right:
                    z[i] = min(right - i, z[2 * center - i])
                while a[i + z[i] + 1] == a[i - z[i] - 1]:
                    z[i] += 1
                if i + z[i] > right:
                    center, right = i, i + z[i]
            return z

#z[2 * center - i] means z[current_left]
# manachers(s) is a arrasy, z

# return sum((v+1)//2 for v in manachers(s)) 看圖就知道為什麼了 https://medium.com/hoskiss-stand/manacher-299cf75db97e

#刷題用這個, 參照leetcode 筆記 time complexity O(n)
class Solution:
    def countSubstrings(self, s: str) -> int:
        return sum((v+1)//2 for v in self.manachers(s)) #(v+1)//2 因為 "#"的關係

    def manachers(self, s):
            a = '#' + '#'.join(s) + '#' 
            z = [0] * len(a)
            center = right = 0
            for i in range(1, len(a)-1):
                if i < right:
                    z[i] = min(right - i, z[2 * center - i])
                while i - z[i] - 1 >= 0 and i + z[i] + 1 < len(a) and a[i + z[i] + 1] == a[i - z[i] - 1]:
                    z[i] += 1
                if i + z[i] > right:
                    center, right = i, i + z[i]
            return z


#刷題用這個
#time complexity O(n^2)
#思路: Let N = len(S). There are 2N-1 possible centers for the palindrome:
#we could have a center at S[0], between S[0] and S[1], at S[1], between S[1] and S[2], at S[2], etc. 這個想法有趣!! 不難懂
class Solution:
    def countSubstrings(self, s):
        n = len(s)
        ans = 0
        for center in range(2*n - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:  #這個想法真好
                ans += 1
                left -= 1
                right += 1
        return ans

# Easy to understand Python DP solution

# Disclaimer: This was adapted from geeksforgeeks.
# A DP solution to this problem is to build a table with all possible string[start:end] combinations, 
# storing which are palindromes and which are not (True or False). At any given moment, 
# when you're checking if string[i:j] is a palindrome, you only need to know two things:

# Is string[i] equal to string[j]?
# Is string[i+1:j-1] a palindrome?
# For condition (1), a simple check might do, for condition (2), you use the table. If both conditions are met, mark table[i][j] as True and increase your count.

# Here's the code:

#O(N^2) 
class Solution:
    def countSubstrings(self, s):
        if not s:
            return 0

        n = len(s)
        table = [[False for _ in range(n)] for _ in range(n)]
        count = 0

        # Every isolated char is a palindrome
        for i in range(n):
            table[i][i] = True
            count += 1

        # Check for a window of size 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                table[i][i+1] = True
                count += 1

        # Check windows of size 3 and more
        for k in range(3, n+1):  #window from 3 to n
            for i in range(n+1-k): #(n+1-k) 可以從 k = n 推導出來=> range(1)-> i = 0
                j = i+k-1  #j-i = k-1 ex: window 4(2,3,4,5), 5-2 = 3
                if table[i+1][j-1] and s[i] == s[j]:
                    table[i][j] = True
                    count += 1

        return count


# Python, Straightforward with Explanation  O(N^2)

# We perform a "center expansion" among all possible centers of the palindrome.

# Let N = len(S). There are 2N-1 possible centers for the palindrome: we could have a center at S[0], 
# between S[0] and S[1], at S[1], between S[1] and S[2], at S[2], etc. 這個想法有趣!! 不難懂

# To iterate over each of the 2N-1 centers, we will move the left pointer every 2 times, 
# and the right pointer every 2 times starting with the second(index 1). Hence, left = center // 2, right = center // 2 + center % 2.
# 這裡指right pointer 每經過兩次center變動也要move, 這個規律從right pointer 到達index 1 開始, left pointer 一開始就是這規律

# From here, finding every palindrome starting with that center is straightforward: while the ends are valid and have equal characters, record the answer and expand.













































