// time complexity O(n^2)
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;
        sort(nums.begin(), nums.end());
        dfs(nums, 0, path, res);
        return res;
    }

    void dfs(vector<int>& nums, int index, vector<int>& path, vector<vector<int>>& res) {
        res.push_back(path);
        for (int i=index; i<nums.size();i++) {
            if (i > index && nums[i] == nums[i-1]) continue;
            path.push_back(nums[i]);
            dfs(nums, i+1, path, res);
            path.pop_back();
        }
    }
};
