class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (!nums.size()) return -1;
        int low = 0, high = nums.size() - 1;
        while (low + 1 < high) {
            int mid = low + (high - low) / 2;
            if (nums[low] <= nums[mid]) {
                if (nums[low] <= target && target <= nums[mid]) high = mid; //注意, c++ 不能寫成 nums[low] <= target <= nums[mid], 因為c++ 會從右到左判斷
                else low = mid;
            }
            else {
                if (nums[mid] <= target && target <= nums[high]) low = mid;
                else high = mid;
            }
        }
        if (target == nums[low]) return low;
        else if (target == nums[high]) return high;
        return -1;
    }
};

