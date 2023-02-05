/*
    Given grid where '1' is land & '0' is water, return # of islands

    DFS, set visited land to '0' to not visit it again, count islands

    Time: O(m x n)
    Space: O(m x n)
*/

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        int result = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j, m, n);
                    result++;
                }
            }
        }
        
        return result;
    }
private:
    void dfs(vector<vector<char>>& grid, int i, int j, int m, int n) {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0') {
            return;
        }
        grid[i][j] = '0';
        
        dfs(grid, i - 1, j, m, n);
        dfs(grid, i + 1, j, m, n);
        dfs(grid, i, j - 1, m, n);
        dfs(grid, i, j + 1, m, n);
    }
};

// 重寫第二次
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int count {0};
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == '1') {
                    dfs(i, j, m, n, grid);
                    count++;
                }
            }
        }
        return count;
    }

    void dfs(int i, int j, int m, int n, vector<vector<char>>& grid) {
        if (i>=0 && i<m && j>=0 && j<n && grid[i][j] == '1') {
            grid[i][j] = '0';
            dfs(i+1, j, m, n, grid);
            dfs(i-1, j, m, n, grid);
            dfs(i, j+1, m, n, grid);
            dfs(i, j-1, m, n, grid);
        }
    }
};
