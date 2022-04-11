'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3




'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#刷題用這個, time complexity O(n), space complexity O(1)
#思路: 使用dummy node 與 pre, head 異步指針來解題
class Solution:
	def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next


# 重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = fast = head
        while fast:
            while fast and fast.val == slow.val:
                fast = fast.next
            slow.next = fast
            slow = slow.next
            if fast:
                fast = fast.next
        return head





