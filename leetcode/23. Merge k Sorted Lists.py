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
# Python concise divide and conquer solution. time complexity O(MN*lg(N)), Space complexity with recursion stack is O(lg(N))
# where M is the size of the merged linked(總字數) list and N is the size of the lists argument.
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

#重寫第二次, time complexity O(mnlogn), space complexity O(logn), m:len(sorted_list), n: len(lists)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r):
        dummy = cur = ListNode()
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
                cur = cur.next
            else:
                cur.next = r
                r = r.next
                cur = cur.next
        cur.next = l or r
        return dummy.next


#重寫第三次, time complexity O(mnlogn), space complexity O(log(n)), m:len(sorted_list), n: len(lists), mn: total elements
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        return self.helper(lists, 0, len(lists) - 1)
    
    def helper(self, lists, left, right):
        if left > right:
            return None
        elif left == right:
            return lists[left]
        else:
            mid = left + (right - left) // 2
            l = self.helper(lists, left, mid)
            r = self.helper(lists, mid + 1, right)
            return self.merge(l, r)
        
    def merge(self, l, r):
        dummy = cur = ListNode()
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
                cur = cur.next
            else:
                cur.next = r
                r = r.next
                cur = cur.next
        cur.next = l or r
        return dummy.next

#重寫第四次, time complexity O(mnlogn), space complexity O(logn)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        n = len(lists)
        return self.helper(0, n - 1, lists)
    
    def helper(self, l, r, lists):
        if l > r:
            return None
        if l == r:
            return lists[l]
        m = l + (r - l) // 2
        left = self.helper(l, m, lists)
        right = self.helper(m+1, r, lists)
        return self.merge(left, right)
    
    def merge(self, left, right):
        dummy = cur = ListNode(0)
        while left and right:
            if left.val <= right.val:
                cur.next = left
                cur = cur.next
                left = left.next
            elif right.val < left.val:
                cur.next = right
                cur = cur.next
                right = right.next
        cur.next = left or right
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