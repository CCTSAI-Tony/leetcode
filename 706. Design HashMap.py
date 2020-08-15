'''
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
'''


# I do not think array solutions are acceptable interviews. So here is my naive implementation of Hash with chaining. 
# One can play with m (number of slots in HashTable) to optimize the runtime. I got 90% with setting m = 1000.

# using just arrays, direct access table
# using linked list for chaining

#自己重寫, 刷題用這個
#思路: 因為總共的key 有10000000 先設一個數m, 讓key % m 可以讓整體index 控制在1000 
#太少也不行 hash collision會很嚴重 => 拖低效率, 再用 linked list 來處理hash collision 的情況
class ListNode:
    def __init__(self, key, val):
        self.pair = [key, val]
        self.next = None
           
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.list = [None] * 1000
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.m
        if not self.list[index]:
            self.list[index] = ListNode(key, value)
        else:
            cur = self.list[index]
            while cur:
                if cur.pair[0] == key:
                    cur.pair[1] = value
                    return
                if cur.next == None:
                    cur.next = ListNode(key, value)
                    return
                cur = cur.next
                    
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.m
        if not self.list[index]:
            return -1
        cur = self.list[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.m
        if not self.list[index]:
            return
        cur = prev = self.list[index]
        if cur.pair[0] == key:
            self.list[index] = cur.next
        cur = cur.next
        while cur:
            if cur.pair[0] == key:
                prev.next = cur.next
            cur, prev = cur.next, prev.next




#刷題用這個, 這個面試才會過
#思路: 因為總共的key 有10000000 先設一個數m, 讓key % m 可以讓整體index 變少, 再用 linked list 來處理hash collision 的情況
class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000;
        self.h = [None]*self.m
        

    def put(self, key, value): #list[index] => O(1000) = > O(1)
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = key % self.m #
        if self.h[index] == None:
            self.h[index] = ListNode(key, value)
        else:
            cur = self.h[index]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value) #update
                    return
                if cur.next == None: 
                    break
                cur = cur.next
            cur.next = ListNode(key, value)
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.m
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1
            
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = key % self.m
        cur = prev = self.h[index]
        if not cur: 
            return
        if cur.pair[0] == key:
            self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next




#面試不接受
#自己想的, time complexity O(1), 188ms
#思路: 建立一個普通dict 即可, 先確認key是否在dict 再del, 不然會key error
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.dict[key] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.dict:
            return self.dict[key]
        return -1
    

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.dict:
            del self.dict[key]


