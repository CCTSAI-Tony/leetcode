'''
Given a node from a Circular Linked List which is sorted in ascending order, 
write a function to insert a value insertVal into the list such that it remains a sorted circular list. 
The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. 
After the insertion, the circular list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single circular list and return the reference to that single node. 
Otherwise, you should return the original given node.

 

Example 1:


 
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements. 
You are given a reference to the node with value 3, and we need to insert 2 into the list. 
The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.



Example 2:

Input: head = [], insertVal = 1
Output: [1]
Explanation: The list is empty (given head is null). We create a new single circular list and return the reference to that single node.
Example 3:

Input: head = [1], insertVal = 0
Output: [1,0]
 

Constraints:

0 <= Number of Nodes <= 5 * 10^4
-10^6 <= Node.val <= 10^6
-10^6 <= insertVal <= 10^6
'''

#自己想的, time complexity O(n), space complexity O(1)
#思路: 使用dummy head, 此題有可能出現相同大小的node, 有兩種狀況可以插入node, 1. cur.next.val >= insertVal >= cur.val
#另一種狀況是insertVal >= 最大的list_val or insertVal <= 最小的list_val, 此時就要找到cur.val > cur.next.val的斷點 來插入我們的node
#當上面的狀況都不適用, 持續 cur = cur.next, 直到cur = dummy.next(走完一圈), 代表list所有node大小一樣, or single circular node 但!= insertVal
#此時當下找一個位置插入即可
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        dummy = cur = Node(0)
        dummy.next = head
        cur = cur.next
        while True:
            if cur.next.val >= insertVal >= cur.val:
                break
            elif cur.val > cur.next.val and (insertVal >= cur.val or insertVal <= cur.next.val):
                break
            cur = cur.next
            if cur == dummy.next: #當所有node大小一樣, or single circular node
                break
        temp = cur.next
        cur.next = Node(insertVal)
        cur.next.next = temp
        return dummy.next






