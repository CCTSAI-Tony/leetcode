'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''

#自己想的
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 0, num
        while low <= high:
            mid = (low + high)//2
            if mid**2 < num:
                low = mid+1
            elif mid**2 == num:
                return True
            else:
                high = mid-1
        return False   


# Solving with Bitwise trick. 不難想, 這個算法在於利用 |= , ^= 之間的差異, ex: num = 25 自己想一下
class Solution:
    def BitwiseTrick(self, num):
       root = 0
       bit = 1 << 15
       
       while bit > 0 :
           root |= bit
           if root > num // root:    
               root ^= bit                
           bit >>= 1        
       return root * root == num

#|  OR  Sets each bit to 1 if one of two bits is 1

#^  XOR Sets each bit to 1 if only one of two bits is 1