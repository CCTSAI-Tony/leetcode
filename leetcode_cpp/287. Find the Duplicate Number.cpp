class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        int l = 0, r = nums.size() - 1;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            int counts = count(nums, mid);
            if (counts > mid) r = mid;
            else l = mid;
        }
        if (count(nums, l) > l) return l;
        return r;
    }
    
    int count(vector<int>& nums, int target) {
        int counts = 0;
        for (auto& num: nums) {
            if (num <= target) ++counts;
        }
        return counts;
    }
};

// 刷題用這個, time complexity O(1), but modifying the array nums
class Solution {
public:
    int store(vector<int>& nums, int cur) {
        if (cur == nums[cur]) // 之前有遇到相同元素
            return cur;
        int nxt = nums[cur];
        nums[cur] = cur;
        return store(nums, nxt);
    }
    
    int findDuplicate(vector<int>& nums) {
        return store(nums, 0);
    }
};

// 自己想的, 刷題用這個, time complexity O(1)
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        for (auto& num: nums) {
            int pos = abs(num) - 1;
            if (nums[pos] < 0) return abs(num);
            nums[pos] *= -1;
        }
        return -1;
    }
};

