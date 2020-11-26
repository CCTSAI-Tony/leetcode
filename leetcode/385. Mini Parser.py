'''
Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

String is non-empty.
String does not contain white spaces.
String contains only digits 0-9, [, - ,, ].
Example 1:

Given s = "324",

You should return a NestedInteger object which contains a single integer 324.
Example 2:

Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
'''

題目解釋

# No offense but this problem seriously needs some more explanation and grammar check. I want to add a few clarification as follows so it saves you some time:

# the add() method adds a NestedInteger object to the caller. e.g.:
# outer = NestedInteger() # []
# nested = NestedInteger(5)
# outer2 = nested
# outer.add(nested) # outer is now [5]
# outer2.add(outer) # outer2 is now [5, [5]]
# "Set this NestedInteger to hold a nested list and adds a nested integer elem to it." cannot be more vague.

# '-' means negative. It's not a delimiter.

# For test cases like "324" you need to return something like NestedInteger(324) not "[324]".

# A list cannot have multiple consecutive integers. e.g. "321, 231" is invalid. I guess it's for difficulty purposes.

# I totally agree with you. This question puzzled me for a long time until I referred to discussion today. I always thought for input as "[123,[345],456]". 
# Actually, this question is more like a ListNode or a Trie as it can be "[Integer, NestedInteger]" only. 
# Each NestedInteger only have a valid Integer value and a NestedInteger (node).




# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it. ex: [123]
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


# My stack solution, as many people have similar solutions:

#s = "[123,[456,[789]]]" 用這當例子, 可以跟341一起服用, 刷題用這個
#思路: NestedInterger 有可能是數字, 也有可能是list, [123] vs 123, 前者有兩層NestedInterger, 後者只有一層NestedInterger
#前者第一層為NestedInterger() => empty list, 第二層為 NestedInterger(integer)
#這裡的NestedInteger.add(elem) 使用時機都是NestedInteger()=>empty list 加一個NestedInteger
#不會是NestedInteger(val).add
#這裡stack 的用意, 是儲存NestedInterger() initial empty list, 唯一例外是若s = "123", stack直接儲存數字
#若遇到"[" stack 加入一個NestedInterger(), 若遇到"]" 若stack有超過兩個元素, 倒數第二個元素要併吞倒數第一個NestedInterger
#最後stack.pop() 就是答案, 其他NestedInterger()都已被併吞掉, 注意: 加完數字後記得start 變回-1
class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        stack, start = [], -1
        for i, c in enumerate(s):  #利用enumerate 分離元素
            if c == '[':
                stack.append(NestedInteger())  #遇到開口, 增加 NestedInteger()元素, initialize an empty list
            elif c == ']':
                # for last ], it is possible that there is only one NestedInteger
                if len(stack) > 1:  #if stack includes more thn one element, the last one need to be included in the second last one
                    t = stack.pop()
                    stack[-1].add(t)
            elif c.isdigit() or c == '-':  #'5'.isdigit() True 針對string
                if start == -1:
                    start = i  #位置指針紀錄數字開始的index
                if i == len(s) - 1 or not s[i + 1].isdigit():  #not s[i + 1].isdigit(), the next one is not digit, i == len(s) - 1 最後一個 ex: s = "123"
                    if stack:
                        stack[-1].add(NestedInteger(int(s[start:i + 1])))  #s = "[123]"
                    else:
                        stack.append(NestedInteger(int(s[start:i + 1])))  #s = "123"
                    start = -1 #set back to default
        return stack.pop()  #因為NestedInteger的特性, 層層包住, stack.pop() 即是答案


#自己重寫, time complexity O(n), 116ms
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = []
        start = -1
        for i, v in enumerate(s):
            if v == "[":
                stack.append(NestedInteger())
            elif v == "]":
                if len(stack) > 1:
                    t = stack.pop()
                    stack[-1].add(t)
            elif v.isdigit() or v == "-":
                if start == -1:
                    start = i
                if i == len(s)-1 or not s[i+1].isdigit():
                    if stack:
                        stack[-1].add(NestedInteger(int(s[start:i+1])))
                    else:
                        stack.append(NestedInteger(int(s[start:i+1])))
                    start = -1
        return stack.pop()



# s = "[123,[456,[789]]]"
# [(i,v) for i,v in enumerate(s)] , (i,v) 要tuple

# [(0, '['),
#  (1, '1'),
#  (2, '2'),
#  (3, '3'),
#  (4, ','),
#  (5, '['),
#  (6, '4'),
#  (7, '5'),
#  (8, '6'),
#  (9, ','),
#  (10, '['),
#  (11, '7'),
#  (12, '8'),
#  (13, '9'),
#  (14, ']'),
#  (15, ']'),
#  (16, ']')]



#s = "[123,[456,[789]]]" 用這當例子
#recursive solution, 這個方法不難懂, 但沒有上面方法直覺
class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if s[0] != '[':  
            return NestedInteger(int(s))  #這句就是此題recursion 精髓, 直接回報 NestedInteger(int(s))
        nested = NestedInteger()
        numP, start = 0, 1
        for i in range(1, len(s)):
            if (numP == 0 and s[i] == ',') or i == len(s) - 1:
                
                # make sure initially it is not an empty string, EX: "[]"
                if start < i:
                    nested.add(self.deserialize(s[start:i]))
                start = i + 1
            elif s[i] == '[':  #numP 類似開關
                numP += 1
            elif s[i] == ']':
                numP -= 1
        return nested



'''
I was a bit confused by add() and setInteger() both for adding integer element. I think add() can do what setInteger does.

Please note that this is not a very fast solution since it requires scanning elements multiple times according to this element's depth.

Using stack would use space as a trade-off for multiple scanning.
'''







































