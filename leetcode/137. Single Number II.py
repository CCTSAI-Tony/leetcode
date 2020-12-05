'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
'''

# There are several 'magical' solutions for this problem I saw in comments, done in O(n), which I really enjoed to read, 
# however I doubt if you never saw this problem you can suceed in real interview. That is why I suggest maybe not the fastest, 
# but much more easier to come up solution. The idea is similar to problem Single Number, but here we need to count each bit modulo 3. So, we
# Iterate over all possible 32 bits and for each num check if this num has non-zero bit on position i with => num & (1<<i) == (1<<i) formula.
# We evaluate this sum modulo 3. Note, that in the end for each bit we can have either 0 or 1 and never 2.
# Next, update our answer single with evaluated bit.
# Finally, we need to deal with overflow cases in python: maximum value for int32 is 2^31 - 1, 
# so if we get number more than this value we have negative answer in fact.
# Complexity: time complexity is O(32n), which may be not fully honest linear, 
# but is fine for the purpose of this problem. If we want just O(n) complexity, I think problem becomes not medium but hard. Space complexity here is O(1).

#bit manipulation
#time complexity O(32n), space complexity O(1)
#思路: 遍歷32個bit, 因為每個數重複三次, 只有一個數出現一次, 把每個bit遍歷所有num的count % 3, 若不等於0, 就代表出現一次的num 有這個bit
#若出現一次的數是負數, 則會造成overfolow (single > 2^31-1), 此時single - 2^32 => 就會變回負數=> 記起來, 不難想不要想太多
class Solution:
    def singleNumber(self, nums):
        single = 0
        for i in range(32): #遍歷32個bits
            count = 0
            for num in nums:
                if num & (1<<i) == (1<<i): 
                    count += 1
            single |= (count%3) << i #這邊也可以用 += 
            
        return single if single < (1<<31) else single - (1<<32)   # 1 << 32 == 2 ** 32 (第33個bit)


#自己重寫, time complexity O(32n) => O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num & 1 << i:
                    count += 1
            single |= (count % 3) << i
        return single if single < 2**31 else single - 2 ** 32


#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += num >> i & 1
            single += (count % 3) << i
        return single if single < (1 << 31) else single - (1 << 32)












# why are we having overflows when there are negative numbers?
# For this scenario you will encounter overflows.
# [-2,-2,1,1,-3,1,-3,-3,-4,-2]

# here final result will be 4294967292 which is greater than pow(2,32). 
# hence will be subtracting with 1<<32 which will be 4294967292 -4294967296=-4

# 1 | 0 => 1, 0 | 1 => 1





#自己想的 time complexity O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num,0) + 1
        for key in d:
            if d[key] == 1:
                return key

