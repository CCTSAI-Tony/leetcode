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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (!root) return res;
        deque<TreeNode*> queue {root};
        while (!queue.empty()) {
            vector<int> layer;
            int queue_size = queue.size();
            for (auto i=0; i < queue_size; i++) {
                TreeNode* node;
                node = queue.front();
                queue.pop_front();
                layer.emplace_back(node->val);
                if (node->left) queue.emplace_back(node->left);
                if (node->right) queue.emplace_back(node->right);
            }
            res.emplace_back(layer);
        }
        return res;
    }
};

