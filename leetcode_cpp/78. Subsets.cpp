class Solution {
public:
    vector<vector<int>> res;
    vector<int> cur;
    vector<vector<int>> subsets(vector<int>& nums) {
        res.push_back(cur);
        dfs(nums, 0);
        return res;
    }
    void dfs(vector<int>& nums, int idx) {
        for (int i=idx; i<nums.size(); i++) {
            cur.push_back(nums[i]);
            res.push_back(cur);
            dfs(nums, i+1);
            cur.pop_back();
        }
    }
};
