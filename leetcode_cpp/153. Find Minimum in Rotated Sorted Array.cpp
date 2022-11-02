class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] > nums[r]) l = mid;
            else r = mid;
        }
        return min(nums[l], nums[r]);
    }
};

