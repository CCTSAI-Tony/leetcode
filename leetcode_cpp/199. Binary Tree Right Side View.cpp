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

// bfs
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if (!root) return res;
        deque<TreeNode*> queue {root};
        while (!queue.empty()) {
            int queue_size = queue.size();
            vector<int> layer;
            for (auto i=0; i < queue_size; i++) {
                TreeNode* node {queue.front()};
                queue.pop_front();
                layer.emplace_back(node->val);
                if (node->left) queue.emplace_back(node->left);
                if (node->right) queue.emplace_back(node->right);
            }
            res.emplace_back(layer.back());
        }
        return res;
    }
};

// dfs
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> view;
        rightView(root, view, 0);
        return view;
    }
private:
    void rightView(TreeNode* root, vector<int>& view, int level) {
        if (!root) {
            return;
        }
        if (view.size() == level) {
            view.push_back(root -> val);
        }
        rightView(root -> right, view, level + 1);
        rightView(root -> left, view, level + 1);
    }
};
