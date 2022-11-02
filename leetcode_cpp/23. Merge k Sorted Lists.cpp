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

// 刷題用這個, time complexity O(mnlogn), space complexity O(logn), m:len(sorted_list), n: len(lists)
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        return mergeKLists(lists, 0, lists.size() - 1);
        }
    
    ListNode* mergeKLists(vector<ListNode*>& lists, int s, int e) {
        if (s > e) return NULL;
        else if (s == e) return lists[s];
        else if ((s + 1) == e) return merge(lists[s], lists[e]);
        int mid = (s + e) / 2;
        ListNode* l = mergeKLists(lists, s, mid-1);
        ListNode* r = mergeKLists(lists, mid, e);
        return merge(l, r);
        }
    
    ListNode* merge(ListNode* l, ListNode* r) {
        ListNode* dummy = new ListNode;
        ListNode* cur = dummy;
        while (l && r) {
            if (l->val < r->val) {
                cur->next = l;
                l = l->next;
            }
            else {
                cur->next = r;
                r = r->next;
            }
            cur = cur->next;
        }
        cur->next = l? l:r;
        return dummy->next;
    }
};



