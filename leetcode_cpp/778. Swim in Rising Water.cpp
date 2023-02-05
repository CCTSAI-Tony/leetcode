// 刷題用這個, time complexity O(N^2*logN), space compolexity O(N^2)
class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<bool>> seen(n, vector(n, false));
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> hp;
        hp.push({grid[0][0], 0, 0});
        vector<pair<int, int>> directs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int ans = 0;
        while (!hp.empty()) {
            int ele, r, c;
            tie(ele, r, c) = hp.top();
            hp.pop();
            ans = max(ans, ele);
            if (r == n-1 && c == n-1) {
                return ans;
            }
            for (auto direct: directs) {
                int n_r = r + direct.first;
                int n_c = c + direct.second;
                if (n_r >= 0 && n_r < n && n_c >= 0 && n_c < n && !seen[n_r][n_c]) {
                    seen[n_r][n_c] = true;
                    hp.push({grid[n_r][n_c], n_r, n_c});
                }
            }
        }
        return -1;
    }
};

// 使用tuple
class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<bool>> seen(n, vector(n, false));
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> hp;
        hp.push({grid[0][0], 0, 0});
        vector<tuple<int, int>> directs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int ans = 0;
        while (!hp.empty()) {
            int ele, r, c;
            tie(ele, r, c) = hp.top();
            hp.pop();
            ans = max(ans, ele);
            if (r == n-1 && c == n-1) {
                return ans;
            }
            for (auto direct: directs) {
                int n_r = r + get<0>(direct); // 使用get
                int n_c = c + get<1>(direct);
                if (n_r >= 0 && n_r < n && n_c >= 0 && n_c < n && !seen[n_r][n_c]) {
                    seen[n_r][n_c] = true;
                    hp.push({grid[n_r][n_c], n_r, n_c});
                }
            }
        }
        return -1;
    }
};