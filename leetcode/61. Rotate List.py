'''
    Given a linked list, rotate the list to the right by k places, where k is non-negative.

    Example 1:

    Input: 1->2->3->4->5->NULL, k = 2
    Output: 4->5->1->2->3->NULL
    Explanation:
    rotate 1 steps to the right: 5->1->2->3->4->NULL
    rotate 2 steps to the right: 4->5->1->2->3->NULL
    Example 2:

    Input: 0->1->2->NULL, k = 4
    Output: 2->0->1->NULL
    Explanation:
    rotate 1 steps to the right: 2->0->1->NULL
    rotate 2 steps to the right: 1->2->0->NULL
    rotate 3 steps to the right: 0->1->2->NULL
    rotate 4 steps to the right: 2->0->1->NULL


    range(l-k-1)
    Imagine a list from Node 1 to N.
    You want a new head, which should point to Node N-k+1(Assuming k is less than N, other wise k = k%N).
    Here OP is trying to find the q which is the node right before the new head, which will be the new tail.
    So q should eventually point to Node N-k, how many loops to move from Node 1 to Node N-k?
    Answer is N-k-1 loop.
    In the end, q.next is the new head, and then set q.next to None to break loop.
    Hope it helps.

'''

# 刷題用這個, time complexity O(n), space complexity O(1)
# 思路: 頭尾先串連, 再從尾端往回算k ％ l 步, 那個node 便是 rotate k 步後最尾端的node => for _ in range(l-k-1):
class Solution:
    def rotateRight(self, head, k):
        if not head:
            return None
        p=q=head
        l=1
        while p.next:
            p=p.next
            l+=1
        p.next=head #頭尾接起來
        k%=l #k= k%l
        for _ in range(l-k-1):
            q=q.next
        ans=q.next  
        q.next=None #斷掉
        return ans      

# 重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        p = q = head
        l = 1
        while p.next:
            p = p.next
            l += 1
        p.next = q
        k %= l
        for _ in range(l-k-1):
            q = q.next
        ans = q.next
        q.next = None
        return ans