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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        return dfs(root, subRoot);
    }
    
    bool dfs(TreeNode* node, TreeNode* subRoot) {
        if (!checkIsSame(node, subRoot)) {
            bool left, right;
            left = false;
            right = false;
            if (node->left) left = dfs(node->left, subRoot);
            if (node->right) right = dfs(node->right, subRoot);
            return left || right;
        }
        return true;
    }
    
    bool checkIsSame(TreeNode* node1, TreeNode* node2) {
        if (!node1 && !node2) return true;
        if (!node1 || !node2) return false;
        if (node1->val != node2->val) return false;
        bool left = checkIsSame(node1->left, node2->left);
        bool right = checkIsSame(node1->right, node2->right);
        return left && right;
    }
};

