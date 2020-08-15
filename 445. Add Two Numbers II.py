'''
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#自己想的 time complexity O(max(len(l1), len(l2))
#思路: 因為不能修改input LinkedList 所以只能walk through 取得兩條 linked list 的資訊
#兩條的值加起來,  做出一條nums3 link list, 並利用dummy head 來回報
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nums1 = 0
        nums2 = 0
        while l1:
            nums1 = nums1*10 + l1.val
            l1 = l1.next
        while l2:
            nums2 = nums2*10 + l2.val
            l2 = l2.next
        
        nums3 = nums1 + nums2
        dummy = cur = ListNode(0)
        for num in list(str(nums3)):
            newNode = ListNode(int(num))
            cur.next = newNode
            cur = cur.next
        return dummy.next
