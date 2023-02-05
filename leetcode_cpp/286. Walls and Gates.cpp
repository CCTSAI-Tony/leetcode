// 刷題用這個
class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        if (rooms.empty() || rooms[0].empty()) return;
        int m = rooms.size();
        int n = rooms[0].size();
        vector<pair<int, int>> direcs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        queue<pair<int, int>> que;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (rooms[i][j] == 0) que.push({i, j});
            }
        }
        int k {1};
        while (!que.empty()) {
            int que_size = que.size();
            for (int t=0; t<que_size; t++) {
                int i, j;
                tie(i, j) = que.front();
                que.pop();
                for (auto d: direcs) {
                    int x = i + d.first;
                    int y = j + d.second;
                    if (x>=0 && x<m && y>=0 && y<n && rooms[x][y] == INT_MAX) {
                        que.push({x, y});
                        rooms[x][y] = k;
                    }
                }
            }
            k++;
        }
    }
};

