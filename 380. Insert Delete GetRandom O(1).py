'''
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
'''


# Python // easy and clear solution // 96 ms // beats 99 %
#  思路: 利用stack 儲存元素, 並同時利用dict儲存在stack 的 index, 以利之後要remove特定元素做準備, 把要remove的item 與最後一個元素做交換, 之後pop()比較方便
#  最後利用random.choice 隨機從stack 挑選一個元素出來   
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.ind = [], {}
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.ind: #只能insert 未有的元素
            self.nums += [val]
            self.ind[val] = len(self.nums) - 1 #建立key:value pair, len(self.nums) - 1(紀錄目前在 self.nums 最新的index)
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.ind:
            ind, last = self.ind[val], self.nums[-1]
            self.nums[ind], self.ind[last] = last, ind  #replace the remove element with the last one!! => 這樣才不會影響其他元素!!
            self.nums.pop()  #please remember to pop the last one element
            self.ind.pop(val)  #pop(val)=> return val key's value and del dict key => 可以改成 del self.ind[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.nums) #從nums list 挑一個元素出來

#  自己重寫, 刷題用這個
#  思路: 利用stack 儲存元素, 並同時利用dict儲存在stack 的 index, 以利之後要remove特定元素做準備, 把要remove的item 與最後一個元素做交換, 之後pop()比較方便
#  最後利用random.choice 隨機從stack 挑選一個元素出來   
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.index = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.index:
            self.nums.append(val)
            self.index[val] = len(self.nums) - 1
            return True
        return False
    
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.index:
            idx = self.index[val]
            last = self.nums[-1]
            self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx] #exchange the remove element with the last one!! => 這樣才不會影響其他元素!!
            self.index[val], self.index[last] = self.index[last], self.index[val]
            self.nums.pop()
            del self.index[val]
            return True
        return False
            
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.nums)



# also can use this 
# idx = random.randint(0,self.length-1)
#        return self.arr[idx] 


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# You can combine the few lines in remove(), utilizing tuple unpacking -
# self.nums[ind], self.ind[self.nums[-1]] = self.ind[self.nums[-1]], self.nums[ind]

# Also, self.ind.pop(val) is the same as del self.ind[val] but that's a personal preference.

# a = {1:10,2:20,3:30,4:40}
# del a[3]
# a
# {1: 10, 2: 20, 4: 40}
# a.pop(2)
# 20
# a
# {1: 10, 4: 40}


# I think using len(self.nums) makes it O(n): no, its O(1)
# Incorrect: len is O(1)
# python list is based on array, so len function just get the index of array












