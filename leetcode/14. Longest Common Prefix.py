# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

#time complexity O(min_len)
#思路: 找出最小長度當作 while loop 的離開點, 不然會 index out of range, 每個word逐一檢查同個位置的字
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ''
        if not strs:
            return result
        
        min_len = min([len(item) for item in strs]) #list comprehension
        
        i = 0
        while i < min_len:
            check = strs[0][i] #+1字逐步檢查, 以第一個字做基準
            for item in strs:
                if item[i] != check: #同個位置檢查
                    return result
            result += check
            i +=1 
        return result


# 重寫第二次, time complexity O(min_len), space complexity O(min_len)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        i = 0
        cur = ""
        while True:
            for string in strs:
                if i >= len(string):
                    return "".join(res)
                if cur == "":
                    cur = string[i]
                if string[i] != cur:
                    return "".join(res)
            res.append(cur)
            i += 1
            cur = ""

