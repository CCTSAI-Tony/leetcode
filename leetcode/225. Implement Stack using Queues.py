'''
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), 
as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

Follow-up: Can you implement the stack such that each operation is amortized O(1) time complexity? In other words, 
performing n operations will take overall O(n) time even if one of those operations may take longer.
'''

#刷題用這個, 使用deque 來實現stack, push item 至最前面
#思路: extend() time complexity O(k), k: len(argument), push 一個item 上面放滿100個credit => amortized O(1) => 其去follow up 沒有答案
#time complexity: push O(k), pop O(1), top O(1), empty O(1)
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        

    def push(self, x: int) -> None: #這裡最關鍵
        """
        Push element x onto stack.
        """
        tmp = deque([x]) #to arrange [x] to be put on the front
        tmp.extend(self.queue) 
        self.queue = tmp #aassign it back to self.queue
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft() #have already put the top element to the left
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0


#重寫第二次
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        temp = deque([x])
        temp.extend(self.queue)
        self.queue = temp

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0



'''
extend(iterable) :- This function is used to add multiple values at the right end of deque. The argument passed is an iterable.

不过，下面的例子就可以看到，deque是通过extend方法初始化集合元素的，同时你可以通过extendleft将结合元素从“左边”加入到集合中：
import collections
d1=collections.deque()
d1.extend('abcdefg')
print 'extend:',d1
d1.append('h')
print 'append:',d1
# add to left
d2=collections.deque()
d2.extendleft(range(6))
print 'extendleft:',d2
d2.appendleft(6)
print 'appendleft:',d2

从输出的结果，我们可以看到，append默认从集合的右边增加数组元素，而另一个appendleft可以从集合的左边增加元素，输出结果如下：
extend: deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
append: deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
extendleft: deque([5, 4, 3, 2, 1, 0])
appendleft: deque([6, 5, 4, 3, 2, 1, 0])



from collections import deque
tmp = deque([1])
tmp
deque([1])
tmp.extend([2,3,4,5])
tmp
deque([1, 2, 3, 4, 5])

















'''



