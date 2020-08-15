'''
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
'''

# Python reservoir sampling solution (when the length of linked list changes dynamically)

https://www.geeksforgeeks.org/reservoir-sampling/

'''
The problem is a little ambiguous. In the interview, you should ask clearly whether the list length is unknown but static or 
it is unknown and dynamically changing. In the first case, you can simply precompute the length and generate random indices based on that. 
It is faster than the reservior sampling solution.

If the list length changes dynamically, reservior sampling is a good choice. If you are not familiar with it, check here.
'''

#這題很蛋疼 不過原理不複雜, 首先選k item elements, 之後k+1 elements 開始, 若random.randint(0,目前index) = 0, 則被放入reservoir
#愈早的item 被抓進去的機率高, 但後面排隊的elements 都有機會取代他, 後面的eklement 雖抓進去機會小, 但不易取代
class Solution(object):

    def __init__(self, head):  #Note that the head is guaranteed to be not null, so it contains at least one node.
        self.head = head

    def getRandom(self):
        result, node, index = self.head, self.head.next, 1  #index = 1, reservoir 1 item
        while node:
            if random.randint(0, index) is 0:
                result = node
            node = node.next
            index += 1
        return result.val



# a = 1
# for a in range(5): #a 被影響了
#     print(a)
# 0
# 1
# 2
# 3
# 4
# a
# 6