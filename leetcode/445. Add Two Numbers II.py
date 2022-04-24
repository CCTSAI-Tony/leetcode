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



#刷題用這個, time complexity O(n), space complexity O(1)
#思路: linkedlist reverse tacnic => 先同位置的數值加一起, reverse => 再進行進位處理 => reverse
#技巧: 等同reverse 2 次
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # find the length of both lists
        n1 = n2 = 0
        curr1, curr2 = l1, l2
        while curr1:
            curr1 = curr1.next 
            n1 += 1
        while curr2:
            curr2 = curr2.next 
            n2 += 1
            
        # parse both lists
        # and sum the corresponding positions 
        # without taking carry into account
        # 3->3->3 + 7->7 --> 3->10->10 --> 10->10->3
        curr1, curr2 = l1, l2
        head = None
        while n1 > 0 and n2 > 0:
            val = 0
            if n1 >= n2:
                val += curr1.val 
                curr1 = curr1.next 
                n1 -= 1
            if n1 < n2:
                val += curr2.val 
                curr2 = curr2.next
                n2 -= 1
                
            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

        # take the carry into account
        # to have all elements to be less than 10
        # 10->10->3 --> 0->1->4 --> 4->1->0
        curr1, head = head, None
        carry = 0
        while curr1:
            # current sum and carry
            val = (curr1.val + carry) % 10
            carry = (curr1.val + carry) // 10
            
            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

            # move to the next elements in the list
            curr1 = curr1.next
        
        # add the last carry
        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr

        return head


#重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = 0, 0
        cur1, cur2 = l1, l2
        while cur1:
            n1 += 1
            cur1 = cur1.next
        while cur2:
            n2 += 1
            cur2 = cur2.next
        cur1, cur2 = l1, l2
        temp = None
        while n1 and n2:
            val = 0
            if n1 > n2:
                val += cur1.val
                cur1 = cur1.next
                n1 -= 1
            elif n1 < n2:
                val += cur2.val
                cur2 = cur2.next
                n2 -= 1
            else:
                val += (cur1.val + cur2.val)
                cur1 = cur1.next
                cur2 = cur2.next
                n1 -= 1
                n2 -= 1
            cur = ListNode(val)
            cur.next = temp
            temp = cur
        temp = None
        carry = 0
        while cur:
            val = (cur.val + carry) % 10
            carry = (cur.val + carry) // 10
            head = ListNode(val)
            head.next = temp
            temp = head
            cur = cur.next
        if carry:
            head = ListNode(carry)
            head.next = temp
        return head


#重寫第三次, time complexity O(n), space complexity O(1)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = 0, 0
        cur1, cur2 = l1, l2
        while cur1:
            cur1 = cur1.next
            n1 += 1
        while cur2:
            cur2 = cur2.next
            n2 += 1
        temp = None
        cur1, cur2 = l1, l2
        while n1 and n2:
            val = 0
            if n1 > n2:
                val += cur1.val
                cur1 = cur1.next
                n1 -= 1
            elif n1 < n2:
                val += cur2.val
                cur2 = cur2.next
                n2 -= 1
            else:
                val += (cur1.val + cur2.val)
                cur1 = cur1.next
                cur2 = cur2.next
                n1 -= 1
                n2 -= 1
            cur = ListNode(val)
            cur.next = temp
            temp = cur
        temp = None
        carry = 0
        while cur:
            val = (cur.val + carry) % 10
            carry = (cur.val + carry) // 10
            head = ListNode(val)
            head.next = temp
            temp = head
            cur = cur.next
        if carry:
            head = ListNode(carry)
            head.next = temp
        return head

#重寫第四次, time complexity O(n), space complexity O(1)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = 0, 0
        cur1, cur2 = l1, l2
        while cur1:
            n1 += 1
            cur1 = cur1.next
        while cur2:
            n2 += 1
            cur2 = cur2.next
        cur1, cur2 = l1, l2
        prev = None
        while n1 and n2:
            val = 0
            if n1 > n2:
                val += cur1.val
                cur1 = cur1.next
                n1 -= 1
            elif n2 > n1:
                val += cur2.val
                cur2 = cur2.next
                n2 -= 1
            else:
                val += cur1.val + cur2.val
                cur1 = cur1.next
                cur2 = cur2.next
                n1 -= 1
                n2 -= 1
            node = ListNode(val)
            node.next = prev
            prev = node
        cur = prev
        carry = 0
        prev = None
        while cur:
            carry, val = (cur.val + carry) // 10, (cur.val + carry) % 10
            node = ListNode(val)
            node.next = prev
            prev = node
            cur = cur.next
        if carry:
            node = ListNode(carry)
            node.next = prev
            prev = node
        return prev




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













