'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
'''

#prefer this one, Python Dynamic Programming
class Solution(object):
    def nthUglyNumber(self, n):
    	res = [1]
        i = j = k = 0
        count = 1
        while count <= n:
            if count == n:
                return res[-1]
            val = min(res[i]*2,res[j]*3,res[k]*5)
            if val == res[i]*2:
                i += 1
            if val == res[j]*3:
                j += 1
            if val == res[k]*5:
                k += 1
            res.append(val)
            count +=1

            

class Solution(object):
    def nthUglyNumber(self, n):
        """
        DP approach.
        The idea is to add the numbers to the uglyNumbers list one-by-one by multiplying 2 
        or 3 or 5. While adding the values, we must make sure that a value lesser than
        previously added won't be divisible by the other 2 primes. Hence, increment the
        pointers such that next minimum value can be added to the list.
        """
        uglyNumbers = [1]
        p2 = p3 = p5 = 0
        
        while len(uglyNumbers) < n:
            #If a value lesser than latest was already added, try finding next least value.
            while uglyNumbers[p2]*2 <= uglyNumbers[-1]:
                p2 += 1
            
            while uglyNumbers[p3]*3 <= uglyNumbers[-1]:
                p3 += 1
            
            while uglyNumbers[p5]*5 <= uglyNumbers[-1]:
                p5 += 1
            
            nextVal = min(uglyNumbers[p2]*2, uglyNumbers[p3]*3, uglyNumbers[p5]*5)
            uglyNumbers.append(nextVal)
        
        return uglyNumbers[-1]




