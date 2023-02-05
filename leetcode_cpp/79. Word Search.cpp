// 刷題用這個 time complexity O(mn*3^l), l: len of word, space complexity O(l), 刷題用這個, backtracking
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m, n;
        if (board.empty()) return false;
        m = (int) board.size();
        n = (int) board[0].size();
        vector<pair<int, int>> direcs {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};
        for (int i=0; i<m;i++) {
            for (int j=0; j<n;j++) {
                if (board[i][j] == word[0] && dfs(board, word, i, j, 0, direcs)) return true;
            }
        }
        return false;
    }

    bool dfs(vector<vector<char>>& board, string& word, int i, int j, int index, vector<pair<int, int>>& direcs) {
        if (index == word.size() - 1) return true;
        int m, n;
        m = (int) board.size();
        n = (int) board[0].size();
        char temp = board[i][j];
        board[i][j] = '#';
        for (auto d: direcs) {
            int x, y;
            x = i + d.first;
            y = j + d.second;
            if (0 <= x && x < m && 0 <= y && y < n && board[x][y] == word[index+1]) {
                if (dfs(board, word, x, y, index+1, direcs)) return true;
            }
        }
        board[i][j] = temp;
        return false;
    }
};


class   Solution
{
    public:

    bool    exist(vector<vector<char>>& board, string word)
    {
            int     rows, cols;

            if (!board.size()) return (false);
            rows = (int) board.size();
            cols = (int) board[0].size();
            for (int i = 0; i < rows; i++)
                for (int j = 0; j < cols; j++)
                    if (dfs(board, word, 0, i, j))
                return (true);
            return (false);
    }

    bool    dfs(vector<vector<char>> &board, string &word, int i, int x, int y)
    {
            int     rows, cols;
            bool    found;
            char    c;

            if (!board.size())
            return (false);
            rows = (int) board.size();
            cols = (int) board[0].size();
            if (x < 0 || x == rows || y < 0 || y == cols || word[i] != board[x][y])
                return (false);
            if (i == (int) word.length() - 1)
                return (true);
            c = board[x][y];
            board[x][y] = 0;
            found = dfs(board, word, i + 1, x + 1, y) ||
                    dfs(board, word, i + 1, x - 1, y) ||
                    dfs(board, word, i + 1, x, y + 1) ||
                    dfs(board, word, i + 1, x, y - 1);
            board[x][y] = c;
            return (found);
    }
};