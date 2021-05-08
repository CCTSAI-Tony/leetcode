# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 自己重寫 time complexity O(n)
# 思路: 此題就是相加兩個list, 首先為個位數相加, 再來十位數, 但別忘了進位到下一round, 最後若有進位要手動加回
# 額外技巧, dummyhead and divmod


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = cur = ListNode(0)
        while l1 or l2:
            temp = 0
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            temp += carry
            carry, value = divmod(temp, 10)
            cur.next = ListNode(value)
            cur = cur.next
        if carry:  # 最後若有進位別忘了加
            cur.next = ListNode(carry)
        return dummy.next


# 自己重寫, time complexity O(max(m, n)), space complexity O(1)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = cur = ListNode()
        while l1 or l2 or carry:
            if l1:
                temp1 = l1.val
                l1 = l1.next
            else:
                temp1 = 0
            if l2:
                temp2 = l2.val
                l2 = l2.next
            else:
                temp2 = 0
            carry, num = divmod(temp1 + temp2 + carry, 10)
            cur.next = ListNode(num)
            cur = cur.next

        return dummy.next

# 重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode()
        carry = 0
        while l1 or l2 or carry:
            temp1, temp2 = 0, 0
            if l1:
                temp1 = l1.val
                l1 = l1.next
            if l2:
                temp2 = l2.val
                l2 = l2.next
            carry, remain = divmod(temp1 + temp2 + carry, 10)
            cur.next = ListNode(remain)
            cur = cur.next
        return dummy.next

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        # dummy head
        head = curr = ListNode(0)  # 重要 dummy head, 剛開始head, curr 起點一樣
        while l1 or l2:
            val = carry  # 紀錄進位
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            curr.next = ListNode(val % 10)
            curr = curr.next  # 增加節點
            carry = val // 10
        if carry > 0:  # 針對最後進位
            curr.next = ListNode(carry)
        return head.next  # 跳過dummy head節點 return 之後一條數列

        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
a+1 vs a+=1 在於a+1單純只是當下變數加一  a+=1 則是重新定義這個變數 變成變數+1
最大差別在於a有沒有被重新定義
'''
