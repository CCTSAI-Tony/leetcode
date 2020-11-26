'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):  #這題不能粗心大意 要考慮所有邊界狀況 例如 防止nonetype.next
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        return dummy_head.next

'''
Before writing any code, it's good to make a list of edge cases that we need to consider. 
This is so that we can be certain that we're not overlooking anything while coming up with our algorithm, 
and that we're testing all special cases when we're ready to test. These are the edge cases that I came up with.

The linked list is empty, i.e. the head node is None.
Multiple nodes with the target value in a row.
The head node has the target value.
The head node, and any number of nodes immediately after it have the target value.
All of the nodes have the target value.
The last node has the target value.
So with that, this is the algorithm I came up with.

In order to save the need to treat the "head" as special, the algorithm uses a "dummy" head. 
This simplifies the code greatly, particularly in the case of needing to remove the head AND some of the nodes immediately after it.

Then, we keep track of the current node we're up to, and look ahead to its next node, as long as it exists. 
If current_node.next does need removing, then we simply replace it with current_node.next.next. 
We know this is always "safe", because current_node.next is definitely not None (the loop condition ensures that), so we can safely access its next.

Otherwise, we know that current_node.next should be kept, and so we move current_node on to be current_node.next.

The loop condition only needs to check that current_node.next != None. 
The reason it does not need to check that current_node != None is because this is an impossible state to reach. 
Think about it this way: The ONLY case that we ever do current_node = current_node.next 
in is immediately after the loop has already confirmed that current_node.next is not None.

The algorithm requires O(1) extra space and takes O(n) time.


'''

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        dummy = p = ListNode(0)
        dummy.next = head
        while p.next != None:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next
