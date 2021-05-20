'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 跟龜兔賽跑那題一起服用 leetcode 141, 142
# 自己重寫, time complexity O(nlogn), space complexity O(1)
# 思路: 就是merge sort, 重點在於如何平分ListNode, 這裡提出兩個指針, slow, fast, 一開始他們站在head, head.next, 分別代表 1, 2 node 位置
# slow 動一格, fast 動兩格, => 1,2 => 2,4 => 3,6 => 4,8 => 5, 10 可以看出slow.next 就是平分的另一半, 之後slow.next = None 就能切分完畢, !!值得記起來這種指針位置
# 之後就是merge 一樣利用多重指針 ex: dummy node 來執行排序
# time complexity 分析: 分割每層O(n), merge 一樣每層O(n), 一共有O(logn) 層
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:  #為了一開始head = [] 
            return None
        if not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)
    
    def merge(self, l, r):
        if l.val > r.val:
            l, r = r, l
        head = cur = l
        l = l.next
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
        return head

# slow, fast = head, head.next 這邊可以改成 slow, fast = head, head.next.next 但複雜度會增加, 因為不是完美平分
# 但不能 slow, fast = (head, head) or (head.next, head.next.next) => 1->2  脫離while loop後, l 依舊 1->2 => 造成無限循環, 這點需要注意

#刷題用這個, 重寫第二次, time complexity O(nlogn), space complexity O(1)
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)
    
    def merge(self, l, r):
        dummy = cur = ListNode(0)
        while l and r:
            if l.val > r.val:
                cur.next = r
                cur = cur.next
                r = r.next
            else:
                cur.next = l
                cur = cur.next
                l = l.next
        cur.next = l or r
        return dummy.next

#重寫第三次, time complexity O(nlogn), space complexity O(1)
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)
    
    def merge(self, l, r):
        dummy = cur = ListNode()
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return dummy.next





#time complexity O(nlogn), space complexity O(1)
#指針遍歷的切分time complexity = merge time complexity = O(n), 因此total time complexity 一樣是 O(nlogn)
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        return self.helper(head)
    
    def helper(self, head):
        if not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        nxt = slow.next
        slow.next = None
        left = self.helper(head)
        right = self.helper(nxt)
        return self.merge(left, right)
    
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



# merge sort, recursively 
class Solution:
    def sortList(self, head):
        if not head or not head.next: #例如 second = None 還有 head 只剩一個
            return head
        # divide list into two parts
        fast, slow = head.next, head #slow 走一步 fast 走兩步
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        # cut down the first part
        slow.next = None
        l = self.sortList(head) #分解左
        r = self.sortList(second) #分解右
        return self.merge(l, r)

    def merge(self, l, r):
        if l.val > r.val:
            l, r = r, l #替換位置
        # get the return node "head"
        head = pre = l
        l = l.next #l 先比pre走一步
        while l and r:
            if l.val < r.val:
                pre.next = l
                l = l.next
            else:
                pre.next = r
                r = r.next
            pre = pre.next #pre也會跟著移動
        # l and r at least one is None
        pre.next = l or r #完成pre線
        return head

       
       #另一版本merge 差在 l.val > r.val 的解釋
       # merge in-place without dummy node        
    def merge(self, l, r):
        if l.val > r.val:
            l, r = r, l
        # get the return node "head"
        head = pre = l
        l = l.next
        while l and r:
            if l.val < r.val:
                l = l.next
            else:
                nxt = pre.next
                pre.next = r
                tmp = r.next
                r.next = nxt
                r = tmp
            pre = pre.next
        # l and r at least one is None
        pre.next = l or r
        return head




'''
a = 1 or 0
a
1
'''











