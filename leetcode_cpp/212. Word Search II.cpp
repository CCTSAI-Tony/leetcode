// 刷題用這個 498ms
class Trie {
    public:
        string word = ""; //本題技巧
        Trie* children[26] = {};
        Trie() {}
    };

class Solution {
public:
    Trie* buildTrie(const vector<string>& words) {
        Trie* root = new Trie();
        for (const string& word : words) {
            Trie* iter = root;
            for (int i = 0; i < word.size(); i++) {
                if (!iter->children[word[i] - 'a'])
                    iter->children[word[i] - 'a'] = new Trie();
                iter = iter->children[word[i] - 'a'];
            }
            iter->word = word;
        }
        return root;
    }

    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        vector<string> res;
        Trie* root = buildTrie(words);
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                dfs(board, root, i, j, res);
            }
        }
        return res;
    }

    void dfs(vector<vector<char>>& board, Trie* node, int i, int j, vector<string>& res) {
        char c = board[i][j];
        if (c == '#') return;
        Trie* next = node->children[c - 'a']; // 提早減枝
        if (next) {
            if (next->word != "") {
                res.push_back(next->word);
                next->word = "";
            }
            board[i][j] = '#';
            if (i > 0) dfs(board, next, i - 1, j, res);
            if (j > 0) dfs(board, next, i, j - 1, res);
            if (i < board.size() - 1) dfs(board, next, i + 1, j, res);
            if (j < board[0].size() - 1) dfs(board, next, i, j + 1, res);
            board[i][j] = c;
        }
    }
};

// 自己重寫, 參照python 2103ms
class Trie {
public:
    Trie* children[26] = {};
    string word_path = "";
    
    Trie() {
    }
    
    ~Trie() {
        for (auto child: children) delete child;
    }

    void insert(string word) {
        Trie* cur = this;
        for (char c : word) {
            c -= 'a';
            if (cur->children[c] == nullptr)
                cur->children[c] = new Trie();
            cur = cur->children[c];
        }
        cur->word_path = word;
    }
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        vector<string> res;
        Trie* trie = new Trie();
        for (auto word: words) trie->insert(word);
        for (auto i=0; i<board.size(); i++) {
            for (auto j=0; j<board[0].size(); j++) dfs(trie, board, i, j, res);
        }
        return res;
    }
    
    void dfs(Trie* node, vector<vector<char>>& board, int i, int j, vector<string>& res) {
        if (node->word_path != "") {
            res.push_back(node->word_path);
            node->word_path = "";
        }
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] == '#') return; //慢
        char c = board[i][j];
        node = node->children[c-'a'];
        if (node == nullptr) return;
        board[i][j] = '#';
        dfs(node, board, i-1, j, res);
        dfs(node, board, i, j-1, res);
        dfs(node, board, i+1, j, res);
        dfs(node, board, i, j+1, res);
        board[i][j] = c;
    }
};

