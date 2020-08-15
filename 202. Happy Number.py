'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        prevNums = set() #不一定用set
        currNum = n
        while currNum != 1:
            sInt = str(currNum)  #為什麼str化, 是因為之後轉換 for char in sInt, 不然 'int' object is not iterable        
            if sInt in prevNums:
                return False
            prevNums.add(sInt)            
            total = 0
            for char in sInt:
                total += pow(int(char), 2)
            currNum = total
        return True

'''
Principle: any number that falls into an infinite loop in this algorithm will arrive at a previous number eventually.

Solution: using a HashSet we can determine if we've seen the number already (in O(1) time), 
and therefore detect if a loop is happening so we can deem it as a non-magic number. otherwise, 
it will be a magic number if the sum evaluates to 1 at some point.

'''
'''
for i in '334':
    print(i)
3
3
4
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        prevNums = []
        currNum = n
        while currNum != 1:
            sInt = str(currNum)
            if sInt in prevNums:
                return False
            prevNums.append(sInt)
            total = 0
            for char in sInt:
                total += pow(int(char),2)
            currNum = total
        return True