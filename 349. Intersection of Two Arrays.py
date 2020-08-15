'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''

# Solution 1:

# use set operation in python, one-line solution.

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

# Solution 2:

# brute-force searching, search each element of the first list in the second list. 
# (to be more efficient, you can sort the second list and use binary search to accelerate)
# time complexity o(mn), m = len(nums1), n = len(nums2)
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            if i not in res and i in nums2:
                res.append(i)
        
        return res


# Solution 3: time complexity O(m*n) 刷題用這個
# 思路: use dict/hashmap to record all nums appeared in the first list, 
# and then check if there are nums in the second list have appeared in the map.

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i]+1 if i in map else 1  #也可以 map[i] = map.get(i,0) +1
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] = 0  #歸0避免重複
        
        return res

# Solution 4: 這個方法比較直觀, 刷題用這個
# 思路: sort the two list, and use two pointer to search in the lists to find common elements.
# O(nlogn) cause sort()
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:       #以下也可以 if not len(res) or nums1[i] != res[-1]: 
                if not (len(res) and nums1[i] == res[-1]):  #True and False -> False, False and False -> False
                    res.append(nums1[i])
                i += 1
                j += 1
    
        return res


#if not (len(res) and nums1[i] == res[len(res)-1]), len(res)先提false 這句就是false, 所以後面就自動跳過檢查 也就不會產生list index out of range



# 自己想的 time complexity O(max(m,n))
# check key if it is in dict O(1)
# 思路: 利用dict 來紀錄兩個序列共同的元素
import collections
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = collections.defaultdict(int)
        for num in nums1:
            if num not in nums1_dict:
                nums1_dict[num] += 1
        for num in nums2:
            if num in nums1_dict:
                nums1_dict[num] -= 1
        return [i for i in nums1_dict if nums1_dict[i] < 1 ]

# What is the time complexity of checking if a key is in a dictionary in Python?
# The (amortized) time complexity is constant (O(1)) in the size of the dictionary.
# Python dictionaries are implemented as hash tables in python

# To check if a key is in a hash table you have to compute the hash of the key and lookup the corresponding entry in an array. 
# Both of this Operations are independent of the size of the dictionary. O(1)
# However, the case can occur, that more than two entries of the hash-table have the same hash (collision), 
# in which case additional perturbations are applied to the hash code. 
# As these case is rather rare, it does not affect the amortized time complexity







   


