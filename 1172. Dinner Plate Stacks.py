'''
You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.

Implement the DinnerPlates class:

DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks.
void push(int val) pushes the given positive integer val into the leftmost stack with size less than capacity.
int pop() returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all stacks are empty.
int popAtStack(int index) returns the value at the top of the stack with the given index and removes it from that stack, 
and returns -1 if the stack with that given index is empty.
Example:

Input: 
["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
Output: 
[null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

Explanation: 
DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // The stacks are now:  2  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 2.  The stacks are now:     4
                                                       1  3  5
                                                       ﹈ ﹈ ﹈
D.push(20);        // The stacks are now: 20  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.push(21);        // The stacks are now: 20  4 21
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
                                                        1  3  5
                                                        ﹈ ﹈ ﹈
D.popAtStack(2);   // Returns 21.  The stacks are now:     4
                                                        1  3  5
                                                        ﹈ ﹈ ﹈ 
D.pop()            // Returns 5.  The stacks are now:      4
                                                        1  3 
                                                        ﹈ ﹈  
D.pop()            // Returns 4.  The stacks are now:   1  3 
                                                        ﹈ ﹈   
D.pop()            // Returns 3.  The stacks are now:   1 
                                                        ﹈   
D.pop()            // Returns 1.  There are no stacks.
D.pop()            // Returns -1.  There are still no stacks.
 

Constraints:

1 <= capacity <= 20000
1 <= val <= 20000
0 <= index <= 100000
At most 200000 calls will be made to push, pop, and popAtStack.
'''

# Use a heap to record all the popAtStack- index. Insert at these locations first. 
# If the heap is empty, (that means all the stacks except the last one are full) then insert at the end of the stacks.

# time complexity push O(logn), pop O(n), popAtStack O(logn)
# 思路: 利用list 來存所有的stacks, 建立self.empty heap 來存儲被 popAtStack 的stack's index, 之後push item 優先push至這些non-full stack
# 當pop self.empty 發現pop出來的index >= self.queue 代表self.empty 裡面的index對應的stack都被pop掉了, update self.empty => []
# 空 self.empty 只能代表除了rightmost stack外 其餘stack都是full
# popAtStack 某個stack 就heappush 該stack index to self.empty, 當該stack 變empty 就不能 popAtStack 該stack,
# 利用heap的結構, 重複元素出現在self.empty 代表該stack 有對應的空缺
# 注意, self.queue 中間的index 可以有empty stack存在

import heapq
class DinnerPlates:

    def __init__(self, capacity: int):
        self.queue = [] #store stacks
        self.c = capacity
        self.emp = [] #non-full stacks, if the same index appears twice, that means it has two empty positions in this stack.

    def push(self, val: int) -> None:
        if self.emp: # 中間有non-full stack
            l = heapq.heappop(self.emp) #leftmost nonfull stack
            if l < len(self.queue): 
                self.queue[l] += [val]
                return
            else: #in some cases, the pop is called too many times, and the queue is shorter than or equal to the index- means there is no empty stack, update empty 
                self.emp = [] #此時empty 只能代表除了最後一個stack以外都是full的
        if len(self.queue)>0 and len(self.queue[-1]) < self.c: #把它塞進最後一個stack
            self.queue[-1] += [val]
            return
        self.queue += [[val]] #連最後一個stack都滿了, 只好新增stack
        
#若pop完rightmost non-empty stack 變成empty stack, 該rightmost空stack還是留在self.queue裡
    def pop(self) -> int:
        while len(self.queue) > 0 and not self.queue[-1]: #去除rightmost 空stack 直到遇到non empty stack
            self.queue.pop()
        if self.queue:
            res = self.queue[-1][-1]
            self.queue[-1].pop()
            return res
        return -1

#每pop指定index 的 stack, push 該index to empty heap, 此階段若pop完指定index 的stack 導致stack變empty, 此空empty 依舊在self.queue裡
    def popAtStack(self, index: int) -> int: 
        if index < len(self.queue) and len(self.queue[index]) > 0:
            res = self.queue[index][-1]
            self.queue[index].pop()
            heapq.heappush(self.emp,index)
            return res
        return -1





#自己重寫, 刷題用這個, time complexity push O(logn), pop O(n), popAtStack O(logn)
import heapq
class DinnerPlates:

    def __init__(self, capacity: int):
        self.queue = []
        self.empty = []
        self.c = capacity
        

    def push(self, val: int) -> None:
        if self.empty:
            i = heapq.heappop(self.empty)
            if i < len(self.queue):
                self.queue[i] += [val]
                return
            else:
                self.empty = [] #其實不用清空也可以
        if self.queue and len(self.queue[-1]) < self.c:
            self.queue[-1] += [val]
            return
        self.queue.append([val])

    def pop(self) -> int:
        while self.queue and not self.queue[-1]:
            self.queue.pop()
        if self.queue:
            res = self.queue[-1].pop()
            return res
        return -1
        

    def popAtStack(self, index: int) -> int:
        if index < len(self.queue) and self.queue[index]:
            res = self.queue[index].pop()
            heapq.heappush(self.empty, index)
            return res
        return -1
























