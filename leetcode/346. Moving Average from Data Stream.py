'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''


#刷題用這個, time complexity O(1), space complexity O(n)
#思路: 建立環狀queue 初始皆為0, tail = (head + 1) mod size, In other words, the tail element is right next to the head element. 
# Once we move the head forward, we would overwrite the previous tail element.
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        # number of elements seen so far
        self.count = 0
        

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        # move on to the next head
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)


#重寫第二次, time complexity O(1), space complexity O(n)
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = [0] * size
        self.count = 0
        self.head = 0
        self.curSum = 0
        self.size = size
        

    def next(self, val: int) -> float:
        self.count += 1
        tail = (self.head + 1) % self.size
        self.curSum = self.curSum - self.queue[tail] + val
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.curSum / min(self.count, self.size)


#自己想的, time complexity O(1), space complexity O(n)
#思路:two pointers
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.l = 0
        self.r = 0
        self.curSum = 0
        self.list = []
        

    def next(self, val: int) -> float:
        self.list.append(val)
        self.curSum += val
        self.r += 1
        if self.r - self.l > self.size:
            self.curSum -= self.list[self.l]
            self.l += 1
        return self.curSum / len(self.list) if len(self.list) < self.size else self.curSum / self.size