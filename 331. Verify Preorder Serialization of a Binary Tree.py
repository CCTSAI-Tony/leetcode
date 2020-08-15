'''
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. 
If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. 
Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:

Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:

Input: "1,#"
Output: false
Example 3:

Input: "9,#,#,1"
Output: false
'''

# This is very simple problem if you use stacks. The key here is, when you see two consecutive "#" characters on stack, 
# pop both of them and replace the topmost element on the stack with "#". For example,

# preorder = 1,2,3,#,#,#,#

        1
       / \
      2   #
     / \
    3   #
   / \
  #   #

# Pass 1: stack = [1]

# Pass 2: stack = [1,2]

# Pass 3: stack = [1,2,3]

# Pass 4: stack = [1,2,3,#]

# Pass 5: stack = [1,2,3,#,#] -> two #s on top so pop them and replace top with #. -> stack = [1,2,#,#]

# Pass 6: stack = [1,2,#,#] -> two #s on top so pop them and replace top with #. -> stack = [1,#,#]

# Pass 7: stack = [1,#,#] -> two #s on top so pop them and replace top with #. -> stack = [#]

# If there is only one # on stack at the end of the string then return True else return False.

'''
 This is a brilliant solution. I could not wrap my head around the idea why the top element was replaced by 
 # when you encounter two #'s and pop them out. After going through couple of example it clicked me (late) that by replacing 
 the top with hash you are shrinking tree's child to null because you already process the child and all it's children.
'''

#preorder traversal: root=>left=>right  這題很棒!
#time complexity O(n)
#思路: 利用stack 來紀錄preorder 的序列, 若stack紀錄到倒數兩個items 都是"#" 代表倒數第三個node是最近的root, 底下左右nodes都以遍歷完成不然就是null
#再把倒數第三個node設為"#", 代表已遍歷完成, 再往上一個root回追, 最後會只剩下一個#, 代表最上面的root
#若不是有效的preorder序列有可能pop倒數兩個# 序列就變empty, or 最後不會只剩下一個#
#技巧: 先把string.split(","), 再利用while loop 來連續消除['#', '#']
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for c in preorder.split(','):
            stack.append(c)
            while stack[-2:] == ['#', '#']:  #stack[-2:] 代表從倒數第二個開始到最後
                stack.pop()
                stack.pop()
                if not stack:  #avoid pop out from empty list
                    return False
                stack.pop()
                stack.append('#')  #replace upper node with # to state that it has already been searched
        return stack == ['#']  #finally, it only be left by one root


#自己重寫, time complexity O(n)
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for i in preorder.split(","):
            stack.append(i)
            while stack[-2:] == ["#","#"]:
                stack.pop()
                stack.pop()
                if not stack:
                    return False
                stack.pop()
                stack.append("#")
        return stack == ["#"]

# class Solution:
#     def isValidSerialization(self, preorder: str) -> bool:
#         stack = []
#         for c in preorder.split(','):
#             stack.append(c)
#             print(stack)
#             while stack[-2:] == ['#', '#']:
#                 stack.pop()
#                 stack.pop()
#                 if not stack: return False
#                 stack.pop()
#                 stack.append('#')
#         return stack == ['#']
        
     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #

# "9,3,4,#,#,1,#,#,2,#,6,#,#"
# print(stack)
# ['9']
# ['9', '3']
# ['9', '3', '4']
# ['9', '3', '4', '#']
# ['9', '3', '4', '#', '#']
# ['9', '3', '#', '1']
# ['9', '3', '#', '1', '#']
# ['9', '3', '#', '1', '#', '#']
# ['9', '#', '2']
# ['9', '#', '2', '#']
# ['9', '#', '2', '#', '6']
# ['9', '#', '2', '#', '6', '#']
# ['9', '#', '2', '#', '6', '#', '#']






