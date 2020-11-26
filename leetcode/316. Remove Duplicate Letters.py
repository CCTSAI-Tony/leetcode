'''
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"  @@就算刪除重複, 前後順序也不能變
Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
'''

# Explanation
# last_index is a mapping from character to its last appearing index
# cur_result stores current result

# When cur_result is not empty, cur_result[-1] represents the last element of current result,
# if the current character ch is smaller than cur_result[-1] and we have another cur_result[-1] in the subsequent string 
# i.e. i < last_index[cur_result[-1]], we need to pop the last element from the current result.
# Example
# Say our input s is 'bcabc'.
# last_index would be

# last_index = {
#     'b': 3,
#     'c': 4,
#     'a':2
# }
# When i = 2, cur_result is ['bc'], current character ch is 'a'.
# As 'a' is smaller than 'c' and i is smaller than last_index['c'], we pop 'c' from cur_result, then cur_result becomes ['b']. 
# Similarly, we pop 'b' as well. At the end of this iteration, we add current character a into the cur_result resulting in ['a'].

# stack solution
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_index = {} #dict
        for index, ch in enumerate(s):
            last_index[ch] = index #紀錄同樣字母最後出現的index
        cur_result = []
        for i, ch in enumerate(s):
            if ch not in cur_result: #只出現一次
                while cur_result and ch < cur_result[-1] and i < last_index[cur_result[-1]]:
                    cur_result.pop() #pop掉最後一個
                cur_result.append(ch)
        return ''.join(cur_result)

# 'a'<'b'
# True