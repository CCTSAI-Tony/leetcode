'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''


#time complexity O(n), space complexity O(1)
#思路: 使用dummy 與異步pointer 解題
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: 
            return head  # 沒有 or 只有一個node
        dummy = ListNode(0)
        dummy.next = head # 接起來
        cur = dummy
        
        while cur.next and cur.next.next:
            first = cur.next
            sec = cur.next.next
            cur.next = sec  # 重要!
            first.next = sec.next
            sec.next = first
            cur = first
        return dummy.next   


#重寫第二次, time compexity O(n), space complexity O(1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = pre = cur = ListNode(0)
        dummy.next = head
        cur = cur.next
        while cur and cur.next:
            nxt = cur.next.next
            pre.next = cur.next
            cur.next.next = cur
            pre = cur
            cur = nxt
        pre.next = cur
        return dummy.next

#重寫第三次, time complexity O(n), space complexity O(1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = pre = cur = ListNode()
        dummy.next = head
        cur = cur.next
        while cur and cur.next:
            nxt = cur.next.next
            pre.next = cur.next
            cur.next.next = cur
            cur.next = nxt
            pre = cur
            cur = nxt
        return dummy.next


# 重寫第四次, time complexity O(n), space complexity O(1)
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = cur = ListNode(0)
        dummy.next = head
        while cur.next and cur.next.next:
            first = cur.next
            second = first.next
            cur.next = second
            first.next = second.next
            second.next = first
            cur = first
        return dummy.next

