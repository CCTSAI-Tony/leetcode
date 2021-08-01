'''
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, 
it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, 
when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. 
This number is set to zero when the item is removed.

 

Follow up:
Could you do both operations in O(1) time complexity?

 

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

# Explanation
# Each key is mapping to the corresponding node (self._node), where we can retrieve the node in O(1) time.

# Each frequency freq is mapped to a Doubly Linked List (self._freq), where all nodes in the DLinkedList have the same frequency, 
# freq. Moreover, each node will be always inserted in the head (indicating most recently used).

# A minimum frequency self._minfreq is maintained to keep track of the minimum frequency of across all nodes in this cache, 
# such that the DLinkedList with the min frequency can always be retrieved in O(1) time.

# Here is how the algorithm works
# get(key)

# query the node by calling self._node[key]
# find the frequency by checking node.freq, assigned as f, and query the DLinkedList that this node is in, through calling self._freq[f]
# pop this node
# update node's frequence, append the node to the new DLinkedList with frequency f+1
# if the DLinkedList is empty and self._minfreq == f, update self._minfreq to f+1.
# return node.val
# put(key, value)

# If key is already in cache, do the same thing as get(key), and update node.val as value
# Otherwise:
# if the cache is full, pop the least frequenly used element (*)
# add new node to self._node
# add new node to self._freq[1]
# reset self._minfreq to 1
# (*) The least frequently used element is the tail element in the DLinkedList with frequency self._minfreq


# 刷題用這個
# 使用double linked list 搭配 freq map 來存儲不同頻率的double linked list
# 技巧, 只使用一個dummy node 自環, 來完成double linked list 初始化
from collections import defaultdict
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 1

class DLinkedList:
    def __init__(self):
        self.sentinel = Node(None, None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.size = 0
        
    def append(self, node):
        node.next = self.sentinel.next
        node.prev = self.sentinel
        node.next.prev = node
        self.sentinel.next = node
        self.size += 1
        
    def pop(self, node=None):
        if self.size == 0:
            return
        if node == None:
            node = self.sentinel.prev # pop out the last one item
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node
    
    
class LFUCache:

    def __init__(self, capacity: int):
        self.nodes = dict()
        self.freqs = defaultdict(DLinkedList)  # 每個freq 都是一個Dlinkedlist
        self.capacity = capacity
        self.size = 0
        self.minfreq = 0
        
    def _update(self, node):
        freq = node.freq
        node = self.freqs[freq].pop(node)
        if freq == self.minfreq and self.freqs[freq].size == 0:
            self.minfreq += 1
        node.freq += 1
        freq = node.freq
        self.freqs[freq].append(node)
        

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._update(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key not in self.nodes:
            node = Node(key, value)
            if self.size == self.capacity:
                tail = self.freqs[self.minfreq].pop()
                del self.nodes[tail.key]
                self.size -= 1
            self.minfreq = 1
            self.nodes[key] = node
            self.freqs[1].append(node)
            self.size += 1
        else:
            node = self.nodes[key]
            self._update(node)
            node.val = value

# 重寫第二次
from collections import defaultdict
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 1

class DLinkedList:
    def __init__(self):
        self.sentinel = Node(None, None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.size = 0
        
    def append(self, node):
        node.next = self.sentinel.next
        self.sentinel.next = node
        node.prev = self.sentinel
        node.next.prev = node
        self.size += 1
        
    def pop(self, node=None):
        if self.size == 0:
            return
        self.size -= 1
        if node == None:
            node = self.sentinel.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        return node
    
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.nodes = {}
        self.freqs = defaultdict(DLinkedList)
        self.min_freq = 0
        
    def update(self, node):
        freq = node.freq
        self.freqs[freq].pop(node)
        if freq == self.min_freq and self.freqs[freq].size == 0:
            self.min_freq += 1
        node.freq += 1
        self.freqs[node.freq].append(node)
        
    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self.update(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.nodes:
            node = self.nodes[key]
            self.update(node)
            node.val = value
            
        else:
            node = Node(key, value)
            if self.size == self.capacity:
                last = self.freqs[self.min_freq].pop()
                self.size -= 1
                del self.nodes[last.key]
            self.min_freq = 1
            self.size += 1
            self.nodes[node.key] = node
            self.freqs[1].append(node)



# 刷題用這個
# 使用double linked list 搭配 freq map 來存儲不同頻率的double linked list
import collections
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next - None

class DLinkedList:
    """ An implementation of doubly linked list.
    
    Two APIs provided:
    
    append(node): append the node to the head of the linked list.
    pop(node=None): remove the referenced node. 
                    If None is given, remove the one from tail, which is the least recently used.
                    
    Both operation, apparently, are in O(1) complexity.
    """
    def __init__(self):
        self._sentinel = Node(None, None) # dummy node
        self._sentinel.next = self._sentinel.prev = self._sentinel #自環
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def append(self, node):
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        self._sentinel.next = node
        self._size += 1
    
    def pop(self, node=None):
        if self._size == 0:
            return
        
        if not node:  # pop tail node
            node = self._sentinel.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        
        return node
        
class LFUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        
        Three things to maintain:
        
        1. a dict, named as `self._node`, for the reference of all nodes given key.
           That is, O(1) time to retrieve node given a key.
           
        2. Each frequency has a doubly linked list, store in `self._freq`, where key
           is the frequency, and value is an object of `DLinkedList`
        
        3. The min frequency through all nodes. We can maintain this in O(1) time, taking
           advantage of the fact that the frequency can only increment by 1. Use the following
           two rules:
           
           Rule 1: Whenever we see the size of the DLinkedList of current min frequency is 0,
                   the min frequency must increment by 1.
           
           Rule 2: Whenever put in a new (key, value), the min frequency must 1 (the new node)
           
        """
        self._size = 0
        self._capacity = capacity
        
        self._node = dict() # key: Node
        self._freq = collections.defaultdict(DLinkedList)
        self._minfreq = 0
        
        
    def _update(self, node):
        """ 
        This is a helper function that used in the following two cases:
        
            1. when `get(key)` is called; and
            2. when `put(key, value)` is called and the key exists.
         
        The common point of these two cases is that:
        
            1. no new node comes in, and
            2. the node is visited one more times -> node.freq changed -> 
               thus the place of this node will change
        
        The logic of this function is:
        
            1. pop the node from the old DLinkedList (with freq `f`)
            2. append the node to new DLinkedList (with freq `f+1`)
            3. if old DlinkedList has size 0 and self._minfreq is `f`,
               update self._minfreq to `f+1`
        
        All of the above opeartions took O(1) time.
        """
        freq = node.freq
        
        self._freq[freq].pop(node)
        if self._minfreq == freq and not self._freq[freq]:
            self._minfreq += 1
        
        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)
    
    def get(self, key):
        """
        Through checking self._node[key], we can get the node in O(1) time.
        Just performs self._update, then we can return the value of node.
        
        :type key: int
        :rtype: int
        """
        if key not in self._node:
            return -1
        
        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        """
        If `key` already exists in self._node, we do the same operations as `get`, except
        updating the node.val to new value.
        
        Otherwise, the following logic will be performed
        
        1. if the cache reaches its capacity, pop the least frequently used item. (*)
        2. add new node to self._node
        3. add new node to the DLinkedList with frequency 1
        4. reset self._minfreq to 1
        
        (*) How to pop the least frequently used item? Two facts:
        
        1. we maintain the self._minfreq, the minimum possible frequency in cache.
        2. All cache with the same frequency are stored as a DLinkedList, with
           recently used order (Always append at head)
          
        Consequence? ==> The tail of the DLinkedList with self._minfreq is the least
                         recently used one, pop it...
        
        :type key: int
        :type value: int
        :rtype: void
        """
        if self._capacity == 0:
            return
        
        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._freq[self._minfreq].pop()
                del self._node[node.key]
                self._size -= 1
                
            node = Node(key, value)
            self._node[key] = node
            self._freq[1].append(node)
            self._minfreq = 1
            self._size += 1













# First, OrderedDict is a dict + double linked list.

# A count2node is a dict of OrderedDict, so you can look up like this count2node[count][key] to remove/update the node in O(1), 
# or count2node[count].popitem(last=True) to remove the oldest node in O(1).

# With this tool, we can easily write a simple code like this:

#time complexity get, put time complexity O(1), 使用defaultdict & OrderedDict
#思路: 此題跟146 最大不同是, 此題要紀錄每個key的使用頻率, 使用Node class, pop出頻率最小的, 而不是最近使用的, 然而若頻率一樣的話則pop出 least recently item
#利用defaultdict 與 OrderedDict 的搭配來儲存不同count 的item, 每個count 裡面是一個OrderedDict, 用來處理count相同時能pop掉 least recently item
#小心此題capacity 有可能=None
#此題 count2node empty key 要清除key還是不清除key都可以, 
#若沒清除 if self.minCount not in self.count2node 要改成 if not self.count2node[self.minCount], 不然 self.minCount 不會+1
from collections import defaultdict, OrderedDict
class Node:
    def __init__(self, key, val, count):
        self.key = key #這個attribute 是不必要的
        self.val = val
        self.count = count
    
class LFUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.key2node = {}
        self.count2node = defaultdict(OrderedDict) #重要, 使用OrderedDict
        self.minCount = None
        
    def get(self, key):
        if key not in self.key2node:
            return -1
        
        node = self.key2node[key]
        del self.count2node[node.count][key] 
        
        # clean memory
        if not self.count2node[node.count]:
            del self.count2node[node.count]
        
        node.count += 1 #node.count += 1, 因此 self.count2node[node.count][key] 要換到key = node.count+1 的地方, 原本的node要delete
        self.count2node[node.count][key] = node #insert again with update
        
        # NOTICE check minCount!!! 最小頻率沒有了, 最小頻率往上找+1
        if self.minCount not in self.count2node:
            self.minCount += 1
            
            
        return node.val
        
    def put(self, key, value):
        if not self.cap: # capacity = None 不能放任何東西
            return 
        
        if key in self.key2node:
            self.key2node[key].val = value #update
            self.get(key) # NOTICE, put makes count+1 too
            return
        
        if len(self.key2node) == self.cap:
            # popitem(last=False) is FIFO(first in first out), like queue
            # it return key and value!!!
            k, n = self.count2node[self.minCount].popitem(last=False) #OrderedDict popitem(), 才能用last=False, 一般dict不行
            del self.key2node[k] #別忘了 也要 key2node delete掉
        #新 node
        self.count2node[1][key] = self.key2node[key] = Node(key, value, 1)
        self.minCount = 1
        return

#刷題用這個
#重做第二次, time complexity O(1), space complexity O(n)
class Node:
    def __init__(self, val, count):
        self.val = val
        self.count = count

from collections import defaultdict, OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count2node = defaultdict(OrderedDict)
        self.key2node = {}
        self.minCount = None
        
        

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1
        node = self.key2node[key]
        del self.count2node[node.count][key]
        if not self.count2node[node.count]:
            del self.count2node[node.count]
        node.count += 1
        self.count2node[node.count][key] = node
        if self.minCount not in self.count2node:
            self.minCount += 1
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return
        if key in self.key2node:
            node = self.key2node[key]
            node.val = value
            self.get(key)
            return
        else:
            if len(self.key2node) == self.capacity:
                k, n = self.count2node[self.minCount].popitem(last=False)
                if not self.count2node[self.minCount]:
                    del self.count2node[self.minCount]
                del self.key2node[k]
            newNode = Node(value, 1)
            self.key2node[key] = self.count2node[1][key] = newNode
            self.minCount = 1











#自己重寫, 刷題用這個 get, put time complexity O(1), 沒有clean memory
from collections import defaultdict, OrderedDict
class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count
        
class LFUCache:

    def __init__(self, capacity: int):
        self.keyToNode = {}
        self.countToNode = defaultdict(OrderedDict)
        self.cap = capacity
        self.minfreq = None
        

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1
        node = self.keyToNode[key]
        del self.countToNode[node.count][key]
        node.count += 1
        self.countToNode[node.count][key] = node
        if not self.countToNode[self.minfreq]:
            self.minfreq += 1
        return node.val
            

    def put(self, key: int, value: int) -> None:
        if not self.cap:
            return
        elif key in self.keyToNode:
            self.keyToNode[key].val = value
            self.get(key)
            return
        else:
            if len(self.keyToNode) == self.cap:
                k, n = self.countToNode[self.minfreq].popitem(last=False) #orderedd dict 專屬用法
                del self.keyToNode[k]
                
            node = Node(key, value, 1)
            self.countToNode[1][key] = node
            self.keyToNode[key] = node
            self.minfreq = 1












