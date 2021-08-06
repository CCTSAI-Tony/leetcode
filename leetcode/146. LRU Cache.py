'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. 
When the cache reached its capacity, it should (invalidate the least recently used item before inserting a new item.)v

The cache is initialized with a positive capacity. => capacity 是正數

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''



https://www.youtube.com/watch?v=7v_mUfpg46E&feature=youtu.be
#刷題用這個, two pointer!!
#思路: Python Dict + Double LinkedList
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict() # self.dic = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key] #key:node
            self._remove(n) #每get一次 就要把get項目拿出來放在排序第一的位置 因此先remoce 再 add
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n) #一樣 put因為觸碰了原本的key 變常用了 在listNode 把key remove
        n = Node(key, value)
        self._add(n) #重新加回listNode
        self.dic[key] = n #新建 key:value pair or 重新定義key:value  => update
        if len(self.dic) > self.capacity:
            n = self.head.next #把head 下一個 remove 也就是the least recently used item
            self._remove(n)
            del self.dic[n.key] #把dict node對應的key消除

    def _remove(self, node): #消除當前node
        p = node.prev 
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node): #把當前node 放在最後, self.tail的前一個
        p = self.tail.prev #這樣寫是不干擾self.head 預設值
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


# 刷題用這個, duble linked list 自環
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.memo = {}
        self.head = Node(-1, -1)
        self.head.next = self.head
        self.head.prev = self.head

    def get(self, key: int) -> int:
        if key in self.memo:
            node = self.memo[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.memo:
            node = self.memo[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            if len(self.memo) >= self.capacity:
                last = self.head.prev
                self.remove(last)
                del self.memo[last.key]
            node = Node(key, value)
            self.add(node)
            self.memo[node.key] = node
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        
    def add(self, node):
        head = self.head
        nxt = head.next
        head.next = node
        node.prev = head
        nxt.prev = node
        node.next = nxt


#重寫第二次, time complexity O(1), space complexity O(n), using dict & double linkedlist
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.prev = self.tail
        self.tail.next = self.head
        self.dict = dict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.dict:
            n = self.dict[key]
            self.remove(n)
            self.add(n)
            return n.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            n = self.dict[key]
            self.remove(n)
            n.val = value
            self.add(n)
        else: 
            if len(self.dict) >= self.capacity:
                k = self.tail.next
                self.remove(k)
            n = Node(key, value)
            self.add(n)
        
    
    def remove(self, n):
        pre = n.prev
        nxt = n.next
        pre.next = nxt
        nxt.prev = pre
        del self.dict[n.key]
        
    
    
    def add(self, n):
        pre = self.head.prev
        pre.next = n
        n.prev = pre
        n.next = self.head
        self.head.prev = n
        self.dict[n.key] = n


#重寫第三次, time complexity O(1), space complexity O(n)
class Node:
    
    def __init__(self, key=0, val=0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        del self.dic[node.key]
        
    def add(self, node):
        prev = self.tail.prev
        self.tail.prev = node
        prev.next = node
        node.next = self.tail
        node.prev = prev
        self.dic[node.key] = node
    
    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            node = Node(key, value)
            if len(self.dic) >= self.capacity:
                old = self.head.next
                self.remove(old)
            self.add(node)




# 刷題用這個 還是使用OrderedDict 好, 搭配460
# Python concise solution with comments (Using OrderedDict).
# 思路: 利用orderdict 來記錄建立key:value pair 的順序, 這樣之後到達capacity就不會 remove錯 item
# 遇到operate 的 item, pop 該item 並重新加進dict裡, pop key in dic, time complexity O(1)
# time complexity of OrderedDict.move_to_end() => O(1)
import collections
class LRUCache:
    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):  #O(1) time complexity
        if key not in self.dic:
            return -1
        v = self.dic.pop(key) #把對應的 key:value pair pop 出來, 並return value, time complexity O(1)
        self.dic[key] = v   # 再重新建立key:value pair, 放在orderdict 最後面, 也就是最近用的item放在最後面
        return v

    def set(self, key, value):  #O(1) time complexity
        if key in self.dic:    
            self.dic.pop(key)  #把舊位置pop掉, 因為之後要重新建立放在最後面
        else:
            if self.remain > 0:
                self.remain -= 1  
            else:  # self.dic is full
                self.dic.popitem(last=False) #orderdict 才有的last=False, pop掉第一個item, 最不經常用的
        self.dic[key] = value #建立key:value pair, 放在orderdict 最後面

# OrderedDict.popitem() returns the first or last key-value, after deleting it. 
# Setting last to False signals you wanted to remove the first.

#重寫第二次, get, put => time complexity O(1)
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.dic = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)
        else:
            if self.capacity == 0:
                self.dic.popitem(last=False)
            else:
                self.capacity -= 1
        self.dic[key] = value

#重寫第三次, time complexity O(1) for get, put method
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.dic = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dic:
            self.dic.move_to_end(key)
            return self.dic[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key] = value
            self.dic.move_to_end(key)
        else:
            if self.capacity == 0:
                self.dic.popitem(last=False)
            else:
                self.capacity -= 1
            self.dic[key] = value









# 刷題用這個, 不需OrderedDict, python 3.7 dict 預設就是ordered, time complecity get, put = O(1)
# 思路: 利用dict 來記錄建立key:value pair 的順序, 這樣之後到達capacity就不會 remove錯 item
# 技巧: 使用 next(iter(self.dict)) 來找出 self.dict 第一個key是什麼, self.dict.pop(第一個key) 
class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        
        
    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        v = self.dict.pop(key)
        self.dict[key] = v
        return v
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                first = next(iter(self.dict))
                self.dict.pop(first)
        self.dict[key] = value










solution vedio

https://www.youtube.com/watch?v=7v_mUfpg46E&feature=youtu.be
#Python Dict + Double LinkedList
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict() # self.dic = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key] #key:node
            self._remove(n) #每get一次 就要把get項目拿出來放在排序第一的位置 因此先remoce 再 add
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n) #一樣 put因為觸碰了原本的key 變常用了 在listNode 把key remove
        n = Node(key, value)
        self._add(n) #重新加回listNode
        self.dic[key] = n #新建 key:value pair or 重新定義key:value 相同key 可以有不同value 
        if len(self.dic) > self.capacity:
            n = self.head.next #把head 下一個 remove 也就是the least recently used item
            self._remove(n)
            del self.dic[n.key] #把dict node對應的key消除

    def _remove(self, node): #消除當前node
        p = node.prev 
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node): #把當前node 放在最後, self.tail的前一個
        p = self.tail.prev #這樣寫是不干擾self.head 預設值
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail




a = {}
a[4]=3
a
{4: 3}
del a[4]
a
{}

#regular dict
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)
a A
b B
c C
d D
e E

#An OrderedDict
import collections
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'
for k, v in d.items():
    print(k, v)

a A
b B
c C
d D
e E

A regular dict does not track the insertion order, and iterating over it produces the values in an arbitrary order. 
In an OrderedDict, by contrast, the order the items are inserted is remembered and used when creating an iterator.


A regular dict looks at its contents when testing for equality. An OrderedDict also considers the order the items were added.

import collections

print 'dict       :',
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = {}
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2

print 'OrderedDict:',

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = collections.OrderedDict()
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2

dict       : True
OrderedDict: False


#OrderedDict
import collections
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'
for k, v in d.items():
    print(k, v)
a A
b B
c C
d D
e E

d.pop('a')
'A'
d
OrderedDict([('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E')])
d['a'] = 'A'
d
OrderedDict([('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E'), ('a', 'A')])

OrderedDict.popitem() returns the first or last key-value, after deleting it. 
Setting last to False signals you wanted to remove the first.


d.popitem(last=False)
('b', 'B')




















































