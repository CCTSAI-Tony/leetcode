'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL


'''
leetcode 92 經典
#思路: 使用dummy head, 與pre 指針, 先讓pre指針走到m-1的位置, 建立cur指針站在m位置上, 額外建立node指針, 之後先紀錄cur指針的下一個為next
#cur.next 接node, node指針指向cur, cur指針指向next, 再一次循環, 最後reverse完指定nodes, 此時pre.next 依舊指向reverse前的第一個node, 現在reverse後變成指定最後一個
#讓reverse指定最後一個 接回剩下未reverse的node
# cur = pre.next #站在m點 建立cur指針, 重要!!, 但pre 的next 指向誰不受cur指針影響, 因為一開始cur與pre不是指向同一個物件(記憶體), cur影響的記憶體是pre.next
class Solution:
    def reverseBetween(self, head, m, n):
    dummy = pre = ListNode(0) #dummy 與 pre 是指向同一個物件
    dummy.next = head
    for _ in range(m-1): #pre 停在m 前一個
        pre = pre.next
    cur = pre.next #站在m點 建立cur指針, 重要!!, 但pre 的next 指向誰不受cur指針影響, 因為一開始cur與pre不是指向同一個物件
    # reverse the defined part
    node = None #只是預設值 其他值也可以
    for _ in range(n-m+1): #reverse移動次數(reverse node的長度)
        nxt = cur.next #現紀錄下一個node是誰
        cur.next = node # 處理當下元素
        node = cur # node: none-> 2>none-> 3>2>none-> 4>3>2>none, 移動node指針 by 一直替換node.head
        cur= nxt #回到最初的線
    # connect three parts
    pre.next.next = cur #pre.next 原本是沒reverse的第一個node, 因為reverse變成最後一個, 要接回剩下沒反轉的
    pre.next = node # 改接回反轉後的第一個node
    return dummy.next


#自己重寫
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = pre = ListNode
        pre.next = head
        for _ in range(m-1):
            pre = pre.next
        cur = pre.next
        temp = None
        for _ in range(n-m+1):
            next = cur.next
            cur.next = temp
            temp = cur
            cur = next
        pre.next.next = cur
        pre.next = temp
        return dummy.next








'''
    1->2->3->4->5->NULL m= 2 n =4

dp  p  c
          n
       c.next=node(none>c)



pre: 1

node: 4>3>2>(none)最終被替換

cur: 5>none

dummy.next: 1>4>3>2>5>none

pre.next = node
pre.next.next = cur

[1,4,5] 順序顛倒會變這樣！






'''
