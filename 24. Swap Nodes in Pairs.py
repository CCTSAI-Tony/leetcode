class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: return head  # 沒有 or 只有一個node
        dummy = ListNode(0)
        dummy.next = head # 接起來
        cur = dummy
        
        while cur.next and cur.next.next:
            first = cur.next
            sec = cur.next.next
            cur.next = sec
            first.next = sec.next
            sec.next = first
            cur = cur.next.next
        return dummy.next       