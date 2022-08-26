class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int N = 9;
        unordered_set<char> rowSet[N]; // 這裡用到c style array
        unordered_set<char> colSet[N];
        unordered_set<char> squareSet[N];
        
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                char val = board[r][c];
                if (val == '.') continue;
                int sPos = (r / 3) * 3 + c / 3; // 技巧
                if (rowSet[r].count(val) || colSet[c].count(val) || squareSet[sPos].count(val))
                    return false;
                rowSet[r].insert(val); // set 只能用insert
                colSet[c].insert(val);
                squareSet[sPos].insert(val);
            }
        }
        return true;
    }
};

// 重寫第二次, time complexity O(49)
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n {9};
        unordered_set<char> row[n];
        unordered_set<char> col[n];
        unordered_set<char> block[n];
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if (board[i][j] == '.') continue;
                char val = board[i][j];
                int pos = (i / 3) * 3 + (j / 3);
                if (row[i].count(val) || col[j].count(val) || block[pos].count(val)) return false;
                row[i].insert(val);
                col[j].insert(val);
                block[pos].insert(val);
            }
        }
        return true;
    }
};