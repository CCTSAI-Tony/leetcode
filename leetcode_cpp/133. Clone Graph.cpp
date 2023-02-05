/*
    Given ref of a node in connected undirected graph, return deep copy

    Both BFS & DFS work, map original node to its copy

    Time: O(m + n)
    Space: O(n)
*/

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

//dfs
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == NULL) {
            return NULL;
        } 
        if (m.find(node) == m.end()) {
            m[node] = new Node(node->val);
            for (int i = 0; i < node->neighbors.size(); i++) {
                Node* neighbor = node->neighbors[i];
                m[node]->neighbors.push_back(cloneGraph(neighbor));
            }
        }
        return m[node];
    }
private:
    unordered_map<Node*, Node*> m;
};

// bfs
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == NULL) {
            return NULL;
        }
        
        Node* copy = new Node(node->val);
        m[node] = copy;
        
        queue<Node*> q;
        q.push(node);
        
        while (!q.empty()) {
            Node* curr = q.front();
            q.pop(); //pop the first item
            
            for (int i = 0; i < curr->neighbors.size(); i++) {
                Node* neighbor = curr->neighbors[i];
                
                if (m.find(neighbor) == m.end()) {
                    m[neighbor] = new Node(neighbor->val);
                    q.push(neighbor);
                }
                
                m[curr]->neighbors.push_back(m[neighbor]);
            }
        }
        
        return copy;
    }
private:
    unordered_map<Node*, Node*> m;
};

// 重寫第二次
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == NULL) return NULL;
        queue<Node*> q;
        Node* copy = new Node(node->val);
        map[node] = copy;
        q.push(node);
        while (!q.empty()) {
            Node* cur = q.front();
            q.pop();
            for (auto c: cur->neighbors) {
                if (map.find(c) == map.end()) {
                    map[c] = new Node(c->val);
                    q.push(c);
                }
                map[cur]->neighbors.push_back(map[c]);
            }
        }
        return copy;
    }

private:
    unordered_map<Node*, Node*> map;


};
