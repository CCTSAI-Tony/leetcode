'''
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
'''

#刷題用這個, 這招學起來!
# You can use a generic memoization decorator also:
class Memoize:
    def __init__(self, f):
        self.f,self.memo = f,{}
    def __call__(self, *args):
        if args not in self.memo: 
        	self.memo[args] = self.f(*args)  # *args 代表可以pass in 多重參數 ex: f(2,(1,1)), 此題只有一個參數 *args 可以不加 *
        return self.memo[args]

@Memoize
def integerReplacement(n):
        if n == 1:
            return 0
        if n % 2:
            return 1 + min(integerReplacement(n+1), integerReplacement(n-1))
        else:
            return 1 + integerReplacement(n/2)    
    
class Solution(object):
    def integerReplacement(self, n):
        return integerReplacement(n)

# As we are using a dictionary, we can't use mutable arguments, i.e. the arguments have to be immutable.

# dict = {}
# dict[1,(2,3)] = 3
# dict
# {(1, (2, 3))


# dict = {}
# dict[1,[2,3]] = 3
# TypeError: unhashable type: 'list'




# Python top-down approach. Memoization saves hundreds of ms (345ms -> 36ms).

# First recursive solution without memo: 345ms 

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n % 2: #can't be devided by two
            return 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))
        else:
            return 1 + self.integerReplacement(n/2)

# Write a helper function with memo: 36ms
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {1:0}
        return self.recRep(n, memo)
        
    def recRep(self, n, memo):
        if n in memo:
            return memo[n]
        if n % 2:
            memo[n] = 1 + min(self.recRep(n+1, memo), self.recRep(n-1, memo))
            return memo[n]
        else:
            memo[n] = 1 + self.recRep(n/2, memo)
            return memo[n]





# Denote f(n) the minimum number of jumps from n to 1.
# By definition, we have the recurrence
# f(1) = 0, f(2n) = 1 + f(n), f(2n + 1) = min(f(2n) + 1, f(2n + 2) + 1).
# First notice that this sequence is well defined because f(2n + 2) = f(n + 1) + 1, so f(2n + 1) = min(f(2n) + 1, f(n + 1) + 2). 
# Every element is defined by some element before it.
# We want to show (*):
# If n % 4 = 3 and n != 3, then f(n) = f(n + 1) + 1.
# If n % 4 = 1 or n = 3, then f(n) = f(n - 1) + 1.
# This gives us an O(log n) time, O(1) space solution.

class Solution(object):
    def integerReplacement(self, n):
        rtn = 0
        while n > 1:
            rtn += 1
            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return rtn


# In this code, n will drop to at most n / 2 in at most 2 iterations, so the number of iterations is at most 2 * log(n). 
# In each iteration, the time complexity is constant. So the overall time complexity is O(log n). The space complexity is obviously 1. 
# Correctness is guaranteed by (*).

# Lemma 1. f(k+1) <= f(k) + 1
# Prove by induction:
# f(2) = 1 <= 0 + 1 = f(1) + 1
# Assume this hold for any 1 <= k' < k,
# If k is even, f(k + 1) = min(f(k) + 1, f(k + 2) + 1) <= f(k) + 1;
# If k is odd, denote k = 2l + 1 (l >= 1), then f(k + 1) = f(2l + 2) = 1 + f(l + 1) <= 1 + 1 + f(l) = 1 + f(2l) = 1 + f(k - 1). 
# Also, f(k + 1) = 1 + f(l + 1) = f(2l + 2) = f(k + 1) <= f(k + 1) + 1. Hence, f(k + 1) <= min(f(k - 1) + 1, f(k + 1) + 1) = f(k) <= f(k) + 1.

# Lemma 2. f(k) <= 1 + f(k + 1), k >= 1
# Prove by induction:
# f(1) = 0 <= 1 + f(2)
# Assume this hold for any 1 <= k' < k,
# If k is odd, f(k) = min(1 + f(k - 1), 1 + f(k + 1)) <= 1 + f(k + 1)
# If k is even, denote k = 2l (l >= 1), then f(k) = f(2l) = 1 + f(l)
# 1 + f(l) <= 3 + f(l) = 2 + f(2l) = 1 + (1 + f(2l))
# 1 + f(l) <= 1 + 1 + f(l + 1) <= 3 + f(l + 1) = 2 + f(2l + 2) = 1 + (1 + f(2l + 2))
# => f(k) = 1 + f(l) <= 1 + min(1 + f(2l), 1 + f(2l + 2)) = 1 + f(2l + 1) = 1 + f(k + 1).

# Proof of (*):

# If n % 4 = 3 and n != 3, denote n = 4k + 3 where k >= 1.
# f(n - 1) = f(4k + 2) = 1 + f(2k + 1) = 1 + min(f(2k) + 1, f(2k + 2) + 1) = min(f(2k) + 2, f(2k + 2) + 2)
# f(2k) + 2 = f(k) + 3 >= f(k + 1) + 2 = 1 + f(2k + 2)
# and f(2k + 2) + 2 > f(2k + 2) + 1, so f(n - 1) >= 1 + f(2k + 2) = f(4k + 4) = f(n + 1) => f(n) = min(f(n - 1) + 1, f(n + 1) + 1) = f(n + 1) + 1.

# If n = 3, it's obvious that f(3) = min(f(2) + 1, f(2) + 2) = f(2) + 1.

# If n % 4 = 1 and n > 1, denote n = 4k + 1 where k >= 1.
# f(n - 1) = f(4k) = 1 + f(2k)
# 1 + f(2k) < 2 + f(2k)
# 1 + f(2k) = 2 + f(k) <= 3 + f(k + 1) = 2 + f(2k + 2)
# => f(n - 1) = 1 + f(2k) <= min(2 + f(2k), 2 + f(2k + 2)) = 1 + min(f(2k) + 1, f(2k + 2) + 1) = 1 + f(2k + 1) = f(4k + 2) = f(n + 1)
# => f(n) = min(f(n - 1) + 1, f(n + 1) + 1) = f(n - 1) + 1.

# Great Proof! But I don't think I can come up with this during an interview....


# I think as long as we get to f(2n + 1) = min(f(n) + 2, f(n + 1) + 2), 
# that should be good enough because that will lead us to a O(logn) time and O(logn) space solution.



























































