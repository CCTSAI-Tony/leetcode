'''
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
'''


# For the interview, is it better to use the constructor to construct the entire flattened list first, or no?

# I noticed simple approach is to just flatten entire list first in constructor, 
# since this makes next and hasNext O(1), even though constructor is O(N). Would an interviewer be ok with this approach, 
# or would he want to actually dynamically maintain some kind of stack so that it always has the next integer?

# Definitely no. An iterator should never copy the input data structure.
# see my post for a comparison between different approaches.


# It's not necessary to pre-process the entire list and create a flatten copy of it , because the idea is to implement an iterator, 
# this means you need to process and return the data when the user asks for them. Imagine the user instanciates the Iterator class, 
# but he never asks if the iterator has some data (hasNext()), another situation is when you have 10 elements, but the user just gets 2 elements. 
# That's the reason I think is better to return and process on demand. This is my solution.


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

#time complexity: next: O(1) and hasNext: O(N) 
#思路: 手動建立__listEmpty, __isComplete, 利用原生method isInteger 來確認current element 是否為integer, 
#若不是, 代表是list, 此時利用 self.__lists 先暫存下一個元素與index, 因為要準備原生method getList 進入nested list, 進入前 self.__position 歸0
#若nested complete, 則在從self.__lists pop 出 上層list下一個元素與index 繼續flatten
#next 是回報integer, hasNext 則是回報self.__nestedList下一個元素是否是數字, 有則return True, 若是nested list, 則進入nested list
#若nested list 裡面有數字則一樣return True, 若裡面沒數字or complete, 則確認self.__lists 裡面是否還有元素, 有則從self.__lists pop出上層list的接續點
#並重新呼叫hasNext, 確認接續點之後是否有integer
#直到self.__isComplete() and self.__listEmpty() 代表之後已無數字, hasNext return False
#注意: nested list 有可能是空list
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.__nestedList = nestedList #self.__ => privite field
        self.__position = 0
        self.__lists = []
    
    def next(self) -> int:  #先呼叫hasNext再next
        integer = self.__nestedList[self.__position].getInteger()
        self.__position += 1
        return integer
        
    
    def hasNext(self) -> bool:    
        while not self.__isComplete():  #self.__nestedList 還沒out of list時
            currNode = self.__nestedList[self.__position]
            
            if currNode.isInteger():
                return True
            else:
                self.__position += 1  #先往下一個
                self.__lists.append((self.__nestedList, self.__position))  #紀錄當層下一個起始位置 by tuple
                self.__position = 0  #position 歸0, 為了進入list中的list做準備
                self.__nestedList = currNode.getList()  #進入nestedinteger 裡的list
            
        if self.__isComplete() and not self.__listEmpty():
            self.__nestedList, self.__position = self.__lists.pop() #回到上一層nested list的紀錄位置 tuple unpacking, 注意這裡用pop(), pop出最後一個item, 似dfs
            return self.hasNext()  #再重新呼叫self.hasNext(), 若 self.hasNext() == True, return True, dfs概念
                    
        return False  
    
    def __listEmpty(self) -> bool:
        return len(self.__lists) == 0
    
    def __isComplete(self) -> bool:
        return self.__position >= len(self.__nestedList)  #base 0 index


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


#自己重寫!
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.__pos = 0
        self.__nestedList = nestedList
        self.__list = []
        
    
    def next(self) -> int:
        integer = self.__nestedList[self.__pos].getInteger()
        self.__pos += 1
        return integer
    
    def hasNext(self) -> bool:
        while not self.isCompleted():
            curr = self.__nestedList[self.__pos]
            if curr.isInteger():
                return True
            self.__pos += 1
            self.__list.append((self.__nestedList, self.__pos))
            self.__pos = 0
            self.__nestedList = curr.getList()
        if self.isCompleted() and not self.isListEmpty():
            self.__nestedList, self.__pos = self.__list.pop()
            return self.hasNext()
        return False
            
        
    def isCompleted(self):
        return self.__pos >= len(self.__nestedList)
    
    def isListEmpty(self):
        return self.__list == []








































