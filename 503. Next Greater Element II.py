'''
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. 
The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, 
which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
'''

# Algorithm

# Stack for next greater element: Suppose we have a decreasing sequence followed by a greater number. 
# For example [5, 4, 3, 2, 1, 6] then the greater number 6 is the next greater element for all previous numbers in the sequence.
# Handling duplicates in input: Push the index and value tuple on the stack instead of just the value. 
# This makes sure duplicated elements are correctly handled. Example:[100,1,11,1,120,111,123,1,-1,-100] - we need to have the right answer for both 1s.
# Handling circular array: Process it twice. Example: [5,4,3,2,1]. 
# By processing it twice, you are essentially doing: [5,4,3,2,1]+[5,4,3,2,1]. 
# Typical pattern to solve circular array problems is to extend the original array to twice length, 2nd half has the same element as first half. 
# Then everything become simple.
# https://discuss.leetcode.com/topic/77881/typical-way-to-solve-circular-array-problems-java-solution

#time complexity: O(n) =>  for loop O(n) , inside while loop O(n-1) => O (n + n-1) => O(n)
#思路: 典型circular array 問題, 主要解法就是加上同樣的arry在原array 後面, 來模擬circular的狀態
#利用dict 來紀錄每個element 下一個比自身大的值是多少, 此方法要同時紀錄index與value 來避免 duplicated element 的狀況, 不然dict key會重複
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cache, st = {}, []
        for idx,x in enumerate(nums): #first half
            while st and st[-1][1] < x:
                a,b = st.pop()
                cache[a] = x
            st.append((idx,x))
        for idx,x in enumerate(nums):  #second half
            while st and st[-1][1] < x:
                a,b = st.pop()
                cache[a] = x
            st.append((idx,x))
        result = [-1]*len(nums)
        for idx,x in enumerate(nums):
            if idx in cache:
                result[idx] = cache[idx]
        return result    

#自己重寫, time complexity O(2n + n - 1) => O(n), 256ms
#思路: 利用 => i % len(nums) 來模擬circular array, 因為要使最後一個element 找到 next greater, 所以要遍歷2*n - 1, circular 到自己之前一個
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        cache = {}
        n = len(nums)
        res = [-1] * n
        for i in range(2*n - 1):
            while stack and stack[-1][1] < nums[i % n]:
                cache[stack[-1][0]] = nums[i % n]
                stack.pop()
            if (i % n) in cache: #若已經找到next greater, 就不需要再放入stack
                continue
            stack.append((i % n, nums[i % n]))
        
        for i in range(n):
            if i in cache:
                res[i] = cache[i]
        return res





#自己想的, 暴力解 time complexity O(n^2), 7328ms
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(len(nums)):
            k = i+1
            while True:
                if nums[(k) % n] > nums[i]:
                    res.append(nums[(k) % n])
                    break
                elif (k) % n == i:
                    res.append(-1)
                    break
                k += 1
        return res







