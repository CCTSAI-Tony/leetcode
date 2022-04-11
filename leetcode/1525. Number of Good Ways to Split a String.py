'''
ou are given a string s.

A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is equal to s 
(i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.

Return the number of good splits you can make in s.

 

Example 1:

Input: s = "aacaba"
Output: 2
Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
Example 2:

Input: s = "abcd"
Output: 1
Explanation: Split the string as follows ("ab", "cd").
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''

# Have two dicionaries to track the frequency of letters for the left partition and the right partition. 
# Initially, left partion will be empty. For each loop, update both dictionaries to reflect the frequency on the left and right partition. 
# If the length of both partitions are equal, we found the good ways, so increment the result.

# 刷題用這個, time complexity O(n), space complexity O(n)
# 思路: 使用 左右 Counter
from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        cnt = 0
        left = Counter()
        right = Counter(s)
        for c in s:
            left[c] += 1
            right[c] -= 1
            if right[c] == 0:
                del right[c]
            if len(left) == len(right):
                cnt += 1
        return cnt


