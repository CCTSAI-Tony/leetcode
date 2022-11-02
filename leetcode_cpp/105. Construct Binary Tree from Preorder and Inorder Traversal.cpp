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

// conversion
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        deque<int> preorder_deq(preorder.begin(), preorder.end());
        return helper(preorder_deq, inorder, 0, inorder.size());
    }
    
    TreeNode* helper(deque<int>& preorder, vector<int>& inorder, int l, int r) {
        if (l < r) {
            int val {preorder.front()};
            preorder.pop_front();
            TreeNode* root = new TreeNode(val);
            auto idx = find(inorder.begin(), inorder.end(), val);
            int index = idx - inorder.begin();
            root->left = helper(preorder, inorder, l, index);
            root->right = helper(preorder, inorder, index+1, r);
            return root;
        }
        return NULL;
    }
};

// move
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        deque<int> preorder_deq;
        move(begin(preorder), end(preorder), back_inserter(preorder_deq));
        int preorder_deq_size = preorder_deq.size();
        return helper(preorder_deq, inorder, 0, inorder.size());
    }
    
    TreeNode* helper(deque<int>& preorder, vector<int>& inorder, int l, int r) {
        if (l < r) {
            int val {preorder.front()};
            preorder.pop_front();
            TreeNode* root = new TreeNode(val);
            auto idx = find(inorder.begin(), inorder.end(), val);
            int index = idx - inorder.begin();
            root->left = helper(preorder, inorder, l, index);
            root->right = helper(preorder, inorder, index+1, r);
            return root;
        }
        return NULL;
    }
};

// copy
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int size = preorder.size();
        deque<int> preorder_deq(size);
        copy(preorder.begin(), preorder.end(), preorder_deq.begin());
        return helper(preorder_deq, inorder, 0, inorder.size());
    }
    
    TreeNode* helper(deque<int>& preorder, vector<int>& inorder, int l, int r) {
        if (l < r) {
            int val {preorder.front()};
            preorder.pop_front();
            TreeNode* root = new TreeNode(val);
            auto idx = find(inorder.begin(), inorder.end(), val);
            int index = idx - inorder.begin();
            root->left = helper(preorder, inorder, l, index);
            root->right = helper(preorder, inorder, index+1, r);
            return root;
        }
        return NULL;
    }
};



