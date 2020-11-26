'''
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- 
it essentially peek() at the element that will be returned by the next call to next().

Example:

Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2. 
You call next() the final time and it returns 3, the last element. 
Calling hasNext() after that should return false.
Follow up: How would you extend your design to be generic and work with all types, not just integer?
'''
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        self.tep = None
        self.it = iterator

    def peek(self):
        if not self.tep: 
        	self.tep = self.it.next() #當執行這句, self.it.next(), self.it 已經迭代到下一個了
        return self.tep

    def next(self):
        if self.tep:
            res = self.tep
            self.tep = None
            return res
        else:
            return self.it.next()
        
    def hasNext(self):
        return self.it.hasNext() or self.tep != None #self.it.hasNext() uses iterartor hasnext method, 注意!! or self.tep != None 不能省略
# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums)) ,inherit from Iterator(nums)
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

#刷題用這個
#思路: 利用iterator interface 來做題, 若cur element 往下沒有element, hasNext => return None, call next() => get cur element, 但self.cur 指針往下走
class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        self.cur = self.iter.next() if self.iter.hasNext() else None

    def peek(self):
        return self.cur
        
    def next(self):
        tmp = self.cur #tmp 紀錄目前self.cur 的值
        self.cur = self.iter.next() if self.iter.hasNext() else None #self.cur 往下一個
        return tmp

    def hasNext(self):
        return self.cur != None


#重寫第二次, time complexity O(1)
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.cur = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.cur

    def next(self):
        """
        :rtype: int
        """
        temp = self.cur
        self.cur = self.iterator.next() if self.iterator.hasNext() else None
        return temp
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur != None
