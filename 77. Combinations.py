class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [] # result list
        out = [] # each list
        self.dfs(n, k, 1, out, res)
        return res
    def dfs(self, n, k, level, out, res):
        # out list length is k, save to res, or do next level
        if len(out) == k: #設定條件 斷掉迴圈
            res.append(out[:]) #這邊不能使用 res.append(out) 因為 會reference def combine的 out = [], 若res途中改變, 答案也會改變, 所以要用out[:], copy當下狀態
            return 
        for i in range(level, n + 1): #這個for loop 是一連串的動作, 到最後for loop will not be executed 
            out.append(i)
            self.dfs(n, k, i + 1, out, res) #這邊i+1 確保不會重複
            out.pop() #確保當層root的更換


'''
Depth First Search(dfs)

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

class Solution:
    def combine(self, n, k):
        res = [] # result list
        out = [] # each list
        self.dfs(n, k, 1, out, res)
        return res
    def dfs(self, n, k, level, out, res):
        # out list length is k, save to res, or do next level
        if len(out) == k: #設定條件 斷掉迴圈
            res.append(out[:])
            return 
        for i in range(level, n + 1): #這個for loop 是一連串的動作, 
            out.append(i)
            print('append',out)
            self.dfs(n, k, i + 1, out, res)
            print('result',res)
            print('out before pop',out)
            out.pop()
            print('out after pop',out)

append [1] >到第二層dfs
append [1, 2] >到第三層dfs ＠＠
append [1, 2, 3]  >到第四層dfs 滿三 return 回第三層 @@@
result [[1, 2, 3]] 
out before pop [1, 2, 3]
out after pop [1, 2]
append [1, 2, 4] >到第四層dfs 滿三 return 回第三層
result [[1, 2, 3], [1, 2, 4]] 
out before pop [1, 2, 4]
out after pop [1, 2] >range跑完 return 回第二層(i 已輪完2) ＠＠
result [[1, 2, 3], [1, 2, 4]]
out before pop [1, 2] !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!第三層輪完 換輪第二層
out after pop [1]
append [1, 3] >到第三層dfs
append [1, 3, 4] >到第四層dfs 滿三 return 回第三層 
result [[1, 2, 3], [1, 2, 4], [1, 3, 4]]
out before pop [1, 3, 4]
out after pop [1, 3] > range跑完 return 回第二層(i 已輪完3) ＠＠
result [[1, 2, 3], [1, 2, 4], [1, 3, 4]]
out before pop [1, 3]
out after pop [1]
append [1, 4] > 已到達最高level 無法繼續往下
result [[1, 2, 3], [1, 2, 4], [1, 3, 4]]
out before pop [1] !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!第二層輪完 換輪第一層
out after pop [1] > 
result [[1, 2, 3], [1, 2, 4], [1, 3, 4]]
out before pop [1]
out after pop []
append [2]
append [2, 3]
append [2, 3, 4]
result [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
out before pop [2, 3, 4]
out after pop [2, 3]
result [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
out before pop [2, 3]
out after pop [2]
append [2, 4]
result [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
out before pop [2, 4]
out after pop [2]
result [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
out before pop [2]
out after pop []
append [3]
append [3, 4]
result [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
out before pop [3, 4]
out after pop [3]
result [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
out before pop [3]
out after pop []
append [4]
result [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
out before pop [4]
out after pop []
Out[169]:
[[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]








'''