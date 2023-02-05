// 刷題用這個
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> rotten;
        vector<pair<int, int>> origin_fresh;
        vector<pair<int, int>> direcs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int minutes {0};
        int m = grid.size();
        int n = grid[0].size();
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == 2) rotten.push({i, j});
                else if (grid[i][j] == 1) origin_fresh.push_back({i, j});
            }
        }
        while (!rotten.empty()) {
            int rotten_size = rotten.size();
            for (int t=0; t<rotten_size; t++) {
                int i, j;
                tie(i, j) = rotten.front();
                rotten.pop();
                for (auto d: direcs) {
                    int x = i + d.first;
                    int y = j + d.second;
                    if (x>=0 && x<m && y>=0 && y<n && grid[x][y] == 1) {
                        rotten.push({x, y});
                        grid[x][y] = 2;
                    }
                }
            }
            if (!rotten.empty()) minutes++;
        }
        for (auto p:origin_fresh) {
            int x, y;
            tie(x, y) = p;
            if (grid[x][y] == 1) return -1;
        }
        return minutes;
    }
};
