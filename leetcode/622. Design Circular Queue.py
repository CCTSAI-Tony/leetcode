'''
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO 
(First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, 
we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.
 

Example:

MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false, the queue is full
circularQueue.Rear();  // return 3
circularQueue.isFull();  // return true
circularQueue.deQueue();  // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();  // return 4
 
Note:

All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Queue library.
'''

# The idea is to use a single list of fixed size k and keep the references to front and rear indices in the array. 
# Since we don't deal with any of the memory allocation/deletion/pointer manipulation, this solution is very fast IMO


# 思路: 雙指針!! 此題重點在於rear, front 的 指針 要circular 移動, 利用list, 並設定rear, front 兩個指針, 隨著enque, deque 來移動指針
# deque, front 往後移動, 因爲first in first out,接下來s enque, rear 往後移動, => 可能出現這樣的情況 [rear,null,null,front,2,3]
# zero based index % self.max_size => 還是符合zero based index 又完成circular
class MyCircularQueue:
    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.front = 0
        self.rear = -1  #故意設計rear指針 比 front指針往前一格, 想像enqueue後, queue只有一個值, rear 與 front 都指同一個元素
        self.queue = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.max_size  #circle => % self.max_size, self.rear + 1, 新加元素, trick!! 一開始 -1+1 = 0
            self.queue[self.rear] = value
            self.size += 1
            return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.front = (self.front+1) % self.max_size   #circle => % self.max_size, self.front + 1, 新加元素
            self.size -= 1
            return True
        

    def Front(self) -> int:
        return self.queue[self.front] if self.size else -1
        

    def Rear(self) -> int:
        return self.queue[self.rear] if self.size else -1
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.max_size



#自己重寫, 注意題目要求!
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        
        self.size = 0
        self.max_size = k
        self.front = 0
        self.rear = -1
        self.queue = [0]*k
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value
        self.size += 1
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.max_size





















