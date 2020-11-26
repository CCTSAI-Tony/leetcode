'''
Given a string containing only three types of characters: '(', ')' and '*', 
write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
'''

# We need to check if the string is properly balanced with left parenthesis (chars "(" and "*") and properly right balanced - (chars ")" and "*") . 
# We check open parenthesis from the left and closed parenthesis from the right. So, use two vars to determine left and right balance. We should follow these rules:

# If we met "(" or "*" - increment left balance; else decrement it
# If we met ")" or "*" - increment right balance; else decrement it
# If we got negative values for left balance or right balance, we have unvaild string - wrong order of parenthesis or unequal number of open/closed parenthesis. ex: "())"
# Repeat steps 1-3 until we reach the end of the string. Return True then, because string is properly balanced.

# The idea is, we firstly treat * as left (, then we need to make sure the left ( is always more than or equal to ).
# We can use a stack to do this.
# Then similarly, we treat * as a right ), we go through s from right to left, to make sure the right ) is always
# more than or equal to (. If both experiments succeed, then return True.

#time complexity O(n) 刷題用這個
#思路: 利用從左從右遍歷方式, 查看是否有")(" 的狀況, 從左遇到"(" or "*" left balance + 1 else -1, 從右遇到")" or "*" right balance + 1 else -1
#若遍歷的途中其中balance < 0 => 代表發生 ")("的狀況 => invalid的狀況 , 正確的是從左邊出發都是先遇到"(", 從右邊出發都是先遇到")", 因此若左右邊配對成功 最小各=0
#有可能其中一邊 > 0, 而另一邊遍歷 < 0 => 代表有一邊檢查到wrong order => invalid, 也有可能兩邊>0 因為"*" 的關係 => valid
#每一邊遍歷 >= 0 => 只能確保該方向open/close 括號沒出現wrong order(從左遍歷open先出現), 但反過來遍歷就不一定 => ex: "(()" 
#因為有"*"的關係需要頭尾遍歷, 若沒有"*" 遍歷一個方向就能知道valid or not
class Solution:
    def checkValidString(self, s: str) -> bool:
        # balance of left parenthesis and right parenthesis
        leftBalance = rightBalance = 0
        n = len(s)
        for i in range(n):
            # if char is ( or * - we increment leftBalance value
            if s[i] in "(*":
                leftBalance += 1
            # else decrement it
            else:
                leftBalance -= 1
            # we check right balance value starting from the end (right side)
            if s[n-i-1] in "*)":
                rightBalance += 1
            else:
                rightBalance -= 1
            # if any balance goes negative we have the case where order of parenthesis is wrong
            # e.g. )(  -> leftBalance will be -1 and rightBalance will be -1 after first iteration
            # or ((( - leftBalance is OK, but rightBalance will be -1 after first iteration
            if leftBalance < 0  or rightBalance < 0:
                return False
        return True


#自己重寫, time complexity O(n)
class Solution:
    def checkValidString(self, s: str) -> bool:
        left_balance = 0
        right_balance = 0
        n = len(s)
        for i in range(n):
            if s[i] in ["(", "*"]:
                left_balance += 1
            else:
                left_balance -= 1
            if s[n-i-1] in [")", "*"]:
                right_balance += 1
            else:
                right_balance -= 1
            if left_balance < 0 or right_balance < 0:
                return False
        return True







