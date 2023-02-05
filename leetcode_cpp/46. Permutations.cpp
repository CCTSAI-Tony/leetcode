// 刷題用這個, time complexity O(n!), space complexity O(n!)
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> temp;
        dfs(nums, temp, res);
        return res;
    }

    void dfs(vector<int>& nums, vector<int>& path, vector<vector<int>>& res) {
        if (nums.empty()) res.push_back(path);
        for (int i=0; i<nums.size(); i++ ) {
            vector<int> nxt;
            for (int j=0; j<nums.size(); j++) {
                if (j != i) nxt.push_back(nums[j]);
            }
            path.push_back(nums[i]);
            dfs(nxt, path, res);
            path.pop_back();
        }
    }
};
