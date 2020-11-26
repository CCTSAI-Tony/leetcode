'''
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


 

Follow up:

Can you solve it using O(1) (i.e. constant) memory?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head):
        fast = slow = head

        while slow and fast and fast.next:
            slow = slow.next                # Step of 1
            fast = fast.next.next           # Setp of 2

            if slow is fast:                # Checking whether two pointers meet
                return True

        return False

'''
Multiple pointers having different steps are our friend to solve Linked List problems. 
We can set two pointers to "run through" the linked list. Since they have different pace, if the list is cyclic, they must meet after the starting point.

In this case I choose two pointers and steps are 1 and 2 respectively. I think assigning one step as 3 is also doable, but I have no ideas which one is better.
'''