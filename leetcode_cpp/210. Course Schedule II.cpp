// 刷題用這個, dfs
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> graph;
        vector<int> visited(numCourses, -1);
        vector<int> res;
        for (auto pair: prerequisites) {
            graph[pair[1]].push_back(pair[0]);
        }
        for (int i=0; i<numCourses; i++) {
            if (!dfs(i, graph, visited, res)) return {};
        }
        reverse(res.begin(), res.end());
        return res;
    }

    bool dfs(int i, unordered_map<int, vector<int>>& graph, vector<int>& visited, vector<int>& res) {
        if (visited[i] == 1) return true;
        else if (visited[i] == 0) return false;
        visited[i] = 0;
        for (auto course: graph[i]) {
            if (!dfs(course, graph, visited, res)) return false;
        }
        visited[i] = 1;
        res.push_back(i);
        return true;
    }
};

// 刷題用這個, bfs
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, int> in_degree;
        unordered_map<int, vector<int>> graph;
        vector<int> res;
        queue<int> que;
        for (auto prerequisite: prerequisites) {
            int cur, pre;
            cur = prerequisite[0];
            pre = prerequisite[1];
            graph[pre].push_back(cur);
            in_degree[cur]++;
        }
        for (int course=0; course<numCourses; course++) {
            if (in_degree[course] == 0) {
                que.push(course);
                in_degree.erase(course);
            }
        }
        while (!que.empty()) {
            int que_size = que.size();
            for (int q=0; q<que_size; q++) {
                int cur = que.front();
                que.pop();
                for (auto nxt: graph[cur]) {
                    in_degree[nxt]--;
                    if (in_degree[nxt] == 0) {
                        que.push(nxt);
                        in_degree.erase(nxt);
                    }
                }
                res.push_back(cur);
            }
        }
        if (res.size() != numCourses) {
            return {};
        }
        else {
            return res;
        }
    }
};

