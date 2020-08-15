'''
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference 
between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
'''
import collections
class Solution:

def containsNearbyAlmostDuplicate(self, nums, k, t):
    if k < 1 or t < 0:
        return False
    dic = collections.OrderedDict()
    for n in nums:
        if not t: #t = 0
                key = n
            else:
                key = n//t
        for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
            if m is not None and abs(n - m) <= t:
                return True
        if len(dic) == k: #保持index distance <= k
            dic.popitem(False) #ordereddict pop出第一順位,因為ordereddict 的原因 index順序不會變
        dic[key] = n
    return False

# numbers in range [x-t, x+t] are mapped to range [x//t-1, x//t+1]
# and
# to prevent case like [1, 19] k = 1 t = 10, the code use abs(n - m) <= t

# this is a beautiful solution with some math tricks!
# Very helpful, use OrderedDict to remember the index and n//t to shrink the interval to -1, 0, 1.

# 如果： | nums[i] - nums[j] | <= t 式a, 注意是絕對值

# 等价： | nums[i] / t - nums[j] / t | <= 1 式b

# 推出： | floor(nums[i] / t) - floor(nums[j] / t) | <= 1 式c, 應該是說符合式b一定符合式c,但符合式c不一定符合式b, 所以要abs(n - m) <= t double check!

# ​等价： floor(nums[j] / t) ∈ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1} 式d
# @@其中式b是式c的充分非必要条件，因为逆否命题与原命题等价，所以：

# 如果： floor(nums[j] / t) ∉ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1} 非d

# 推出： | nums[i] - nums[j] | > t 非a

# OrderedDict preserves the order in which the keys are inserted. A regular dict doesn’t track the insertion order, 
# and iterating it gives the values in an arbitrary order. By contrast, the order the items are inserted is remembered by OrderedDict.

# from collections import OrderedDict 
  
# print("This is a Dict:\n") 
# d = {} 
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
  
# for key, value in d.items(): 
#     print(key, value) 
  
# print("\nThis is an Ordered Dict:\n") 
# od = OrderedDict() 
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# od['d'] = 4
  
# for key, value in od.items(): 
#     print(key, value) 

# This is a Dict:
# ('a', 1)
# ('c', 3)
# ('b', 2)
# ('d', 4)

# This is an Ordered Dict:
# ('a', 1)
# ('b', 2)
# ('c', 3)
# ('d', 4)




# 2.collections.OrderedDict
# 这个类型在添加键的时候会保持顺序，因此键的迭代次序总是一致的。OrderedDict 的 popitem 方法默认删除并返回的是字典里的最后一个元素，但是如果像 my_odict.popitem(last=False) 这样调用它，那么它删除并返回第一个被添加进去的元素。

# import collections
# e = collections.OrderedDict()
# e[1]=10
# e[2]=20
# e[3]=30
# e
# OrderedDict([(1, 10), (2, 20), (3, 30)])
# e.popitem(False) #ordereddict pop出第一順位
# (1, 10) 

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        size = len(nums)


        if t == 0 and len(nums) == len( set(nums) ):
        
            # Quick response for special case on t = 0
            # t = 0 requires at last one pair of duplicate elements
            return False
        
        
        
        for i, cur_val in enumerate(nums):
            
            for j in range( i+1, i+k+1): #比i大 1 至 k
                
                if j >= size: 
                    # avoid index out of boundary
                    break
                
                if abs(cur_val - nums[j]  ) <= t:
                    # hit: 
                    # i != j, | i-j | <= k
                    # | nums[i] - nums[j] | <= t
                    return True
                
            
        return False

#刷題用這個 bucket solution
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0: 
            return False
        d = {}
        for i, (n, b)  in enumerate(zip(nums, map(lambda x: x // (t + 1), nums))): #map 針對每個元素
            if b in d or min(n - d.get(b - 1, float('-inf')), d.get(b + 1, float('inf')) - n) <= t:  #敘述三種狀況
                return True
            d[b] = n
            if i >= k: 
                del d[nums[i - k] // (t + 1)] #刪除離目前index有k個元素的元素key,該元素key= nums[i - k] // (t + 1)
        return False

# The main idea is splitting elements in nums into different buckets in terms of the value of t (for each element, divide by (t+1) for integer division).
# If the result is True, which means one of the following 3 cases hold:

# Two elements in the same bucket - 可以理解為什麼divide by (t+1),這樣同個bucket 最大-最小 <= t
# One in the previous bucket
# One in the next bucket
# If the case 2 or 3 holds, you need to check if their difference <= t.
# And there can be at most k buckets at any time. If i (counter in code) >= k, delete the (i-k)-th one.

# That's my understanding of the code. Hope it can help you.




# map(fun, iter)

# def addition(n): 
#     return n + n 
  
# # We double all numbers using map() 
# numbers = (1, 2, 3, 4) 
# result = map(addition, numbers) 
# print(list(result)) 
# [2, 4, 6, 8]

# Use dict.get(key[, default]) to assign default values
# The code below is functionally equivalent to the original code above, but this solution is more concise.

# When get() is called, Python checks if the specified key exists in the dict. If it does, then get() returns the value of that key. 
# If the key does not exist, then get() returns the value specified in the second argument to get().

# dictionary = {"message": "Hello, World!"}

# data = dictionary.get("message", "")

# print(data)  # Hello, World!

# d = {1:10,2:20,3:30,4:40,5:50}
# d.get(10,100)
# 100














