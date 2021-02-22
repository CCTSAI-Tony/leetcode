'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
 

Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
Number of Nodes will not exceed 1000.
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# 刷題用這個
# using dictionary, time complexity O(n)
# 思路:  利用dict 來存放相對應的copy node, 再遍歷linked list來把相對應的copy node串連起來, 高招!
class Solution(object):    
  def copyRandomList(self, head):
      if not head:
          return 
      cur, dic = head, {}
      # copy nodes
      while cur:
          dic[cur] = Node(cur.val)
          cur = cur.next
      cur = head  #back to start point
      # point to copy random pointers
      while cur:
          if cur.random:  #預設cur.random = None
              dic[cur].random = dic[cur.random]
          if cur.next:
              dic[cur].next = dic[cur.next]
          cur = cur.next
      return dic[head]

#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.random:
                dic[cur].random = dic[cur.random]
            if cur.next:
                dic[cur].next = dic[cur.next]
            cur = cur.next
        return dic[head]


#重寫第三次, time complexity O(n), space complexity O(n)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cur = head
        dic = {}
        while cur:
            node = Node(cur.val)
            dic[cur] = node
            cur = cur.next
        cur = head
        while cur:
            copy = dic[cur]
            nxt = cur.next
            rand = cur.random
            if nxt:
                copy.next = dic[nxt]
            if rand:
                copy.random = dic[rand]
            cur = cur.next
        return dic[head]


#重寫第三次, time complexity O(n), space complexity O(n)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        dic = {}
        dummy = head
        while head:
            copy_node = Node(head.val)
            dic[head] = copy_node
            head = head.next
        head = dummy
        while head:
            nxt = head.next
            random = head.random
            if nxt:
                dic[head].next = dic[nxt]
            if random:
                dic[head].random = dic[random]
            head = head.next
        return dic[dummy]


#  這有可能follow up, 不使用dict 優化
#  time complexity O(n), space complexity O(2n) => O(n)
#  思路: 先建立A --> A' --> B --> B' --> C --> C' --> D --> D', 再從頭遍歷把各個copynode 的random pointer 接上 random copynode
#  最後從頭遍歷拆分 old and new linked list
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        p = head
        while p:
            node = Node(p.val)
            node.next = p.next
            p.next = node
            p = p.next.next
            # p = node.next
        p = head    
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        newhead = head.next
        pold = head
        pnew = newhead
        while pnew.next:  #這邊tricky, 若pnew.next == None, pnew.next = pold.next => None.next => error
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return newhead






