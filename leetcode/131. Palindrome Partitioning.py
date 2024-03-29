'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''

# 刷題用這個, backtracking
# time complexity O(N⋅2^N), where N is the length of string s, This is the worst-case time complexity when all the possible substrings are palindrome.
# space complexity O(N)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        self.dfs(s, 0, res, path)
        return res

    def dfs(self, s, index, res, path):
        if index == len(s):
            res.append(path.copy())
            return
        for i in range(index, len(s)):
            if self.isPalindrome(s, index, i):
                path.append(s[index:i+1])
                self.dfs(s, i+1, res, path)
                path.pop()
    
    def isPalindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start+=1
            end-=1
        return True





class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        
        res = []
        
        def helper(s, tmp):
            """
            如果是空字符串，说明已经处理完毕
            否则逐个字符往前测试，判断是否是回文
            如果是，则处理剩余字符串，并将已经得到的列表作为参数
            """
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1): 
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tmp + [s[:i]]) #回朔法=樹狀
        
        helper(s, [])
        return res

        #看到所有可能的结果的时候，一般想到回溯
        '''
        什么是回溯法

回溯法（探索与回溯法）是一种选优搜索法，又称为试探法，
按选优条件向前搜索，以达到目标。但当探索到某一步时，发现原先选择并不优或达不到目标，就退回一步重新选择，这种走不通就退回再走的技术为回溯法，而满足回溯条件的某个状态的点称为“回溯点



回溯法与递归： 
回溯法是一种思想，递归是一种表達形式

divide and conquer 是一种思想，递归是一种表達形式
'''