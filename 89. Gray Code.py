class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        res = self.grayCode(n-1) #先取得前次結果
        num = 2**(n-1) # flip the first binary digit to 1
        res += res[::-1]
        for i in range(num,len(res)): #對於新增的數做處理
            res[i] ^= num
        return res



'''
Recursion. grayCode(n) can be obtained by first constructing grayCode(n-1) and append grayCode(n-1)[::-1] 
with a bit 1 added in front of every binary number in grayCode(n-1)[::-1]. The base case: grayCode(0) = [0].

Consider the example n = 3. With n = 2, we have grayCode(2) = [00, 01, 11, 10] = [0, 1, 3, 2]. 
For n = 3, 
the 4 binary numbers in grayCode(2) still show up, i.e., it will contain [000, 001, 011, 010] = [0, 1, 3, 2]. 
To obtain the other 4 binary numbers, we simply flip the first binary digit to 1, i.e., [100, 101, 111, 110] = [4, 5, 7, 6].
Finally, we append [6, 7, 5, 4] to [0, 1, 3, 2] to obtain the output for grayCode(3) = [0, 1, 3, 2, 6, 7, 5, 4]. 
Note that we have to reverse the second list because 6 (110) can be obtained from 2 (010) by flipping one bit, whereas 4 (100) cannot.

Time complexity: O(2^n), space complexity: O(2^n).


In the table below: Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)

^	Bitwise XOR	x ^ y = 14 (0000 1110)


'''






'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 2**0 = 1.
             Therefore, for n = 0 the gray code sequence is [0].


'''