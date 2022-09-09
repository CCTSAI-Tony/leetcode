// time complexity O(n). monotonic queue
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res (temperatures.size(), 0);
        vector<int> stack;
        for (int i = 0; i < temperatures.size(); i++) {
            int t = temperatures[i];
            while (!stack.empty() && temperatures[stack.back()] < t) {
                int cur = stack.back();
                stack.pop_back();
                res[cur] = i - cur;
            }
            stack.emplace_back(i);
        }
        return res;
    }
};

