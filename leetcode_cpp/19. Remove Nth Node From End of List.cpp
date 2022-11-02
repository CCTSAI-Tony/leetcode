class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy = ListNode();
        ListNode* slow = &dummy;
        ListNode* fast = &dummy;
        dummy.next = head;
        for (int i = 0; i < n; i++) fast = fast->next;
        while (fast->next) {
            fast = fast->next;
            slow = slow->next;
        }
        slow->next = slow->next->next;
        return dummy.next;
    }
};

 