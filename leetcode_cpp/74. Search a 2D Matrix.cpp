// 刷題用這個, time complexity O(mlogn)
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        for (auto row: matrix) {
            if (row.back() < target) continue;
            int l = 0, r = row.size() - 1;
            while (l + 1 < r) {
                int mid = l + (r - l) / 2;
                if (row[mid] >= target) r = mid;
                else l = mid;
            }
            if (row[l] == target || row[r] == target) return true;
            else return false;
        }
        return false;
    }
};
