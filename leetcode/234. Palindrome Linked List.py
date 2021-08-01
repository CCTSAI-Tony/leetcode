'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#刷題用這個, time complexity O(n), space complexity O(1)
#思路: 利用快慢指針來反轉第二半, 之後再驗證此兩半是否一樣
class Solution:
    def isPalindrome(self, head):
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next #jump two steps
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow #generate node line represent second half(reversed)
            slow = nxt
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True

#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        temp = None
        while slow:
            nxt = slow.next
            slow.next = temp
            temp = slow
            slow = nxt
        while temp:
            if temp.val != head.val:
                return False
            temp = temp.next
            head = head.next
        return True


1->2->2->1
hfs

h  s  f

h    s      f

2->1->none ---->  1->2->none