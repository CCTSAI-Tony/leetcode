'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.
'''
import math
class Solution:
# @param num, a list of integer
# @return an integer
    def maximumGap(self, nums):
        if len(nums) < 2 or min(nums) == max(nums):
            return 0
        a, b = min(nums), max(nums)
        size = math.ceil((b-a)/(len(nums)-1)) #bucket裡 max - min 的 size
        bucket = [[None, None] for _ in range((b-a)//size + 1)] #向下取整後加1 為啥加1 因為range
        for n in nums:
            b = bucket[(n-a)//size] #丟到不同的桶子 記得向下取整 >這就是為什麼 bucket 要+1
            b[0] = n if b[0] is None else min(b[0], n) #動態更新min
            b[1] = n if b[1] is None else max(b[1], n) #動態更新max
        bucket = [b for b in bucket if b[0] is not None] #排除空桶子 list comprehension
        return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket))) #當前桶的最小值 - 前一桶最大值

'''
Thanks for sharing! My understanding: we want to make sure those two numbers forming the maximum difference fall into separate buckets 
so that we do not need to worry about the numbers in the same bucket. To achieve this we want the size of each bucket to be less than the maximum difference.

Assuming md denotes the maximum difference, then we have md * (len(nums) - 1) >= b - a, ((len(nums) - 1) 個空隙), so md >= (b - a) / (len(nums) - 1), 
since md must be integer, we get md >= math.ceil((b - a) / (len(num) - 1)), thus we make size = math.ceil((b - a) / (len(num) - 1)).

Then by making the number of buckets to be (b - a) // size + 1, it is guaranteed that the final bucket size is less than maximum difference 
hence those two numbers forming maximum difference will be in separate buckets.

Finally, we find the maximum difference between two adjacent buckets (min value of current bucket and max value of previous bucket) and that will be the answer.

'''
def maximumGap(self, num):
        if len(num) < 2 or min(num) == max(num):
            return 0
        a, b = min(num), max(num)
        size = (b-a)//(len(num)-1) or 1
        bucket = [[None, None] for _ in range((b-a)//size+1)]
        for n in num:
            b = bucket[(n-a)//size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)
        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket)))








'''
Python | math.ceil() function

In Python, math module contains a number of mathematical operations, which can be performed with ease using the module. 
math.ceil() function returns the smallest integral value greater than the number. If number is already integer, same number is returned.


x = 33.7
    
# returning the ceil of 33.7 
print ("The ceil of 33.7 is : ", end ="")  
print (math.ceil(x))

The ceil of 33.7 is : 34
'''

