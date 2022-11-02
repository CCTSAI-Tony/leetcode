class Solution {
public:
    void reorderList(ListNode* head) {
        vector<ListNode*> stack;
        ListNode* pointer = head;
        while (pointer) {
            stack.push_back(pointer);
            pointer = pointer->next;
        }
        int l = 0, r = stack.size() - 1;
        while (l < r) {
            stack[l]->next = stack[r];
            l++;
            stack[r]->next = stack[l];
            r--; 
        }
        if (!stack.empty()) stack[l]->next = NULL;
    }
};

