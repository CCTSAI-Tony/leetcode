/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// 刷題用這個, time complexity O(n)
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        int count = 0;
        ListNode* node = head;
        while (node && count < k) {
            node = node->next;
            count++;
        }
        if (count < k) return head;
        ListNode *new_head, *prev;
        tie(new_head, prev) = reverse(head, count);
        head->next = reverseKGroup(new_head, k);
        return prev;
    }
    
    pair<ListNode*, ListNode*> reverse(ListNode* head, int count) {
        ListNode* prev = NULL;
        ListNode* cur = head;
        ListNode* nxt = head;
        while (count > 0) {
            nxt = cur->next;
            cur->next = prev;
            prev = cur;
            cur = nxt;
            count--;
        }
        return make_pair(cur, prev);
    }
};

