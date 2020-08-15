'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''


#Sieve of Eratosthenes
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0
            
        primes = [True] * n #把0也算進去了
        primes[0] = primes[1] = False
        for num in range(2, int(math.sqrt(n)) + 1): #到根號n
            if primes[num]:
                primes[num**2:n:num] = [False] * len(primes[num**2:n:num])
        
        return sum(primes)

'''
Hey man, I was trying to figure this out on my own but I couldn't come up with this "num**2:n:num" part, could you please explain me what it does?
Thanks!

Sure! It's python indexing. For example [starting index: ending index: step size], so [0:10:2] would be the 0, 2, 4, 6, and 8th positions of whatever iterable - 
in this problem an array .

Here's a more complete explanation of the problem:
This wiki animation is what it's doing visually https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes. 
The idea is that for every prime, its multiple up to the given range n is NOT prime.

Here's an example given a range or number 30:
0 & 1 are not prime
2 is prime, therefore 4 (2^2), 6 (4+2), 8 (6+2),..., 30 (28+2) are NOT prime
then you repeat this process for 3 and so on up to the sqrt(n)+1 since everything over that you've already checked

'''


a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
a[0:25:2] = [1] * len(a[0:25:2])

a
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

b = [True,True,False]
sum(b)

2

class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2, n):
            if res[i] == True:
                for j in range(2, (n-1)//i+1): #for i in range(2, n): biggest i = n-1, Count the number of prime numbers less than a non-negative number, n.
                    res[i*j] = False
        return sum(res)
'''
what does "(n-1)//i+1" mean?

@@ I guess n-1 is the biggest i. (n-1)//i is the j we want,which makes i*j not prime. The +1 makes the right edge of the range.

'''



