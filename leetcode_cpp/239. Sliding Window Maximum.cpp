// time complexity O(n)
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        deque<int> dq;
        for (int i=0; i < (k-1); i++) helper(nums, i, dq);
        int start {0};
        for (int end = k-1; end < nums.size(); end++) {
            helper(nums, end, dq);
            while (dq.front() < start) dq.pop_front();
            res.push_back(nums[dq.front()]);
            start++;
        }
        return res;
    }
    
    void helper(vector<int>& nums, int i, deque<int>& dq) {
        while (!dq.empty() && nums[i] > nums[dq.back()]) {
            dq.pop_back();
        }
        dq.push_back(i);
    }
};




