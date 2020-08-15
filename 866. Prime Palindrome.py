'''
Find the smallest prime palindrome greater than or equal to N.

Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1. 

For example, 2,3,5,7,11 and 13 are primes.

Recall that a number is a palindrome if it reads the same from left to right as it does from right to left. 

For example, 12321 is a palindrome.

 

Example 1:

Input: 6
Output: 7
Example 2:

Input: 8
Output: 11
Example 3:

Input: 13
Output: 101
 

Note:

1 <= N <= 10^8
The answer is guaranteed to exist and be less than 2 * 10^8.
'''
#time complexity O(10^(d+1)-10^(d)), d = len(str(n) // 2), 刷題用這個
#思路: 與其check 是否為palindrome 不如自己製造palindrom
#先找出n的幾位數, 再建立該位數的所有palindrom 看是否有palindrom 是 prome 且 > N
#若沒有則總位數增加1位數, 再建立該位數的所有palindrome
#技巧: 利用yield 讓func 變成generator
class Solution:
    def primePalindrome(self, N):
        ndigits = len(str(N)) #先查看有幾個digits
        while True:
            for x in self.palindromes(ndigits):
                if x >= N and self.isPrime(x):
                    return x
            ndigits += 1 #增加位數
            
    def palindromes(self, n):
        if n == 1:
            for i in range(10):
                yield i
        elif n % 2 == 0:
            d = n // 2
            for i in range(10**(d-1), 10**d): #ex: n = 8, d = 4, i in range(1000, 10000) => 四位數
                s = str(i)
                yield int(s + s[::-1])
        else:
            d = n // 2
            for i in range(10**(d-1), 10**d):
                s = str(i)
                for j in range(10): #中間值
                    yield int(s + str(j) + s[::-1])
                    
    def isPrime(self, x):
        if x == 1:
            return False
        for i in range(2, int(x**0.5+1)):
            if x % i == 0:
                return False
        return True

#自己重寫 time complexity O(10^(d+1) - 10^d), d = len(str(n) // 2)
class Solution:
    def primePalindrome(self, N: int) -> int:
        n = len(str(N))
        while True:
            for i in self.palindrome(n):
                if self.prime(i) and i >= N:
                    return i
            n += 1
    
    def palindrome(self, n):
        if n == 1:
            for i in range(1,10):
                yield i
            
        elif n % 2 == 0:
            d = n // 2
            for i in range(10**(d-1), 10**d):
                yield int(str(i) + str(i)[::-1])
        else:
            d = n // 2
            for i in range(10**(d-1), 10**d):
                for j in range(10): #中間值包含0
                    yield int(str(i) + str(j) + str(i)[::-1])
    
    def prime(self, num):
        if num == 1:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True


#自己想的 naive TLE, time complexity O(10n)
class Solution:
    def primePalindrome(self, N: int) -> int:
        n = 2
        while True:
            count = 0
            for i in range(1, int(n**0.5)+1):
                if i != 1 and n % i == 0:
                    count += 1
                    break
            
            if count == 0 and self.check(n) and n >= N:
                return n
            n+=1
        
                   
    def check(self, n):
        str_n = str(n)
        mid = len(str_n) // 2
        if len(str_n) % 2 != 0:
            if str_n[:mid+1] == str_n[mid:][::-1]:
                return True
            return False
        else:
            if str_n[:mid+1] == str_n[mid+1::-1]:
                return True
            return False