'''
A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. 
Leaf nodes (nodes with 0 children) correspond to operands (numbers), 
and internal nodes (nodes with 2 children) correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

For each internal node with operator o, the infix expression that it represents is (A o B), 
where A is the expression the left subtree represents and B is the expression the right subtree represents.

You are given a string s, an infix expression containing operands, the operators described above, and parentheses '(' and ')'.

Return any valid binary expression tree, which its in-order traversal reproduces s after omitting the parenthesis from it (see examples below).

Please note that order of operations applies in s. That is, expressions in parentheses are evaluated first, 
and multiplication and division happen before addition and subtraction.

Operands must also appear in the same order in both s and the in-order traversal of the tree.

 

Example 1:


Input: s = "3*4-2*5"
Output: [-,*,*,3,4,2,5]
Explanation: The tree above is the only valid tree whose inorder traversal produces s.
Example 2:


Input: s = "2-3/(5*2)+1"
Output: [+,-,1,2,/,null,null,null,null,3,*,null,null,5,2]
Explanation: The inorder traversal of the tree above is 2-3/5*2+1 which is the same as s without the parenthesis. 
The tree also produces the correct result and its operands are in the same order as they appear in s.
The tree below is also a valid binary expression tree with the same inorder traversal as s, but it not a valid answer because it does not evaluate to the same value.

The third tree below is also not valid. Although it produces the same result and is equivalent to the above trees, 
its inorder traversal does not produce s and its operands are not in the same order as s.

Example 3:

Input: s = "1+2+3+4+5"
Output: [+,+,5,+,4,null,null,+,3,null,null,1,2]
Explanation: The tree [+,+,5,+,+,null,null,1,2,3,4] is also one of many other valid trees.
 

Constraints:

1 <= s.length <= 1000
s consists of digits and the characters '+', '-', '*', and '/'.
Operands in s are exactly 1 digit.
It is guaranteed that s is a valid expression.
'''

# 刷題用這個, time complexity O(n), space complexity O(n) 
# 思路: inorder traversal 搭配 basic calculator III, 利用stack 來存儲operands and nodes, 並利用*, / 優先的rule => ex: (3 + 5 => 不能產生node) * 7 vs (3 * 5 => 產生node) * 7
# ex: (5 + 7 * 6) => 7*6 -> (node) => 5 + (7*6) -> (node) -> pop掉 "("
class Solution:
    def expTree(self, s: str) -> 'Node':
        ops, nums = [], []

        def mock_compute():
            op = ops.pop()
            r = nums.pop()
            l = nums.pop()
            nums.append(Node(val=op, left=l, right=r))
            
        for ch in s:
            if ch.isdigit():
                nums.append(Node(val=ch))
            elif ch in ['+', '-']:
                while ops and ops[-1] in ['+', '-', '*', '/']:
                    mock_compute()
                ops.append(ch)
            elif ch in ['*', '/']: 
                while ops and ops[-1] in ['*', '/']: # *, / 優先計算, 所以可以先生成node
                    mock_compute()
                ops.append(ch)
            elif ch == '(':
                ops.append(ch)
            elif ch == ')':
                while ops[-1] != '(':
                    mock_compute()
                ops.pop()
        while ops:
            mock_compute()
        return nums[0]


#重寫第二次, time complexity O(n), space complexity O(n)
class Solution:
    def expTree(self, s: str) -> 'Node':
        ops, nodes = [], []
        for ch in s:
            if ch.isdigit():
                node = Node(ch)
                nodes.append(node)
            elif ch in ["+", "-"]:
                while ops and ops[-1] in ["+", "-", "*", "/"]:
                    self.compute(ops, nodes)
                ops.append(ch)
            elif ch in ["*", "/"]:
                while ops and ops[-1] in ["*", "/"]:
                    self.compute(ops, nodes)
                ops.append(ch)
            elif ch == "(":
                ops.append(ch)
            elif ch == ")":
                while ops and ops[-1] != "(":
                    self.compute(ops, nodes)
                ops.pop()
        while ops:
            self.compute(ops, nodes)
        return nodes[0]
    
    def compute(self, ops, nodes):
        op = ops.pop()
        r = nodes.pop()
        l = nodes.pop()
        node = Node(op, l, r)
        nodes.append(node)




