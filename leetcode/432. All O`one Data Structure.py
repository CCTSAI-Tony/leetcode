'''
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. 
It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"
 

Constraints:

1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.
'''


# 刷題用這個, time complexity O(1), space complexity O(n)
# 思路: double linked list => value 越小擺前面 越大擺後面, 每個node 有 key set 代表這些key 都有相同的value
class Node(object):
    def __init__(self, val=0):
        self.num = val
        self.key_set = set() # 重要, find key in set() => O(1)
        self.prev = None
        self.next = None
        
class AllOne(object):
    def __init__(self):
        self.head = Node() 
        self.tail = Node()  
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = collections.defaultdict(Node)  

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if not key in self.cache:  
            cur = self.head  # default one with value = 0
        else:
            cur = self.cache[key]
            cur.key_set.remove(key)

        if cur.num + 1 != cur.next.num:  # fine out smaller one, put it in the front
            new_node = Node(cur.num + 1)
            self._insert_after(cur, new_node)
        else:
            new_node = cur.next

        new_node.key_set.add(key)  # add the key under the node with same value
        self.cache[key] = new_node  # update hash map

        if not cur.key_set and cur.num != 0:  # 該node 裡面已經沒有key了 而且又不是default head, 刪掉它
            self._remove(cur)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if not key in self.cache:
            return

        cur = self.cache[key]
        self.cache.pop(key)  # 先pop掉該key, 因為有可能decrease 後, val = 0
        cur.key_set.remove(key)

        if cur.num != 1:
            if cur.num - 1 != cur.prev.num:  
                new_node = Node(cur.num - 1)
                self._insert_after(cur.prev, new_node)
            else:
                new_node = cur.prev
            new_node.key_set.add(key)
            self.cache[key] = new_node

        if not cur.key_set and cur.num != 0:  
            self._remove(cur)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        """
        if self.tail.prev.num == 0:
            return ""
        key = self.tail.prev.key_set.pop()  # pop and add back to get arbitrary (but not random) element
        self.tail.prev.key_set.add(key)
        return key

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        """
        if self.head.next.num == 0:
            return ""
        key = self.head.next.key_set.pop()
        self.head.next.key_set.add(key)
        return key

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _insert_after(self, node, new_block):
        old_after = node.next
        node.next = new_block
        new_block.prev = node
        new_block.next = old_after
        old_after.prev = new_block



# 重寫第二次, time complexity O(1), space complexity O(n)
from collections import defaultdict
class Node:
    def __init__(self, val=0):
        self.val = val
        self.key_set = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.cache = defaultdict(Node)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def _insert_after(self, node, insert_node):
        node_next = node.next
        node.next = insert_node
        insert_node.prev = node
        insert_node.next = node_next
        node_next.prev = insert_node
        
    def inc(self, key: str) -> None:
        if not key in self.cache:
            cur = self.head
        else:
            cur = self.cache[key]
            cur.key_set.remove(key)
        if cur.val + 1 != cur.next.val:
            new_node = Node(cur.val + 1)
            self._insert_after(cur, new_node)
        else:
            new_node = cur.next
        new_node.key_set.add(key)
        self.cache[key] = new_node
        if not cur.key_set and cur.val != 0:
            self._remove(cur)
            
        
    def dec(self, key: str) -> None:
        cur = self.cache[key]
        cur.key_set.remove(key)
        if cur.val != 1:
            if cur.val - 1 != cur.prev.val:
                new_node = Node(cur.val - 1)
                self._insert_after(cur.prev, new_node)
            else:
                new_node = cur.prev
            new_node.key_set.add(key)
            self.cache[key] = new_node
        else:
            del self.cache[key]
        if not cur.key_set and cur.val != 0:
            self._remove(cur)
        

    def getMaxKey(self) -> str:
        if self.tail.prev.val == 0:
            return ""
        else:
            key = self.tail.prev.key_set.pop()
            self.tail.prev.key_set.add(key)
            return key
        

    def getMinKey(self) -> str:
        if self.head.next.val == 0:
            return ""
        else:
            key = self.head.next.key_set.pop()
            self.head.next.key_set.add(key)
            return key














