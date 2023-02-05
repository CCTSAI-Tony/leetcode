/*
    Top & left pacific, bottom & right atlantic, determine spots that flow to both

    Instead go outside in, from oceans to spots where rain could flow from
    Faster bc avoids repeated work: cells along a path can also reach that ocean

    Time: O(m x n)
    Space: O(m x n)
*/

// 刷題用這個
class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();
        vector<vector<bool>> pacific(m, vector<bool>(n));
        vector<vector<bool>> atlantic(m, vector<bool>(n));
        vector<pair<int, int>> direcs {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        vector<vector<int>> res;
        for (int i=0; i<m; i++) {
            dfs(i, 0, m, n, direcs, heights, pacific);
            dfs(i, n-1, m, n, direcs, heights, atlantic);
        }
        for (int j=0; j<n; j++) {
            dfs(0, j, m, n, direcs, heights, pacific);
            dfs(m-1, j, m, n, direcs, heights, atlantic);
        }
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (pacific[i][j] && atlantic[i][j]) res.push_back({i, j});
            }
        }
        return res;
    }

    void dfs(int i, int j, int m, int n, vector<pair<int, int>>& direcs, vector<vector<int>>& heights, vector<vector<bool>>& ocean) {
        ocean[i][j] = true;
        for (auto d: direcs) {
            int x = i + d.first;
            int y = j + d.second;
            if (x>=0 && x<m && y>=0 && y<n && !ocean[x][y] && heights[i][j] <= heights[x][y]) {
                dfs(x, y, m, n, direcs, heights, ocean);
            }
        }
    }
};



class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();
        
        vector<vector<bool>> pacific(m, vector<bool>(n));
        vector<vector<bool>> atlantic(m, vector<bool>(n));
        
        for (int i = 0; i < m; i++) {
            dfs(heights, pacific, i, 0, m, n);
            dfs(heights, atlantic, i, n - 1, m, n);
        }
        
        for (int j = 0; j < n; j++) {
            dfs(heights, pacific, 0, j, m, n);
            dfs(heights, atlantic, m - 1, j, m, n);
        }
        
        vector<vector<int>> result;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    result.push_back({i, j});
                }
            }
        }
        
        return result;
    }
private:
    void dfs(vector<vector<int>>& heights, vector<vector<bool>>& visited,
        int i, int j, int m, int n) {
        
        visited[i][j] = true;
        
        if (i > 0 && !visited[i - 1][j] && heights[i - 1][j] >= heights[i][j]) {
            dfs(heights, visited, i - 1, j, m, n);
        }
        if (i < m - 1 && !visited[i + 1][j] && heights[i + 1][j] >= heights[i][j]) {
            dfs(heights, visited, i + 1, j, m, n);
        }
        if (j > 0 && !visited[i][j - 1] && heights[i][j - 1] >= heights[i][j]) {
            dfs(heights, visited, i, j - 1, m, n);
        }
        if (j < n - 1 && !visited[i][j + 1] && heights[i][j + 1] >= heights[i][j]) {
            dfs(heights, visited, i, j + 1, m, n);
        }
    }
};