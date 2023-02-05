// 刷題用這個
class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        int n = nums.size();

        for (int i=0; i<n; i++) {
            if (i == 1) {
                nums[i] = max(nums[0], nums[1]);
            }
            else if (i > 1) {
                nums[i] = max(nums[i] + nums[i-2], nums[i-1]);
            }
        }

        return nums[n-1];
    }
};
