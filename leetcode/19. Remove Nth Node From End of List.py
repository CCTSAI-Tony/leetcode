# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:

# Given n will always be valid.

# Follow up:

# Could you do this in one pass?

#自己重寫 time complexity O(n)
#思路: 利用dummy head 與快慢指針使得快指針到最後一個節點時, 慢指針的下一個節點就是 n-th node from the end, dummy->1->2->3->4->5->Null, 自己推導就懂
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = pre = cur = ListNode(0)
        dummy.next = head
        for _ in range(n): #先拉開快慢指針距離
            cur = cur.next
        while cur.next:
            cur = cur.next
            pre = pre.next
        pre.next = pre.next.next
        return dummy.next

#重寫第二次, one pass time complexity O(n), space complexity O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = slow = fast = ListNode(0)
        dummy.next = head
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next




class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head  #list node 大家起始都在第一個節點
        for _ in range(n):  #_ 代表只要迴圈, 其他不重要  換i也可以
            fast = fast.next
        if not fast: #針對n = lemgh(head)
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head



        #The standard solution, but without a dummy extra node. Instead, I simply handle the special case of removing the head (right after) the fast cursor got its head start.

        #1>2>3>4>5

        # Definition for singly-linked list.
        # class ListNode:
        #     def __init__(self, x):
        #         self.val = x
        #         self.next = None
'''
1>2>3>4>5>6>7   n=4           
            f
    s   s'
h

head = 1>2>3>5>6>7





1>2>3>4>5>6>7 none n=1
            f
          s   s'  
h

head = 1>2>3>4>5>6


1>2>3>4>5>6>7 none  n=7           
              f
s   
  h

head = 2>3>4>5>6>7


1>2>3>4>5>6>7 none  n=6           
            f
s   s'
h

head = 1>3>4>5>6>7





'''