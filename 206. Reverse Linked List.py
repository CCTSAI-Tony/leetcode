'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#刷題用這個 iterative
#自己重寫 time complexity O(n) 搭配 92 一起服用
#思路: 利用next_node 來暫存head.next, 再利用head, temp 指針轉換使後面node接前面node, 最後 next_node = head 開始新迴圈
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        temp = None
        while head and head.next:
            next_node = head.next
            head.next = temp
            temp = head
            head = next_node
        head.next = temp
        return head

#自己重寫, recusion, time complexity O(n)
#思路: 同樣利用 head, temp 指針轉換使後面node接前面node, 若head.next = None, 代表最後一個node, 等最後一個node接回前一個, return 此node, 結束遞迴
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        temp = None
        return self.dfs(head, temp)
        
    def dfs(self, head, temp):
        next_node = head.next
        head.next = temp
        if not next_node:
            return head
        return self.dfs(next_node, head)





....................................................................................................................................................................


#這一題不需要dummy head!
class Solution:
# @param {ListNode} head
# @return {ListNode}
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


# Recursion
class Solution:
# @param {ListNode} head
# @return {ListNode}
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)