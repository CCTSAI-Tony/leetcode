'''
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

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

class Solution:
    def insertionSortList(self, head):
        p = dummy = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val: #就是新value比cur大時, 前進一步!     這邊不能用while 因為val 需要一直更新
                cur = cur.next
                continue
            if p.next.val > val: #如果w新value 比指針下一個小 poiner就要刷新為了找尋新value位置
                p = dummy #refresh p
            while p.next.val < val:
                p = p.next
            new = cur.next # new: value 比cur 小 ->準備拿到前面
            cur.next = new.next #把new 拿走
            new.next = p.next
            p.next = new
        return dummy.next

Of course, the solution is still O(n^2) in the worst case, but it can be faster than most implements under given test cases.

Two key points are: 
(1) a quick check see if the new value is already the largest
(2) only refresh the search pointer p when the target is before it, in other words smaller.













