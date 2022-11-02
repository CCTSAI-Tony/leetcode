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
    int goodNodes(TreeNode* root) {
        int res {0};
        dfs(root, INT_MIN, res);
        return res;
    }
    
    void dfs(TreeNode* node, int max_val, int& res) {
        if (max_val <= node->val) res++;
        max_val = max(max_val, node->val);
        if (node->left) dfs(node->left, max_val, res);
        if (node->right) dfs(node->right, max_val, res);
    }
};

