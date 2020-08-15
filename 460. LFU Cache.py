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

# First, OrderedDict is a dict + double linked list.

# A count2node is a dict of OrderedDict, so you can look up like this count2node[count][key] to remove/update the node in O(1), 
# or count2node[count].popitem(last=True) to remove the oldest node in O(1).

# With this tool, we can easily write a simple code like this:

#time complexity get, put time complexity O(1), 使用defaultdict & OrderedDict
#思路: 此題跟146 最大不同是, 此題要紀錄每個key的使用頻率, pop出頻率最小的, 而不是最近使用的, 然而若頻率一樣的話則pop出 least recently item
#利用defaultdict 與 OrderedDict 的搭配來儲存不同count 的item, 每個count 裡面是一個OrderedDict, 用來處理count相同時能pop掉 least recently item
#小心此題capacity 有可能=None
#此題 count2node empty key 要清除key還是不清除key都可以, 
#若沒清除 if self.minCount not in self.count2node 要改成 if not self.count2node[self.minCount], 不然 self.minCount 不會+1
from collections import defaultdict, OrderedDict
class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count
    
class LFUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.key2node = {}
        self.count2node = defaultdict(OrderedDict)
        self.minCount = None
        
    def get(self, key):
        if key not in self.key2node:
            return -1
        
        node = self.key2node[key]
        del self.count2node[node.count][key] #
        
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
            k, n = self.count2node[self.minCount].popitem(last=False) 
            del self.key2node[k] #別忘了 也要 key2node delete掉
        #新 node
        self.count2node[1][key] = self.key2node[key] = Node(key, value, 1)
        self.minCount = 1
        return


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
                k, n = self.countToNode[self.minfreq].popitem(last=False)
                del self.keyToNode[k]
                
            node = Node(key, value, 1)
            self.countToNode[1][key] = node
            self.keyToNode[key] = node
            self.minfreq = 1












