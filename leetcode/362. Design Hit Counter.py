# Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

# Your system should accept a timestamp parameter (in seconds granularity), 
# and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). 
# Several hits may arrive roughly at the same time.

# Implement the HitCounter class:

# HitCounter() Initializes the object of the hit counter system.
# void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
# int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
 

# Example 1:

# Input
# ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
# [[], [1], [2], [3], [4], [300], [300], [301]]
# Output
# [null, null, null, null, 3, null, 4, 3]

# Explanation
# HitCounter hitCounter = new HitCounter();
# hitCounter.hit(1);       // hit at timestamp 1.
# hitCounter.hit(2);       // hit at timestamp 2.
# hitCounter.hit(3);       // hit at timestamp 3.
# hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
# hitCounter.hit(300);     // hit at timestamp 300.
# hitCounter.getHits(300); // get hits at timestamp 300, return 4.
# hitCounter.getHits(301); // get hits at timestamp 301, return 3.
 

# Constraints:

# 1 <= timestamp <= 2 * 109
# All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
# At most 300 calls will be made to hit and getHits.
 

# Follow up: What if the number of hits per second could be huge? Does your design scale?




# Deque Based Solution

# Use deque as container. Deque stores the value of the timestamp.
# hit: append the timestamp to the deque. O(1)
# get_hit: O(N). During get_hit, pop out all elements from the left of the queue which do not serve any purpose and are stale.Return the length of the deque.
# How do we find the elenments which are stale? Condition we want to use:* timestamp-t >= 300*
# Example: timestamp = 301 and t = 1. Valid Range: [1 to 300], [2 to 301], [3,303]. So 301-1 >= 300. Hence 1 should be popped since it doesnt belong to range 2 to 301.
# Poor scalability of the solution since we store all timestamps.

# 刷題用這個, hit: O(1). get_hit: O(n)
# 思路: 使用deque 來存timestamp
from collections import deque
class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = deque()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.counter.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.counter and timestamp -self.counter[0] >= 300:
            self.counter.popleft()
        return len(self.counter)


# 重寫第二次
from collections import deque
class HitCounter:

    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.queue and timestamp - self.queue[0] >= 300:
            self.queue.popleft()
        return len(self.queue)


# Optimized and Scalable Solution

# The third solution creates an array of 300 elements. Every element of the array comprises of [frequency, timestamp].
# Timestamp 1 maps to index 0. Timestamp 100 maps to index 99.
# Use modulo mathematics to update it. hit: O(1). get_hit: O(300). This solution will scale perfectly!

# follow up 刷題用這個, hit: O(1). get_hit: O(300)
# 思路: 使用modulo 來固定儲存hit 位置
class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = [[0,i+1] for i in range(300)]
        return

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        # ts = 301 means (301-1)%300
        idx = int((timestamp - 1)%300)
        if self.counter[idx][1] == timestamp:
            self.counter[idx][0] += 1
        else:
            self.counter[idx][0] = 1   # reset         
            self.counter[idx][1] = timestamp   # set a new timestamp         

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        cnt = 0
        for x in self.counter:
            c,t = x[0],x[1]
            if timestamp - t < 300:
                cnt += c
        return cnt

# 重寫第二次, hit: O(1). get_hit: O(300)
class HitCounter:

    def __init__(self):
        self.count = [[0, i+1] for i in range(300)]
        

    def hit(self, timestamp: int) -> None:
        idx = (timestamp - 1) % 300
        if self.count[idx][1] == timestamp:
            self.count[idx][0] += 1
        else:
            self.count[idx][0] = 1
            self.count[idx][1] = timestamp
        

    def getHits(self, timestamp: int) -> int:
        counts = 0
        for x in self.count:
            count, time = x[0], x[1]
            if timestamp - time < 300:
                counts += count
        return counts
