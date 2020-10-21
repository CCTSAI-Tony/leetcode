'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

 

Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
Example 4:

Input: num = "1"
Output: true
'''

#自己想的, time complexity O(n)
#思路: 建立dic 紀錄可以反轉的num:invert_num, 再create 原num invert, 並遍歷它, 把可以反轉的數字替換, 若遇到不能反轉的直接return False
#最後再跟原num比較, 若相同return True
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        invert_dic = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        invert_num = list(num[::-1])
        for i in range(len(invert_num)):
            if invert_num[i] not in invert_dic:
                return False
            else:
                invert_num[i] = invert_dic[invert_num[i]]
        invert_num = "".join(invert_num)
        return num == invert_num