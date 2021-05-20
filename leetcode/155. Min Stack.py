'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

# 刷題用這個, time complexity O(1), space complexity O(n)
# 思路: 存入tuple: (x, cur_min) 來記錄push x 元素後當下的最小值
class MinStack:

    def __init__(self):
        self.q = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        curMin = self.getMin() 
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin)) #append tuple 每次push都會更新curmin

    # @return nothing
    def pop(self):
        self.q.pop()


    # @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[- 1][0]


    # @return an integer
    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[- 1][1] #取top的元素

#重寫第二次, time complexity O(1), space complexity O(n)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        min_value = self.stack[-1][1] if self.stack else None
        if not self.stack or x < self.stack[-1][1]:
            min_value = x
        self.stack.append((x, min_value))
            
        
    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
