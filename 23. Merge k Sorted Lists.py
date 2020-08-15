'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''
# Python concise divide and conquer solution. time complexity O(M*lg(N)), Space complexity with recursion stack is O(lg(N))
# 思路: 利用分治法來合併lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return  # 等於 return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)//2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge(l, r)

    def merge(self, l, r):
        dummy = cur = ListNode(0)
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r  #其中有一為none
        return dummy.next

# What's the time and space complexity here?

# This seems to be performing a modified merge sort.
# So it iterates over the linked lists lg(N) times, making the time complexity O(M*lg(N)), 
# where M is the size of the merged linked list and N is the size of the lists argument.
# Space complexity with recursion stack is O(lg(N)), without recursion stack is O(1)

#這個解釋不錯
# the time complexity of your algorithm is o(nklogk), absolutely.
# assume the average length of lists is n, there are k lists.
# firstly, merge every two list need nk/2; in the next round, the length of list becomes 2n, the number of lists becomes k/2, 
# so the complexity is still nk/2. Keep such rounds until k == 1, that would be log(k) rounds. so the total complexity is nklog(k)