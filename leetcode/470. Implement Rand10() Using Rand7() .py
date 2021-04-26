'''
Given the API rand7() that generates a uniform random integer in the range [1, 7], write a function rand10() that generates a uniform random integer in the range [1, 10]. 
You can only call the API rand7(), and you shouldn't call any other API. Please do not use a language's built-in random API.

Each test case will have one internal argument n, the number of times that your implemented function rand10() will be called while testing. 
Note that this is not an argument passed to rand10().

Follow up:

What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?
 

Example 1:

Input: n = 1
Output: [2]
Example 2:

Input: n = 2
Output: [2,8]
Example 3:

Input: n = 3
Output: [3,8,10]
 

Constraints:

1 <= n <= 105
'''

# Algorithm

# This solution is based upon Rejection Sampling. The main idea is when you generate a number in the desired range, output that number immediately. 
# If the number is out of the desired range, reject it and re-sample again. As each number in the desired range has the same probability of being chosen, 
# a uniform distribution is produced.

# Obviously, we have to run rand7() function at least twice, as there are not enough numbers in the range of 1 to 10. By running rand7() twice, 
# we can get integers from 1 to 49 uniformly. Why?


# A table is used to illustrate the concept of rejection sampling. 
# Calling rand7() twice will get us row and column index that corresponds to a unique position in the table above. 
# Imagine that you are choosing a number randomly from the table above. If you hit a number, you return that number immediately. 
# If you hit a * , you repeat the process again until you hit a number.

# Since 49 is not a multiple of 10, we have to use rejection sampling. Our desired range is integers from 1 to 40, which we can return the answer immediately. 
# If not (the integer falls between 41 to 49), we reject it and repeat the whole process again.


# Time Complexity: O(1) average, but O(∞) worst case.
# 思路: 利用double call rand7(), 產生1-49, 但只有1-40 區間的數都是平均分佈的, 可以直接轉化成1-10 range, 若數落在41-49 => reject sample, 再產生一組隨機值
# 技巧: 1 + (idx - 1) % 10 是為了應付1 based index issue
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row = rand7()
            col = rand7()
            idx = col + (row - 1) * 7
            if idx <= 40:
                return 1 + (idx - 1) % 10

#重寫第二次, time complexity: O(1) average, but O(∞) worst case.
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row = rand7()
            col = rand7()
            idx = col + (row - 1) * 7
            if idx <= 40:
                return 1 + (idx - 1) % 10




