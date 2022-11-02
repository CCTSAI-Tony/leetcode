class Trie {
public:
    Trie* children[26] = {};
    bool isWord = false;
    
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
        cur->isWord = true;
    }
    
    bool search(string word) {
        Trie* cur = this;
        for (char c : word) {
            c -= 'a';
            if (cur->children[c] == nullptr) return false;
            cur = cur->children[c];
        }
        return cur->isWord;
    }
    
    bool startsWith(string prefix) {
        Trie* cur = this;
        for (char c : prefix) {
            c -= 'a';
            if (cur->children[c] == nullptr) return false;
            cur = cur->children[c];
        }
        return true;
    }
};

// trienode unordered_map version
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

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    void insert(const string & word) {
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
        curr->m_is_end = true;//means one word end here
    }

    // Returns if the word is in the trie.
    bool search(const string & word) const {
        TrieNode* curr = find_root_node_with_prefix(word);
        if(!curr) return false;
        return curr->m_is_end == true;//one word end here or not
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    bool startsWith(const string & prefix) const {
        TrieNode* curr = find_root_node_with_prefix(prefix);
        return curr == nullptr ? false : true;
    }
    //destructor
    ~Trie() {delete root;}
protected:
    // return the root node of a prefix
    TrieNode* find_root_node_with_prefix(string prefix) const{
        TrieNode* curr = root;
        for (auto ch : prefix) {
            curr = curr->find_child(ch);
            if (curr == nullptr)
                return nullptr;
        }
        return curr;
    }
private:
    TrieNode* root;
};

// trienode vector version
class TrieNode {
public:
    // Initialize your data structure here.
    TrieNode(const char c) : m_char(c),m_is_end(false){}
    TrieNode():TrieNode(' '){}
    TrieNode* find_child(const char c) const{
        for(TrieNode* child: m_children){
            if(child->m_char == c) return child;
        }
        return nullptr;
    }
    ~TrieNode(){
        for(TrieNode* child: m_children) delete child;
    }
    char m_char;
    bool m_is_end;
    vector<TrieNode*> m_children;
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    void insert(const string & word) {
        TrieNode* curr = root;
        for (auto ch : word) {
            TrieNode* child = curr->find_child(ch);
            if (child != nullptr) {
                curr = child;
            } else {
                TrieNode *newNode = new TrieNode(ch);
                curr->m_children.push_back(newNode);
                curr = newNode;
            }
        }
        curr->m_is_end = true;//means one word end here
    }

    // Returns if the word is in the trie.
    bool search(const string & word) const {
        TrieNode* curr = find_root_node_with_prefix(word);
        if(!curr) return false;
        return curr->m_is_end == true;//one word end here or not
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    bool startsWith(const string & prefix) const {
        TrieNode* curr = find_root_node_with_prefix(prefix);
        return curr == nullptr ? false : true;
    }
    //destructor
    ~Trie() {delete root;}
protected:
    // return the root node of a prefix
    TrieNode* find_root_node_with_prefix(string prefix) const{
        TrieNode* curr = root;
        for (auto ch : prefix) {
            curr = curr->find_child(ch);
            if (curr == nullptr)
                return nullptr;
        }
        return curr;
    }
private:
    TrieNode* root;
};


