'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

#自己重寫 time complexity O(3(4)^n) space complexity O(3(4)^n)
#思路: dfs backtracking, 建立phone graph 再利用dfs 來找出所有的組合
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        graph = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"] }
        self.dfs(digits, graph, "", res)
        return res
    
    def dfs(self, digits, graph, path, res):
        if not digits:
            res.append(path)
            return
        for char in graph[digits[0]]:
            self.dfs(digits[1:], graph, path+char, res)


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
            for letter in interpret_digit[digit]: #dic  & '1':'' boolean = false 遇到字串包含1 答案直接['']
                for combination in all_combinations: #['']也算一個item, 並不是空list
                    current_combinations.append(combination + letter)
            all_combinations = current_combinations #換成當層layer
        return all_combinations

        #take points '' 空字串 []空list ['']不是空list
