/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root) return NULL;
        return dfs(root, p, q);
    }
    
    TreeNode* dfs(TreeNode* node, TreeNode* p, TreeNode* q) {
        if (!node) return NULL;
        if (node == p || node == q) return node;
        TreeNode *left, *right;
        left = dfs(node->left, p, q);
        right = dfs(node->right, p, q);
        if (left && right) return node;
        else return left? left:right;
    }
};

