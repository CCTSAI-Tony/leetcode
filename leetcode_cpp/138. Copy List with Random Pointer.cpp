/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == NULL) return NULL;
        Node* cur = head;
        unordered_map<Node*, Node*> dic;
        while (cur) {
            dic[cur] = new Node(cur->val);
            cur = cur->next;
        }
        cur = head;
        while (cur) {
            if (cur->random) dic[cur]->random = dic[cur->random];
            if (cur->next) dic[cur]->next = dic[cur->next];
            cur = cur->next;
        }
        return dic[head];
    }
};



