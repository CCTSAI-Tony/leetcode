// 刷題用這個, time complexity O(V+E), space complexity O(V+E)
class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        unordered_map<int, vector<int>> graph;
        for (auto edge: edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        vector<int> visited(n, 0);
        if (!dfs(0, -1, graph, visited)) {
            return false;
        }
        if (count(visited.begin(), visited.end(), 1) != n) {
            return false;
        }
        return true;
    }

    bool dfs(int i, int parent, unordered_map<int, vector<int>>& graph, vector<int>& visited) {
        visited[i] = 1;
        for (auto nbr: graph[i]) {
            if (visited[nbr] == 0) {
                if (!dfs(nbr, i, graph, visited)) {
                    return false;
                }
            }
            else if (nbr != parent) {
                return false;
            }
        }
        return true;
    }
};
