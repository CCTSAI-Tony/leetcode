'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

#自己重寫 time complexity O(3(4)^n) space complexity O(n)
#思路: dfs backtracking, 建立phone graph 再利用dfs 來找出所有的組合
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return None
        memo = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], 
               "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], 
               "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        res = []
        self.digits = digits
        self.dfs(memo, 0, [], res)
        return res
    
    def dfs(self, memo, idx, path, res):
        if idx == len(self.digits):
            res.append("".join(path))
            return
        for c in memo[self.digits[idx]]:
            path.append(c)
            self.dfs(memo, idx + 1, path, res)
            path.pop()

#重寫第二次, time complexity O(3(4)^4), space complexity O(1)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        memo = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        res = []
        self.dfs(digits, "", memo, res)
        return res if digits else None
        
    def dfs(self, digits, path, memo, res):
        if not digits:
            res.append(path)
            return
        for letter in memo[digits[0]]:
            self.dfs(digits[1:], path + letter, memo, res)


#思路: bfs -> bfs 也可以能來遍歷全部可能組合
class Solution(object):
    def letterCombinations(self, digits):
        interpret_digit = {
            '1': '',  #空字串
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        all_combinations = [''] if digits else [] #好語法學起來。[]空list
        for digit in digits: #每個digit 代表一個layer
            current_combinations = list()
            for letter in interpret_digit[digit]:
                for combination in all_combinations: #['']也算一個item, 並不是空list
                    current_combinations.append(combination + letter)
            all_combinations = current_combinations #換成當層layer
        return all_combinations

        #take points '' 空字串 []空list ['']不是空list

#重謝第二次, time complexity O(3^4), space complexity O(1)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        memo = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        combinations = [""]
        for digit in digits:
            cur_combinations = []
            for combination in combinations:
                for letter in memo[digit]:
                    cur_combinations.append(combination + letter)
            combinations = cur_combinations
        
        return combinations if digits else None


#重寫第四次, time complexity (3^4), space complexity O(1)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return None
        memo = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], 
               "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], 
               "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        res = []
        self.digits = digits
        self.dfs(memo, 0, "", res)
        return res
    
    def dfs(self, memo, idx, path, res):
        if idx == len(self.digits):
            res.append(path)
            return
        for c in memo[self.digits[idx]]:
            self.dfs(memo, idx + 1, path + c, res)
