# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

#自己重寫 time complexity O(m+n)
#思路: 使用dummy node 與 cur 指針 來連結 排序的node
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
            
        cur.next = (l1 or l2)
        return dummy.next




class Solution:  
    def mergeTwoLists1(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:  #包含 l1>l2 l1=l2   若改為 if l1.val > l2.val:  若等於發生 cur = cur.next 會發生nonetype 無next attribute 的error
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2  #if l1 or l2 其中一個為 None
        return dummy.next

        # recursively 
class Solution:     
    def mergeTwoLists2(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)  #遞迴用return 回報給上層問題
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        
