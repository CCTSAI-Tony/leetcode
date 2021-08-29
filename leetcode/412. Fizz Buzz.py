'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

Constraints:

1 <= n <= 104
'''

# 自己想的, time complexity O(n), space complexity O(n)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [str(i) for i in range(1, n+1)]
        i = 3
        while i <= n:
            res[i-1] = "Fizz"
            i += 3
        i = 5
        while i <= n:
            if res[i-1] == "Fizz":
                res[i-1] = "FizzBuzz"
            else:
                res[i-1] = "Buzz"
            i += 5
        return res