/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        deque<pair<TreeNode*, TreeNode*>>queue = {make_pair(p, q)};
        while (!queue.empty()) {
            TreeNode *node1, *node2;
            tie(node1, node2) = queue.front();
            queue.pop_front();
            if (!node1 && !node2) continue;
            else if (!node1 || !node2) return false;
            else {
                if (node1->val != node2->val) return false;
                queue.emplace_back(make_pair(node1->left, node2->left));
                queue.emplace_back(make_pair(node1->right, node2->right));
            }
        }
        return true;
    }
};

