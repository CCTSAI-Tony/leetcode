'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. 
Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''

# 这个题的初级版本中 ，只有一个数出现一次，xor 一遍即可得到答案。为什么呢？

# A xor A=0
# 0 xor A=A
# 并且 xor 满足交换律和结合律。
# 比如 2 2 3 1 3，2 xor 2 xor 3 xor 1 xor 3
# = 2 xor 2 xor 3 xor 3 xor 1
# =(2 xor 2) xor (3 xor 3) xor 1
# = 0 xor 0 xor 1
# = 1

# 在这道加强版的题目里，也会很自然的想到 xor 一遍，那结果是什么呢。假设只出现一次的两个数是 A、B，那我们最后只能得到一个值 = A xor B，但没有办法知道 A 是多少，B 是多少。
# 那得到的这个值有没有用呢？有，xor 是按位比较，相同为0，不同为1，也就是说得到的这个值里，所有的1都代表了：在这个位置上，A 和 B 是不同的，这给我们区分 A B 提供了一个方法：

# 我们随便找一个是1的位置（也就是 A和B 在这个位置上的值反正有一个是0 有一个是1），再次遍历一遍数组，按照这个位置上是0还是1分成两组，那么 A 和 B 一定会被分开。
# 而对于其他的数字，无论他们在这个位置上是0还是1，总之他们会两两一对分到两个组中的任意一个组里去。

# 这就转化成了初级版本的问题了，每个组中都只有一个数出现1次，对两个组分别做一次xor ，得到两个数就是 A 和 B。

# ALGORITHM:

# Suppose that a and b are the numbers that occur once.
# XOR all numbers. Because all other numbers occur twice, XOR-ing them will
# cancel them out. We are left with XOR of a and b.
# Find the right most set bit(1) in this xor. That means, starting from right,
# this is the first bit that is different in a and b. all other but in the
# right are same.
# Create a mask, with only this bit set and all other bits being 0.
# Maintain 2 variables a and b to get the 2 single numbers.
# Iterate over all numbers in nums again. BITWISE AND the mask and each
# number. If num & mark == 0, XOR num with (a) else XOR num with (b)
# After this iteration a and b will contain the two single occuring nums.
# Return [a, b]
# RUNTIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(1)

#bit manipulation, time complexity O(n), space complexity O(1), 112ms
#思路: 先利用xor 來消除重複兩次的num, 得到的結果從右到左第一個出現1的bit, 則代表兩個出現一次的數表現不一樣的bit, 建立mask 紀錄這個bit
#利用a,b 分流, 遍歷nums => num & mask == 1, ^= a, num & mask == 0, ^= b, 因為出現兩次的num會被抵銷, 最後a,b分流結果就是出現一次的num
class Solution(object):
    def singleNumber(self, nums):
        xor = 0
        for n in nums:
            xor ^= n
        
        mask = 1
        while True: # Create a mask, with only this bit set and all other bits being 0, then find the right most set bit in this xor
            if xor & mask == 0:
                mask = mask << 1 #shift one bit to left
            else:
                break
        
        a, b = 0, 0
        for n in nums:
            if n & mask == 0:
                a ^= n
            else:
                b ^= n
        return [a,b]


#自己重寫
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        mask = 1
        while True:
            if mask & xor == 0:
                mask <<= 1
            else:
                break
        a, b = 0, 0
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        return [a,b]














