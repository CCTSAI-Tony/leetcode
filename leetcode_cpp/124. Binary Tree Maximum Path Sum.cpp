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
    int max_sum {INT_MIN};
    int maxPathSum(TreeNode* root) {
        if (!root) return 0;
        dfs(root);
        return max_sum;
    }
    
    int dfs(TreeNode* node) {
        if (!node) return 0;
        int left_sum = max(0, dfs(node->left));
        int right_sum = max(0, dfs(node->right));
        max_sum = max(max_sum, node->val + left_sum + right_sum);
        return max(left_sum, right_sum) + node->val;
    }
};

