'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


 

Follow-up:
Can you solve it without using extra space?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#  刷題用這個, time complexity O(n)
#  思路: 利用快慢指針來確認是否有cycle, 若有cycle則快指針會與慢針相遇, 若無則快指針會先到none, 所以使用try, except抓錯
#  快指針快慢指針2倍, 查看下面圖, 設他們相遇時 慢指針走了h steps進入 cycle, 再走了d steps 與快指針相遇, 
#  快指針總步數 => 2(h+d) = h + nc + d => h = nc -d, 證明出當它們第一次相遇再讓慢指針從頭走h步到cycle入口會與快指針相遇(快指針從相遇點一步一步走)=>再次相遇就是cycle 路口
#  注意: 一開始為何slow, fast 不從head出發, 因為這樣一開始slow = fast = head, 一開始迴圈就斷了, 所以一開始就要各先走一步與兩步來錯開
#  若h = 0, head就是迴圈入口如何? 就算一開始錯開, 慢指針, 快指針終究會與在head點相遇, 奇數node cycle or 偶數node cyclea都一樣, 畫圖就清楚了(跑操場的概念)
class Solution:
    def detectCycle(self, head):
        try: ##如果有尾部，必然出错，进入except。
            Slow = head.next ## 保证Slow和 Fast同时移动
            Fast = head.next.next
            while Slow!=Fast: ## Fast一直是Slow的两倍速度，这点很关键, 若有circle他們終究會相會
                Slow = Slow.next
                Fast = Fast.next.next
        except:
            return None       
        Slow = head ##让Slow从头开始，Fast保持上一步的位置
        while Slow != Fast:
            Slow = Slow.next
            Fast = Fast.next
        return Slow


# 重寫第二次, time complexity O(n), space complexity O(1)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow = head.next
        fast = head.next.next
        while slow != fast and fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        if fast == None or fast.next == None:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow







'''

                          _____
                         /     \
        head_____H_____r_      \
                        \       /
                         m_____/   
        
    
       

首先，判定环的存在：
a. 有环的话，快指针和慢指针必然相遇，通过指针相等退出循环；
b. 无环时，快指针将访问非法域，导致异常，从而被try...except...捕获，进而返回None.

判定有环后，利用上一步的信息（相遇的点），判定入口：
a. 设起点q到入口点r的距离为H步，入口r到第一次见面点m的为D步。一圈为C步，设第一次相遇时，Fast相对于r点转了n圈。如下图所示;
b. 则第一次相遇时，Slow运动了(H+D)步，Fast运动了(H + nC + D), 由于Fast指针是慢指针Slow的两倍速度, 从而有距离公式：

                      2(H+D) = H + nC + D,
经过简单的移位运算，有：

                       H = nC -D (想成H很長 迴圈很小 nC概念就懂)
c. 这表明，当我们让Slow重新从q点处、Fast继续从相遇见的m点处，以相等的速度移动时，两个指针会在入口r点相遇。即Slow从q点移动H步，而Fast相当于会从m点移动n圈(会回到m处)，再后退D步。最终都在r点遇见。
上面其實在證明: ws當他們碰到時就在r點

'''
Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the try statement:

Example
The try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")

  Example
Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")













































