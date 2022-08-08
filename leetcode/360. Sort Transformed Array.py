'''
Given a sorted integer array nums and three integers a, b and c, apply a quadratic function of the form f(x) = ax2 + bx + c to each element nums[i] in the array, 
and return the array in a sorted order.

 

Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
 

Constraints:

1 <= nums.length <= 200
-100 <= nums[i], a, b, c <= 100
nums is sorted in ascending order.
 

Follow up: Could you solve it in O(n) time?
'''


'''
Intro
Math + Two Pointers

I feel like this is more of a Math question than Two Pointer algorithm.

Math fact:
if a>0: the quadratic function is something like this

y
^
|   +               +
|    +             +
|      +         +
|          + +
---------------------------> x
if a<0: the quadratic function is something like this

y
^
|          + +
|      +         +  
|    +             +
|   +               +
---------------------------> x
About this question
We have a sort list nums from small to large.
I hope you know what vertex is and how it's calculated. Vertex x = -b/(2a). Tho, formula is not important, but the concept is. Vertex is the center x so that y is max or min (depending on sign of a).
When a > 0, we have 3 senarios:

nums[-1] <= vertex, meaning all values in nums will be on the left side of the center line of the quadratic function graph. (Decreasing side)
nums[0] >= vertex, meaning all values in nums will be on the right side of the center line of the quadratic function graph. (Increasing side)
nums[0] <= nums[i] <= vertex <= nums[j] <= nums[-1], meaning some values are on the left and some are on the right.
How do we take advantage of these given information? Above information can be summed up to following. It tells you:

When a>0, the largest number is either on left or right end of nums.

Correspondingly,
When a<0, the smallest number is either on left or right end of nums.

Then, I think the idea is pretty simple, we use Two Pointer method to pick current largest or smallest in nums and add to new array (you can also do in-place change), depends on the sign of a.

Why we don't care about when a = 0, b > 0 or b <0?
Because, above method can handle that. How?
When a = 0, b > 0, the graph is mono-increase, which is the same case as the right side of quadratic graph when a > 0 (or left side when a < 0).
You can figure out the cooresponding cases for a = 0, b < 0.
'''

# 刷題用這個, time complexity O(n), space compplexity O(1)
# 思路: 使用雙指針, math, 拋物線 a 正負值 代表開口向上or向下
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quadratic(x):
            return a*x*x + b*x + c 
        n = len(nums)
        index = 0 if a < 0 else n-1 # a <= 0 開口向下
        l, r, ans = 0, n-1, [0] * n
        while l <= r:
            l_val, r_val = quadratic(nums[l]), quadratic(nums[r])
            if a >= 0:
                if l_val > r_val:
                    ans[index] = l_val 
                    l += 1
                else:    
                    ans[index] = r_val 
                    r -= 1
                index -= 1
            else:
                if l_val > r_val:
                    ans[index] = r_val 
                    r -= 1
                else:    
                    ans[index] = l_val 
                    l += 1
                index += 1
        return ans




# 自己想的, time complexity O(nlogn), space complexity O(n)
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        helper = lambda x: a*x**2 + b * x + c
        array = []
        for num in nums:
            array.append(helper(num))
        array.sort()
        return array