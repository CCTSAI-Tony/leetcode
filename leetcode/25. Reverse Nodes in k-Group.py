# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# Follow up:

# Could you solve the problem in O(1) extra memory space?
# You may not alter the values in the list's nodes, only nodes itself may be changed.
 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
# Example 3:

# Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]
# Example 4:

# Input: head = [1], k = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is in the range sz.
# 1 <= sz <= 5000
# 0 <= Node.val <= 1000
# 1 <= k <= sz

# This problem is a standard follow up to
# LC 206 Reverse Linked List

# A lot of the solutions implemented the reversing logic from scratch
# I am going to pretend that I just finish writing the standard reverse method, and reuse the method on the follow up.


#刷題用這個, time complexity O(n), space complexity O(1)
#思路: 利用count variable 來記錄reverse 次數, 並使用reverse linked list 遞迴來連結nodes
class Solution(object):
    def reverseKGroup(self, head, k):
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k: 
            return head
        new_head, prev = self.reverse(head, count) #此時回傳的prev 是區間的第一個node
        head.next = self.reverseKGroup(new_head, k) #此時最初的head已被調換至最後面, 且next 為None, 使用recursion 來接下一個區間的第一個node
        return prev
    
    def reverse(self, head, count):
        prev, cur, nxt = None, head, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev) # 下一區間的第一個node, 此區間反轉後第一個node



#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1
        if count < k:
            return head
        newHead, prev = self.reverse(head, count)
        head.next = self.reverseKGroup(newHead, k)
        return prev
        
    def reverse(self, node, count):
        prev = None
        while count:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
            count -= 1
        return (node, prev)

#重寫第三次, time complexity O(n), space complexity O(1)
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = k - 1
        node = head
        while node and count:
            node = node.next
            count -= 1
        if not node:
            return head
        new_head, cur_head = self.reverse(head, k)
        cur_tail = head
        cur_tail.next = self.reverseKGroup(new_head, k)
        return cur_head
    
    def reverse(self, head, k):
        cur, prev = head, None
        while k:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            k -= 1
        return nxt, prev

# 重寫第四次, time complexity O(n), space complexity O(1)
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node, count):
            cur, prev = node, None
            while count:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                count -= 1
            return (cur, prev)
        
        node = head
        counts = 0
        while node:
            node = node.next
            counts += 1
        if counts < k:
            return head
        new_head, cur_head = reverse(head, k)
        head.next = self.reverseKGroup(new_head, k)
        return cur_head

