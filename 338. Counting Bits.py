'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''
# 類似dp bottom up, time complexity O(n), 刷題用這個
# 思路: 若n 是奇數, 則n的binary 1的個數 是 n//2 + 1, 若n 是 偶數 則n的binary 1的個數 是 n//2
# If n is odd, the last digit is a '1', so a right shift (which is the same as n//2) will eliminate one 1.
# If n is even, the last digit is a '0', so a right shift (i.e. n//2) will have the same number of 1's
class Solution:
    def countBits(self, num):
        output = [0]
        for i in range(1,num+1):
            a = output[i//2] + (i % 2)  #奇數+1
            output.append(a)
                
        return output

#自己重寫 time complexity O(n)
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num+1):
            a = res[i//2] + (i % 2)
            res.append(a)
        return res


# Code works by constantly extending a list with itself but with the values incremented by 1.
# 思路: 每增加一次, 就是增加跟自己一樣大的序列, 這添加序列的每個值都是舊序列的值+1, 因為左邊添加一個1bit, 也就是往左shit到特定bit 添一個1bits,
class Solution(object):
    def countBits(self, num):
        res = [0]
        while len(res) <= num:
            res += [i+1 for i in res] #每增加一次, 就是增加跟自己一樣大的序列, 也就是往左shit到特定bit 添一個1bits, 
        return res[:num+1]  #選擇區間


# [0, 1]
# [0, 1, 1, 2]
# [0, 1, 1, 2, 1, 2, 2, 3]
# [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
# Out[2]:
# [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]

# class Solution(object):
#     def countBits(self, num):
#         """
#         :type num: int
#         :rtype: List[int]
#         """
#         res = [0]
#         while len(res) <= num:
#             res += [i+1 for i in res]
#             print(res)
#         return res[:num+1]

# a = Solution()
# a.countBits(10)




# The number of 1's in the binary representation of 0 is clearly 0 (base case). For a number n, the number of 1's 
# in its binary representation will be determined as follows:










