// 刷題用這個, time complexity O(mn), space complexity O(h)
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        if (m == 0 || n == 0) return 0;
        int max_area {0};
        vector<pair<int, int>> direcs {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == 1) {
                    max_area = max(max_area, dfs(i, j, grid, m, n, direcs));
                }
            }
        }
        return max_area;
    }

    int dfs(int i, int j, vector<vector<int>>& grid, int m, int n, vector<pair<int, int>>& direcs) {
        grid[i][j] = 0;
        int area = {1};
        for (auto d: direcs) {
            int x = i + d.first;
            int y = j + d.second;
            if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == 1) {
                area += dfs(x, y, grid, m, n, direcs);
            }
        }
        return area;
    }
};

