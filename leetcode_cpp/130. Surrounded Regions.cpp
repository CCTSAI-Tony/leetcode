// 刷題用這個, time complexity O(mn), space complexity O(mn)
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int m = board.size();
        int n = board[0].size();
        queue<pair<int, int>> q;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (((i == 0 || i == m-1) || (j == 0 || j == n-1)) && board[i][j] == 'O') {
                    q.push({i, j});
                }
            }
        }
        while (!q.empty()) {
            int q_size = q.size();
            for (int _=0; _<q_size; _++) {
                int r, c;
                tie(r, c) = q.front();
                q.pop();
                if (r>=0 && r<m && c>=0 && c<n && board[r][c] == 'O') {
                    board[r][c] = 'D';
                    q.push({r+1, c});
                    q.push({r-1, c});
                    q.push({r, c+1});
                    q.push({r, c-1});
                }
            } 
        }
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (board[i][j] == 'D') {
                    board[i][j] = 'O';
                }
                else if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
            }
        }
    }
};