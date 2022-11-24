class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        return select(0, nums.size() - 1, nums, nums.size() - k);
    }
    
    int select(int l, int r, vector<int>& nums, int k) {
        int pivot = rand() % (r - l + 1) + l;
        int pivot_idx = partition(nums, l, r, pivot);
        if (pivot_idx > k) return select(l, pivot_idx - 1, nums, k);
        else if (pivot_idx < k) return select(pivot_idx+1, r, nums, k);
        else return nums[k];
    }
    
    int partition(vector<int>& nums, int l, int r, int pivot) {
        int temp = nums[pivot];
        nums[pivot] = nums[r];
        nums[r] = temp;
        int pivot_idx = l;
        for (auto i=l; i < r; i++) {
            if (nums[i] < nums[r]) {
                temp = nums[i];
                nums[i] = nums[pivot_idx];
                nums[pivot_idx] = temp;
                pivot_idx++;
            }
        }
        temp = nums[r];
        nums[r] = nums[pivot_idx];
        nums[pivot_idx] = temp;
        return pivot_idx;
    }
};

