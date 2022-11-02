// array solution, 刷題用這個, 954ms
class WordDictionary {
public:
    WordDictionary* children[26] = {};
    bool isWord = false;
    bool res = false;
    WordDictionary() {
        
    }
    ~WordDictionary(){
        for(auto child: children) delete child;
    }

    void addWord(string word) {
        WordDictionary* cur = this;
        for (char c : word) {
            c -= 'a';
            if (cur->children[c] == nullptr)
                cur->children[c] = new  WordDictionary();
            cur = cur->children[c];
        }
        cur->isWord = true;
    }
    
    bool search(string word) {
        WordDictionary* cur = this;
        res = false;
        int word_size = word.size();
        dfs(cur, word, word_size, 0);
        return res;
    }
    
    void dfs(WordDictionary* node, string& word, int& word_size, int idx) {
        if (idx == word_size) {
            if (node->isWord) res = true;
            return;
        }
        if (word[idx] == '.') {
            for (auto child: node->children) {
                if (child != nullptr) dfs(child, word, word_size, idx+1);
            }
        }
        else {
            char c = word[idx];
            c -= 'a';
            node = node->children[c];
            if (node == nullptr) return;
            dfs(node, word, word_size, idx+1);
        }
    }
};

// TrieNode solution, tle
class TrieNode {
public:
    // Initialize your data structure here.
    char m_char;
    bool m_is_end;
    unordered_map<char, TrieNode*> m_children;
    TrieNode(const char c) : m_char(c),m_is_end(false){}
    TrieNode():TrieNode(' '){}
    TrieNode* find_child(const char c) {
        if (m_children.find(c) != m_children.end()) return m_children[c];
        return nullptr;
    }
    ~TrieNode(){
        for(auto child: m_children) delete child.second;
    }
};

class WordDictionary {
public:
    TrieNode* root;
    bool res = false;
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* curr = root;
        for (auto ch : word) {
            TrieNode* child = curr->find_child(ch);
            if (child != nullptr) {
                curr = child;
            } else {
                TrieNode* newNode = new TrieNode(ch);
                curr->m_children[ch] = newNode;
                curr = newNode;
            }
        }
        curr->m_is_end = true;
    }
    
    bool search(string word) {
        TrieNode* node = root;
        res = false;
        int word_size = word.size();
        dfs(node, word, word_size, 0);
        return res;
    }
    
    void dfs(TrieNode* node, string& word, int word_size, int idx) {
        if (idx == word_size) {
            if (node->m_is_end) res = true;
            return;
        }
        if (word[idx] == '.') {
            for (auto child: node->m_children) {
                dfs(child.second, word, word_size, idx+1);
            }
        }
        else {
            node = node->find_child(word[idx]);
            if (node == nullptr) return;
            dfs(node, word, word_size, idx+1);
        }
    }
};

