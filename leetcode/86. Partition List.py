'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        h1 = l1 = ListNode(0)   #2 pointer
        h2 = l2 = ListNode(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next #推進
        l2.next = None #若沒這行就無法斷點 會出現 Error - Found cycle in the ListNode  listnode尾端next最終要接 None
        l1.next = h2.next
        return h1.next


# 自己想的, time complexity O(n)
# 思路:  額外建立兩個dummy head 與 大小指針 來分別串連比x小 or 相等or大於x 的 node, 最後兩個list串連在一起
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = cur = ListNode(0)
        small = smaller = ListNode(0)
        big = bigger = ListNode(0)
        dummy.next = head
        while cur.next:
            if cur.next.val < x:
                smaller.next = cur.next
                smaller = smaller.next
                cur = cur.next
            elif cur.next.val >= x:
                bigger.next = cur.next
                bigger = bigger.next
                cur = cur.next
        bigger.next = None
        smaller.next = big.next
        return small.next



