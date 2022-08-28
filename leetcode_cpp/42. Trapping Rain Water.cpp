// time complexity O(n)
class Solution {
public:
    int trap(vector<int>& height) {
        vector<int> height_left;
        vector<int> height_right;
        int left {0}, right {0}, water {0};
        for (int i = 0; i < height.size(); i++){
            left = max(left, height[i]);
            height_left.push_back(left);
        }
        for (int i = height.size() - 1; i >= 0; i--){
            right = max(right, height[i]);
            height_right.push_back(right);
        }
        reverse(height_right.begin(), height_right.end());
        for (int i = 0; i < height.size(); i++){
            water += (min(height_left[i], height_right[i]) - height[i]);
        }
        return water;
    }
};
