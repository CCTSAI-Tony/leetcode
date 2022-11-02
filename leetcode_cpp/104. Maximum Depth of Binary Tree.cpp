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
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        deque<pair<TreeNode*, int>> queue {make_pair(root, 1)};
        int max_depth = 0;
        while (!queue.empty()) {
            int queue_size = queue.size();
            for (auto i=0; i < queue_size; i++) {
                TreeNode* node;
                int depth;
                tie(node, depth) = queue.front();
                queue.pop_front();
                max_depth = max(max_depth, depth);
                if (node->left) queue.emplace_back(make_pair(node->left, depth+1));
                if (node->right) queue.emplace_back(make_pair(node->right, depth+1));
            }
        }
        return max_depth;
    }
};

// dfs
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        return dfs(root);
    }
    
    int dfs(TreeNode* root) {
        if (!root) return 0;
        return 1 + max(dfs(root->left), dfs(root->right));
    }
};

