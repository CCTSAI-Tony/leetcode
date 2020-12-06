'''
Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
'''

# 刷題用這個, Time complexity: O(n) where n is the number of nodes in the linked list, Space complexity: O(1)
# 思路: 分別建立odd, and even head, 最後odd.next 接 evenhead
class Solution:
    def oddEvenList(head):
            if not head or not head.next: 
                return head

            odd = head
            even = head.next
            evenHead = even
            
            while even and even.next:
                odd.next = even.next
                odd = odd.next
                even.next = odd.next
                even = even.next
            
            odd.next = evenHead
            return head

#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        oddhead = head
        evenhead = head.next
        odd = oddhead
        even = evenhead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return oddhead

# 最主要注意就是不要在過程中出現None node 因為 None, which has no attribute 'next'
# Four conditions I doubt for the while-loop:

# odd and odd.next -> wrong when 1->2->3->4->None ( even nodes ) because even.next is None, which has no attribute 'next'
# odd and even.next -> wrong when 1->2->3->4->5->None ( odd nodes ) because even is None, which has no attribute 'next'
# even and odd.next -> wrong when 1->2->3->4->None ( even nodes ) because even.next is None, which has no attribute 'next'
# even and even.next -> correct
# 1. when 1->2->3->4->5->None ( odd nodes ) even will become None first and at the same time, 
# odd points at the last node of the linked list; therefore, breaks from the while loop.
# 2. when 1->2->3->4->None ( even nodes ) even.next will become None first and at the same time, 
# odd points at the last-2 node of the linked list and even points at the last node of the linked list; therefore, breaks from the while loop.