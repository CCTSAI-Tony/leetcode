'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
'''


# A bit verbose but hopefully easier to understand. We start from the middle and expand out.

# Time complexity O(n). We iterate n//2 times in for _ in range(n//2). Within this, 
# we iterate for num in output at most 5 times, since output has at most 5 numbers.

# Space complexity O(1). temp uses constant space of at most 5.

#刷題用這個, time complexity O(n), space complexity O(1)
#思路: 先觀察怎樣的情況, 就算旋轉180度 數字還是一樣呢, ex: 69 => 69, 689 => 689, 609 => 609, 619 => 619
#以字串中心來想, 若n % 2 != 0, 字串中心有 ['0', '1', '8'] 三種選擇, 因為upside down 不會變, 若n%2 == 0, 則沒有中心數字
#但中心兩邊新增數字則有{"0":"0","1":"1","6":"9","8":"8","9":"6"}, 因為轉180度 順序剛好顛倒, 但upside down後變為還未轉180度的狀態
#因為要避免leading zero => 當 len(num) >= n-2 時, 中心兩邊新增數字不能新增"0"
#iterate 次數 => n // 2
class Solution:
    def findStrobogrammatic(self, n):
        output = [''] if n%2 == 0 else ['0', '1', '8'] #中間值
        for _ in range(n//2):
            temp = []
            for num in output:
                temp.append('1' + num + '1')
                temp.append('8' + num + '8')
                temp.append('6' + num + '9')
                temp.append('9' + num + '6')
                if len(num) < n-2:
                    temp.append('0' + num + '0')
            output = temp

        return output


#自己重寫, time complexity O(n), space complexity O(1)
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        output = [""] if n % 2 == 0 else ["0", "1", "8"]
        for i in range(n // 2):
            temp = []
            for num in output:
                temp.append("1" + num + "1")
                temp.append("6" + num + "9")
                temp.append("8" + num + "8")
                temp.append("9" + num + "6")
                if len(num) < n-2:
                    temp.append("0" + num + "0")
            output = temp
        return output






#自己想的, TLE, time complexity O(5^n)
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        dic = {"0":"0","1":"1","6":"9","8":"8","9":"6"}
        res = []
        self.dfs(n, [], dic, res)
        return res
        
    def dfs(self, n, path, dic, res):
        if n == 0:
            if len(path) > 1 and (path[0] == "0" or path[-1] == "0"):
                return
            else:
                new_path = path[:]
                for i in range(len(path)):
                    new_path[i] = dic[path[i]]
                if new_path[::-1] == path:
                    path = "".join(path)
                    res.append(path)
                return
        for d in dic:
            self.dfs(n-1, path + [d], dic, res)