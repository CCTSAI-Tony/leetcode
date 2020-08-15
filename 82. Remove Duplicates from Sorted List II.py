# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head):
        dummy = pre = ListNode(0) #dummy head  想像dummy 跟 pre 是同一條線 與head是不同條, pre 來負責接縫
        dummy.next = head
        while head and head.next: #去除 head = 單一元素 or none
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val: #跳過有重複的元素
                    head = head.next
                head = head.next #前進
                pre.next = head  #pre.next接head  跳過重複 (遇到重複 pre.next會不斷變化)
            else:
                pre = pre.next
                head = head.next
        return dummy.next


'''
 0 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 ->None
dp h(d.next)
 d p    h
 d      p    h
 d           h... h>>> h(p.next)
 d                          h>>>>h(p.next)
           

dummy.next = 1->2->5

0 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 4 ->None
dp h(d.next)
 d p    h
 d      p    h
 d           h... h>>> h(p.next)
 d                              h>>>>>h(p.next) 
 d          

dummy.next = 1->2 


'''












'''

Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3







'''




