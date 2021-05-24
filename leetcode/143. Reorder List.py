'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#  刷題用這個, time complexity: O(n), space complexity O(n)
#  思路: 利用stack 來存取ListNode, 並利用左右index 來操縱stack 裡 ListNode的next指針要接誰
#  記得再把最後一個ListNode next指針 接None
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack=[]  #存放ListNode
        pointer=head
        while pointer:
            stack.append(pointer)
            pointer=pointer.next
        left=0
        right=len(stack)-1
        while left < right:
            stack[left].next=stack[right]
            left+=1
            stack[right].next=stack[left]
            right-=1
        if stack: #避免stack =  [], 最後的left.next = None, 觀察例子就知道為什麼, left+= 1 是關鍵
            stack[left].next=None

# 1->2->3->4->5
# 1->2->3->4

# class ListNode:
#      def __init__(self, x):
#          self.val = x
#          self.next = None


# a = ListNode(5)
# a.next = a

# ListNode.next 可以接自己

#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        l, r = 0, len(stack) - 1
        while l < r:
            temp = stack[l].next
            stack[l].next = stack[r]
            stack[r].next = temp
            l += 1; r -= 1
        stack[l].next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return head
        llist = [] #use list[] to arrange listnode
        llist.append(None)
        i = 1 #llist[0] = None
        while(head):
            llist.append(head)
            head = head.next
        for i in range(1,len(llist) // 2): #向下取整
            llist[i].next = llist[-i]
            llist[-i].next = llist[i + 1]
        if (len(llist) % 2) == 1:
            llist[(len(llist) // 2) + 1].next = llist[0] #決定誰接 None
        else:
            llist[(len(llist) // 2)].next = llist[0]

            None1->1->2->3->4->5.






















