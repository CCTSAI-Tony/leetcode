'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), 
as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''


Approach 2: push O(1), pop amortized O(1)

# 刷題用這個, push O(1), pop O(1)
# 思路: 利用兩個stack 來做題, self.s2 儲存較前的元素, self.s1 儲存後加的元素, 要pop之前, 若self.s2 有元素, 先pop s2, 若沒有, 再把後加的元素從s1 到 s2
# 每個元素都先加一個credit -> 來提供轉移至s2的花費 => amortized
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):  #此題關鍵
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]        

    def empty(self):
        return not self.s1 and not self.s2

#重寫第二次, time complexity: push O(1), pop O(1)
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.s2:
            return self.s2.pop()
        self.peek()
        return self.s2.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s2:
            return self.s2[-1]
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop())
        return self.s2[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.s1 and not self.s2




# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()