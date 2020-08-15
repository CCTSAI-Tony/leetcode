'''
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. 
Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix

Note that the returned canonical path must always begin with a slash /, 
and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. 
Also, the canonical path must be the shortest string representing the absolute path.

 

Example 1:

Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:

Input: "/a/./b/../../c/"
Output: "/c"
Example 5:

Input: "/a/../../b/../c//.//"
Output: "/c"
Example 6:

Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
'''

class Solution:
    def simplifyPath(self, path):
        stack = []
        for token in path.split('/'):
            if token in ('', '.'): #ex: //, /./ 注意這邊是用tuple ('', '.')
                pass
            elif token == '..': #注意這裡不能使用 elif token == '..' and stack: ex: /../ 因為這樣會讓 .. append to stack 造成 /..
                if stack: 
                    stack.pop() #jump to one step high
            else:
                stack.append(token)
        return '/' + '/'.join(stack) #path must always begin with a slash /

# 自己重寫 time complexity O(n)
# 思路: 此題重點在於一開始即split("/"), 並skip "" and ".", 遇到".." 則stack.pop() 回到上一層即可, 最後再 "/".join()
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for i in path.split("/"):
            if i in ("", "."):
                continue
            elif i in (".."):
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "/" + "/".join(stack)

'''
path = "/home//foo/"
path.split('/')
['', 'home', '', 'foo', '']

stack = ['', 'home', '', 'foo', '']
a = '/'.join(stack)
a
'/home//foo/'

'''
Python的collections中有一个deque,这个对象类似于list列表，不过你可以操作它的“两端”。
deque是通过extend方法初始化集合元素的，同时你可以通过extendleft将结合元素从“左边”加入到集合中：

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

extend: deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
append: deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
extendleft: deque([5, 4, 3, 2, 1, 0])
appendleft: deque([6, 5, 4, 3, 2, 1, 0])

可知extend相比append 多了迭代功能
a = [1,2,3]
a.append([123])
a
[1, 2, 3, [123]]

a = [1,2,3]
a.extend([123])
a
[1, 2, 3, 123]
a.extend("123")
a
[1, 2, 3, 123, '1', '2', '3']
a.append("123")
a
[1, 2, 3, 123, '1', '2', '3', '123']

a = []
a.extend(range(5))
a
[0, 1, 2, 3, 4]
a.append(range(4))
a
[0, 1, 2, 3, 4, range(0, 4)]













'''