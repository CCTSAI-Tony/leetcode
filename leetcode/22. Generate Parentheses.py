# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

#自己想的, time complexity O(n), backtracking, 40ms, 刷題用這個
#思路: 設"(" = 1, ")" = -1, pathSum 來紀錄目前括號的數量狀態, 途中若出現<0代表有")" 無法跟"(" 配對的情況->提早return, 最後全部配對完成 pathSum = 0, 才是valid的答案
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        self.dfs(n, '', 0, res)
        return res
    
    
    def dfs(self, n, path, pathSum, res):
        if pathSum < 0 or pathSum > n:  #代表有 ")" 但前面沒有"(" 與它配對 or "(" 過半
            return
        if len(path) == 2*n:
            if pathSum == 0: #剛好全部配對成功
                res.add(path)
            return
        self.dfs(n, path + "(", pathSum + 1, res)
        self.dfs(n, path + ")", pathSum - 1, res)




class Solution:
# @param {integer} n
# @return {string[]}
    def generateParenthesis(self, n):
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left,right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):
        if right < left:
            return
        if not left and not right:
            ans.append(string)
            return
        if left:
            self.dfs(left-1, right, ans, string + "(") #argument string + "("  不能rgument string += "("
        if right:
            self.dfs(left, right-1, ans, string + ")")

        '''

        回朔法! backtracking
        dfs(2, 2, [], "")
        dfs(1, 2, [], "(")
                dfs(0, 2, [], "((")
                        dfs(0, 1, [], "(()")
                                dfs(0, 0, [], "(())") # We got "(())" and we append it to ans
                dfs(1, 1, ["(())"], "()")
                        dfs(0, 1, ["(())"], "()(")
                                dfs(0, 0, ["(())"], "()()") # We got "(())" and we append it to ans
                        dfs(1, 0, ["(())", "()()"], "())") # will just return as right < left
        dfs(2, 1, ["(())", "()()"], ")") # will just return as right < left

        For the output string to be right, stack of ")" most be larger than stack of "(". If not, it creates string like "())"
Since elements in each of stack are the same, we can simply express them with a number. For example, left = 3 is like a stacks ["(", "(", "("]
        '''