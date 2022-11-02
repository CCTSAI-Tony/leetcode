class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        ListNode* p = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return p;
    }
};


// 刷題用這個
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (! head) return NULL;
        ListNode* temp = NULL;
        while (head && head->next) {
            ListNode* next_node = head->next;
            head->next = temp;
            temp = head;
            head = next_node;
        }
        head->next = temp;
        return head;
    }
};

