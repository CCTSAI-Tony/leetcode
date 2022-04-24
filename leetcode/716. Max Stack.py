'''
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:

MaxStack() Initializes the stack object.
void push(int x) Pushes element x onto the stack.
int pop() Removes the element on top of the stack and returns it.
int top() Gets the element on the top of the stack without removing it.
int peekMax() Retrieves the maximum element in the stack without removing it.
int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.
 

Example 1:

Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation
MaxStack stk = new MaxStack();
stk.push(5);   // [5] the top of the stack and the maximum number is 5.
stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, 5] the stack did not change.
stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [5, 1] the stack did not change.
stk.peekMax(); // return 5, [5, 1] the stack did not change.
stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
stk.top();     // return 5, [5] the stack did not change.
 

Constraints:

-107 <= x <= 107
At most 104 calls will be made to push, pop, top, peekMax, and popMax.
There will be at least one element in the stack when pop, top, peekMax, or popMax is called.
 

Follow up: Could you come up with a solution that supports O(1) for each top call and O(logn) for each other call? 
'''

# 刷題用這個
# 思路: Use doubly linked list + heap + dictionary to achieve O(logN) time complexity.
# The basic idea is to use the heap to find the max in O(logN) and do removal in O(1) with the help of dict and doubly linked list.
from collections import defaultdict
from heapq import heappush, heappop, heapify
class DoubleLinkedList:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.pre = None
	
class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.stack = DoubleLinkedList(float('-inf')) # init a dummy node
        self.last = self.stack                       # reference the stack tail
        self.heap = []
        self.hmap = defaultdict(list)
        

    def push(self, x: int) -> None:
        # O(logn)
        node = DoubleLinkedList(x)
        
        # update the tail
        self.last.next = node
        node.pre = self.last
        self.last = node
        
        # push -x to the min heap
        heappush(self.heap, -x)
        
        # append node the the map entry
        self.hmap[x].append(node)
        
    def pop(self) -> int:
        # O(1)
        # pop from the stack and remove from map
        num = self.last.val
        self.last = self.last.pre
        self.last.next = None
        
        self.hmap[num].pop()
        if not self.hmap[num]:
            del self.hmap[num]
        return num

    def top(self) -> int:
        # O(1)
        return self.last.val

    def peekMax(self) -> int:
        # O(logN)
        # during the pop(), we didn't remove the element from heap
        # So here is to remove the the poped elements from heap
        while -self.heap[0] not in self.hmap:
            heappop(self.heap)
        
        return -self.heap[0]

    def popMax(self) -> int:
        # O(logN)
        # get the top-most node from map
        num = self.peekMax()
        node = self.hmap[num].pop()
        if not self.hmap[num]:
            del self.hmap[num]
        
        # update the tail reference
        if node == self.last:
            self.last = self.last.pre
        
        # remove the node from stack
        if node.pre:
            node.pre.next = node.next
        if node.next:
            node.next.pre = node.pre
        return num

