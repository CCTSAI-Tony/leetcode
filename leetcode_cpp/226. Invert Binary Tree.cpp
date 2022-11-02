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
    TreeNode* invertTree(TreeNode* root) {
        deque<TreeNode*>deque {root};
        while (!deque.empty()) {
            TreeNode* node = deque.front();
            deque.pop_front();
            if (node) {
                TreeNode* temp = node->left;
                node->left = node->right;
                node->right = temp;
                deque.emplace_back(node->left);
                deque.emplace_back(node->right);
            }
        }
        return root;
    }
};

