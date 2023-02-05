// 刷題用這個
/*
    Given undirected graph, return an edge that can be removed to make a tree
    Ex. edges = [[1,2],[1,3],[2,3]] -> [2,3]

    If n nodes & n edges, guaranteed a cycle
    How to know creating cycle? When connecting a node already connected
    Union Find: can find this redundant edge, track parents & ranks

    Time: O(n)
    Space: O(n)
*/

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        
        vector<int> parents;
        vector<int> ranks;
        for (int i = 0; i < n + 1; i++) {
            parents.push_back(i);
            ranks.push_back(1);
            
        }
        
        vector<int> result;
        for (int i = 0; i < n; i++) {
            int n1 = edges[i][0];
            int n2 = edges[i][1];
            if (!doUnion(parents, ranks, n1, n2)) {
                result = {n1, n2};
                break;
            }
        }
        return result;
    }
private:
    int doFind(vector<int>& parents, int n) {
        int p = parents[n];
        while (p != parents[p]) {
            parents[p] = parents[parents[p]];
            p = parents[p];
        }
        return p;
    }
    
    bool doUnion(vector<int>& parents, vector<int>& ranks, int n1, int n2) {
        int p1 = doFind(parents, n1);
        int p2 = doFind(parents, n2);
        if (p1 == p2) {
            return false;
        }
        
        if (ranks[p1] > ranks[p2]) {
            parents[p2] = p1;
            ranks[p1] += ranks[p2];
        } else {
            parents[p1] = p2;
            ranks[p2] += ranks[p1];
        }
        
        return true;
    }
};

// 自己重寫, time complexity O(n), union find without Union by Rank and but use Path Compression
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        vector<int> parent((int) edges.size() + 1, 0);
        for (auto edge: edges) {
            if (!union_search(edge[0], edge[1], parent)) {
                return edge;
            }
        }
        return {};
    }

    bool union_search(int x, int y, vector<int>& parent) {
        int root_x = find(x, parent);
        int root_y = find(y, parent);
        if (root_x == root_y) {
            return false;
        }
        parent[root_x] = root_y;
        return true;
    }

    int find(int x, vector<int>& parent) {
        if (parent[x] == 0) {
            return x;
        }
        parent[x] = find(parent[x], parent);
        return parent[x];
    }
};

