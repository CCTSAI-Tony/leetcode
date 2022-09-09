// 模板二, time complexity O(logn)
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l + 1 < r) {
            int mid = l + (r - l)/2;
            if (nums[mid] > target) r = mid;
            else l = mid;
        }
        if (nums[l] == target) return l;
        else if (nums[r] == target) return r;
        else return -1;
    }
};

