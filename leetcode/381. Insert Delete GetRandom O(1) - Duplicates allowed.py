'''
Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. 
The probability of each element being returned is linearly related to the number of same value the collection contains.
Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
'''

# 刷題用這個, each func time complexity O(1), space complexity O(n)
# 思路: 建立vals list 來記錄目前存在的所有元素, 建立 index map 來紀錄相同元素所有的位置, remove 元素時, 會拿最後insert 的元素來補充該被刪元素的位置
# 技巧: set 的 remove 與 discard 很類似, 若即將被刪掉的元素不存在, 用discard 不會raise error.
import random
from collections import defaultdict
class RandomizedCollection(object):

    def __init__(self):
        self.vals, self.idxs = [], defaultdict(set)
        

    def insert(self, val):
        self.vals.append(val)
        self.idxs[val].add(len(self.vals) - 1)  #add the specific index
        return len(self.idxs[val]) == 1  #check if there is only one element no duplicate
        

    def remove(self, val):
        if self.idxs[val]:
            out, ins = self.idxs[val].pop(), self.vals[-1]  #self.idxs[val].pop() remove set() 隨機一個
            self.vals[out] = ins  #拿最後一個元素替換
            self.idxs[ins].add(out)  #add first plz see more info
            self.idxs[ins].discard(len(self.vals) - 1) # Cause we take the last one to fill the vacancy.
            self.vals.pop()
            return True
        return False 

    def getRandom(self):
        return random.choice(self.vals)


#重寫第二次, each func time complexity O(1), space complexity O(n)
from collections import defaultdict
import random
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals, self.index = [], defaultdict(set)
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.vals.append(val)
        self.index[val].add(len(self.vals) - 1)
        return len(self.index[val]) == 1
            
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.index[val]:
            return False
        out, ins = self.index[val].pop(), self.vals[-1]
        self.vals[out] = ins
        self.index[ins].add(out)
        self.index[ins].discard(len(self.vals) - 1)
        self.vals.pop()
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.vals)


#more info: if what the element we want to remove is exactly the last element, self.idx[ins] will be empty first, and discard will yield error so add first

# set 注意!! in general, sets don't support indexing or slicing.解法 list化

# The built-in method, discard() in Python, removes the element from the set only if the element is present in the set. 
# If the element is not present in the set, then no error or exception is raised and the original set is printed.
# If the element is present in the set:

# Method 2: Use of remove() method

# The built-in method, remove() in Python, removes the element from the set only if the element is present in the set, 
# just as the discard() method does but If the element is not present in the set, then an error or exception is raised.
# If the element is present in the set:


# d = set()
# a = [1,2,3,4,5]
# d.update(a)
# a
# [1, 2, 3, 4, 5]
# d.discard(3)
# d
# {1, 2, 4, 5}
# d.pop()
# 1
# d.pop()
# 2


# Python Set | pop()
# This in-built function of Python helps to pop out elements from a set just like the principal used in the concept while implementing Stack. 
# This method removes a random element from the set and returns the removed element. Unlike, a stack a random element is popped off the set.

# S = {"ram", "rahim", "ajay", "rishav", "aakash"} 
  
# # Popping three elements and printing them 
# print(S.pop()) 
# print(S.pop()) 
# print(S.pop()) 
  
# # The updated set 
# print("Updated set is", S) 
# Output:

# rishav
# ram
# rahim
# Updated set is {'aakash', 'ajay'}














