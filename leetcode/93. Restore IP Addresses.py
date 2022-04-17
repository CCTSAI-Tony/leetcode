# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.

# Example:

# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]

#刷題用這個
#自己重想, dfs backtracking time complexity O(27), 最多12個數字11間隔, 分割位置有三個, 但一個位置確定後, 下一個位置只能選後三個位置, 所以是3*3*3, space complexity O(19)
#思路: 選擇前三個空格的其中一格設分號, 符號以前的s[:i] 就是其中一個integers, 注意這個integers 不能有leading zero and 不能 > 255
#超過 4個 integers return, 還沒集滿4個integers但s用完了 return
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return None
        res = set()  #切記 backtracking 尋找所有可能, res 儘量用set, 避免重複
        self.dfs(s, [], res)
        return res
        
    def dfs(self, s, path, res):
        if not s and len(path) == 4:
            res.add(".".join(path))
            return
        if not s or len(path) > 4:
            return
            
        for i in range(1,4):
            if i > 1 and s[:i][0] == "0" or int(s[:i]) > 255:  #自己寫的時候 == "0" 寫成 == 0, 造成bug 要小心
                continue
            path.append(s[:i])
            self.dfs(s[i:], path, res)  #注意, 到第四個數字時, 剩餘s小於3有可能造成答案重複, ex: 剩餘 len(s) = 2, 但 s[:3], s[:4] 皆一樣, 造成答案重複
            path.pop()

#重寫第三次, 刷題用這個, 用到backtracking, time complexity O(27), space complexity O(1)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = set()
        self.dfs(s, [], res)
        return res
    
    def dfs(self, s, path, res):
        if not s and len(path) == 4:
            res.add(".".join(path))
        
        elif s and len(path) < 4:
            for i in range(3):
                temp = s[:i+1]
                if len(temp) > 1 and temp[0] == "0":
                    continue
                elif int(temp) > 255:
                    continue
                else:
                    self.dfs(s[i+1:len(s)], path+[temp], res)
        if path: #prevent pop from empty list
            path.pop()

# a = [1,2]
# a[:100]
# [1, 2]
# a[:3]
# [1, 2]

#重寫第二次, time complexity O(27), space complexity O(19)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.dfs(s, [], res)
        return res
        
    def dfs(self, s, path, res):
        n = len(s)
        if not n:
            if len(path) == 4:
                res.append(".".join(path))
            return
        if s and len(path) == 4:
            return
        for i in range(3):
            temp = s[:i + 1]
            if len(temp) > 1 and temp[0] == "0" or int(temp) > 255:
                break
            if i + 1 < n + 1:
                self.dfs(s[i+1:], path + [temp], res)
        return


class Solution:
    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, 0, "", res)
        return res
    
    def dfs(self, s, index, path, res):
        if index == 4: #ip address 四個數字組成 index 0,1,2,3 path 到4時 s = none時 才算有效ip
            if not s:
                res.append(path[:-1]) #path[:-1] 拿掉最後一個元素"." .
            return # backtracking
        for i in range(1, 4):
            # the digits we choose should no more than the length of s
            if i <= len(s):
                #choose one digit
                if i == 1: 
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)
                #choose two digits, the first one should not be "0"
                elif i == 2 and s[0] != "0": 
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)
                #choose three digits, the first one should not be "0", and should less than 256
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)


'''
IPv4 uses 32 binary bits to create a single unique address on the network. 
An IPv4 address is expressed by four numbers separated by dots. 
Each number is the decimal (base-10) representation for an eight-digit binary (base-2) number, 
also called an octet. For example: 216.27.61.137

'''



