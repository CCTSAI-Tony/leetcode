// 刷題用這個
class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        int n = nums.size();

        if (n <= 3) {
            return *max_element(nums.begin(), nums.end());
        }

        vector<int> dp1(n, 0);
        vector<int> dp2(n, 0);

        dp1[0] = nums[0];
        dp1[1] = max(nums[0], nums[1]);
        dp2[1] = nums[1];
        dp2[2] = max(nums[1], nums[2]);

        for (int i=2; i<n-1; i++) {
            dp1[i] = max(nums[i] + dp1[i-2], dp1[i-1]);
        }

        for (int i=3; i<n; i++) {
            dp2[i] = max(nums[i] + dp2[i-2], dp2[i-1]);
        }
        
        int max_dp1 = *max_element(dp1.begin(), dp1.end());
        int max_dp2 = *max_element(dp2.begin(), dp2.end());

        return max(max_dp1, max_dp2);
    }
};
