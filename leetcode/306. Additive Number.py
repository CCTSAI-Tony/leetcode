'''
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, 
each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
 

Constraints:

num consists only of digits '0'-'9'.
1 <= num.length <= 35
Follow up:
How would you handle overflow for very large input integers?
'''
# First we find the first two valid numbers and generate a fibonacci like string use these two numbers.
# Then compare the generated string with the given num string.

# the length of first number should be less then len/2 since the third is the sum of the first two; 


class Solution(object):
    def isAdditiveNumber(self, num):
        if len(num) < 3:
            return False
        for i in range(len(num) // 2): #ex: 999 + 1 = 1000 99911000
            for j in range(i+1, len(num) // 3 * 2): #because a+b = c, a+b 字串最多<=總長的2/3
                one = int(num[:i+1]) #cause we translate it to int first, we have already excluded leading zero conditions 這個重要!! 
                two = int(num[i+1:j+1])
                if self.generate_fib_str(one, two, len(num)) == num:
                    return True
                if num[i+1] == '0': #no leading zeros, 提早結束迴圈, 這個不寫答案也對
                    break #code out side the second for loop
            if num[0] == '0': #if single 0 can't find the right string then there is no right string, break! 這個不寫答案也對
                break #code out side the first for loop
        return False
    
    def generate_fib_str(self, a, b, n): #序列生成器
        # type: int, int, int -> str
        fib_str = str(a) + str(b)
        while len(fib_str) < n:
            fib_str += str(a + b)
            a, b = b, a+b
        return fib_str[:n] #index 0 to (n-1)


# a = Solution()
# a.isAdditiveNumber('99911000')
# True






        




