'''
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. 
You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.

Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4, z = sx+ly => 4 = -2*3 +2*5 or -7*3 + 5*5 or -12*3 + 8*5 or -17*3 + 11*5 or 3*3 -1*5 or 8*3 -4*5 or 13*3 -7*5
Output: True

Example 2:

Input: x = 2, y = 6, z = 5
Output: False
'''

# Explanation: 
        # Key idea is that z litres is measurable using jugs of size x and y only if , z is a linear combination of x and y.
        # Reasoning for key idea : 
        # basically only options we have to solve the issue is - either pour water of amount x or y 
        # (which is positive multiplication constant on x or y) or a choice of emptying x or y (which is negative multiplication constant on x or y).
        # hence for z to be measurable by x and y, z has to be 
        # z = sx+ly (where s and l are integer constants, we dont need to know s and l to solve our problem :))
        # So, in positive case where, z = kx + ly where k and l are constants, z is measurable. 
        # Now, if g is gcd of x and y, then z = kag + lbg where a and b are constants 
        # So, z = (ka+lb)g  = cg (c is constant) -> @@ which suggests z must be divisible by g in order for z to be measurable by x and y. 
        # 以上證明只要z 能被g整除, 代表z 一定可以成為 kx + ly 組合的其中一個數, 反之則不行
        # AND 
        # x + y must be equal or greater than z, otherwise we can fill up x and y both, but still they will sum up less than z. Hence, z won't be measurable if x + y < z
        # using that logic, we can say answer is:
        # return true if z % gcd(x, y) == 0 and x + y >= z

#greatest common divisor (GCD) 最大公因數 輾轉相除法
#ex gcd(35,10)->gcd(10,5)->gcd(5,0), gcd(3,5)->gcd(5,3)->gcd(3,2)->gcd(2,1)->gcd(1,0)
#Using Euclid's algorithm - https://en.wikipedia.org/wiki/Greatest_common_divisor & https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        
        def gcd(x, y):  
            
            if x < y: 
                x, y = y, x
            while  y != 0 : #while x != y ex: gcd(6,6)
                remainder = x % y 
                x = y
                y = remainder
            return x
        
        g = gcd(x,y)

        if g == 0:
            return z == 0
        
        return (x+y) >= z and z % g == 0  #ex: x=5 ,y =0, z=5, gcd(5,0) = 5 



# Euclidean algorithms (Basic and Extended)
# def gcd(a, b):  
#     if a == 0 : 
#         return b  
      
#     return gcd(b%a, a) 
  
# a = 10
# b = 15
# print("gcd(", a , "," , b, ") = ", gcd(a, b)) 
  
# a = 35
# b = 10
# print("gcd(", a , "," , b, ") = ", gcd(a, b)) 
  
# a = 31
# b = 2
# print("gcd(", a , "," , b, ") = ", gcd(a, b)) 
  
# # Code Contributed By Mohit Gupta_OMG <(0_o)> 

# Output :
# GCD(10, 15) = 5
# GCD(35, 10) = 5
# GCD(31, 2) = 1

# 0和1的最大公因数和最小公倍数是多少
# 研究公因数和公倍数时不考虑0,这是规定


# 有趣的例子看一下
# class Solution:
#     def canMeasureWater(self, x: int, y: int, z: int) -> bool:
#         def gcd(x,y):
#             if x < y:
#                 x,y = y,x
#             while x!=y and y != 0:
#                 remainder = x % y
#                 x = y
#                 y = remainder
#             return x
#         g = gcd(x,y)
#         if g == 0:
#             return z == 0
#         return (x+y)>=z and z % g ==0

# a = Solution()
# a.canMeasureWater(5,0,5)
# True

# 5%0
# ZeroDivisionError: integer division or modulo by zero













