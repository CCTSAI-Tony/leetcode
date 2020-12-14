第一题： 删除链表里所有重复元素。

class ListedNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def deleteDuplicate(head):
    if not head:
        return None
    dummy = prev = ListedNode(0)
    dummy.next = head
    cur = head
    nxt = head.next

    while nxt:
        while nxt and nxt.val == cur.val:
            nxt = nxt.next
        if not nxt or not nxt.next or nxt.val != nxt.next.val:
            prev.next = nxt
            prev = prev.next
        cur = nxt
        if nxt:
            nxt = nxt.next
    return dummy.next

a = [ListedNode(1), ListedNode(1), ListedNode(1), ListedNode(2), ListedNode(2), ListedNode(3), ListedNode(4), ListedNode(5), ListedNode(5)]
for i in range(len(a) - 1):
    a[i].next = a[i + 1]
b = deleteDuplicate(a[0])
while b:
    print(b.val)
    b = b.next

=> 3 4

硬币和=target，问多少种不同的排列方式。
#Ways to sum to N using array elements with repetition allowed              
def waysToSum(n: int, k: int) -> int:               
    mod = 10**9 + 7             
    coins = [i for i in range(1, k + 1)]                
                
    f = [1] + [0] * n               
    for i in range(1, n + 1):               
        for coin in coins:              
            if i >= coin:               
                f[i] += f[i - coin]             
    return f[n] % mod               
                
                    
waysToSum(5, 3)             


#準備數據庫與網絡基礎知識