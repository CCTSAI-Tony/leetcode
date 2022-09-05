// 刷題用這個, time complexity O(n)
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        heights.emplace_back(0);
        vector<int> stack {(int) heights.size() - 1};
        int ans {0};
        for (int i = 0; i < heights.size(); i++) {
            while (heights[i] < heights[stack.back()]) {
                int h = heights[stack.back()];
                stack.pop_back();
                int w;
                if (stack.back() == heights.size() - 1) w = i - (-1) - 1;
                else (w = i - stack.back() - 1);
                ans = max(ans, h * w);
            }
            stack.emplace_back(i);
        }
        return ans;
    }
};

// 重寫第二次
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        heights.emplace_back(0);
        vector<int> stack {(int) heights.size() - 1};
        int ans {0};
        for (int i = 0; i < heights.size(); i++) {
            while (heights[i] < heights[stack.back()]) {
                int h = heights[stack.back()];
                stack.pop_back();
                int w = (stack.back() == heights.size() - 1) ? i - (-1) - 1: i - stack.back() - 1;
                ans = max(ans, h * w);
            }
            stack.emplace_back(i);
        }
        return ans;
    }
};

