'''
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; 
There are 3 nodes before the intersected node in B.
 

Example 2:


Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. 
There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 

Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. 
Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        curA,curB = headA,headB
        lenA,lenB = 0,0
        while curA is not None: #caculate list length
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next
        curA,curB = headA,headB #back to origin
        if lenA > lenB:
            for i in range(lenA-lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB-lenA):
                curB = curB.next
        while curB != curA:
            curB = curB.next
            curA = curA.next
        return curA #if no intersection, till the end just return None

'''
The solution is straightforward: 
maintaining two pointers in the lists under the constraint that both lists have the same number of nodes starting from the pointers. 
We need to calculate the length of each list though. So O(N) for time and O(1) for space.

'''


#  自己重寫, time complexity O(n), space complexity O(1)
#  思路: 先計算headA, headB 的長度, 讓長的一邊先跑多餘的點, 使兩條listnode在同樣起跑點, 之後同步往後走,每走一步邊check是否站在同一個node, 是就回報該node
#  直到兩條同時進入null, return None, 兩條無相交, 額外技巧, dummy head 當作 reference 點
#  兩條若有相交, 相交點之後的路線一定都是一樣的, 也就是說兩條相同長度起始點開始的每個node才有可能成為相交點, 長度比較長的線 起始點以前的node都是不可能成為相交點的
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        curA, curB = headA, headB
        while curA:
            lenA += 1
            curA = curA.next
        
        while curB:
            lenB += 1
            curB = curB.next
        
        curA, curB = headA, headB
        if lenA > lenB:
            for _ in range(lenA-lenB):
                curA = curA.next
        elif lenB > lenA:
            for _ in range(lenB-lenA):
                curB = curB.next
        while curA and curB:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None



#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dummy1 = cur1 = ListNode(0)
        dummy2 = cur2 = ListNode(0)
        dummy1.next = headA
        dummy2.next = headB
        lenA, lenB = 0, 0
        while cur1.next:
            lenA += 1
            cur1 = cur1.next
        while cur2.next:
            lenB += 1
            cur2 = cur2.next
        cur1, cur2 = dummy1, dummy2
        diff = abs(lenA - lenB)
        if lenA > lenB:
            for _ in range(diff):
                cur1 = cur1.next
        elif lenA < lenB:
            for _ in range(diff):
                cur2 = cur2.next
        while cur1:
            cur1 = cur1.next
            cur2 = cur2.next
            if cur1 == cur2:
                return cur1
        return None












