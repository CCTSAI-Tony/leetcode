/*
    Given airline tickets, find valid itinerary (use all tickets once)
    Ex. tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
        output = ["JFK","MUC","LHR","SFO","SJC"]

    Greedy DFS, build route backwards when retreating, merge cycles into main path

    Time: O(E log (E / V)) -> E = # of flights, V = # of airports, sorting
    Space: O(V + E) -> store # of airports & # of flights in hash map
*/

// 刷題用這個
// multiset https://www.geeksforgeeks.org/multiset-in-cpp-stl/
// Also set/ multiset is sorted so it gets sorted in lexical order itself
// insert ordering: 字母排序小的放後面 ex: 60 50 50 40 30 20 10,
// 但 reassign a new multiset from old one => multiset<int> gquiz2(gquiz1.begin(), gquiz1.end());
// order will be => 10 20 30 40 50 50 60 
class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, multiset<string>> m;
        for (int i = 0; i < tickets.size(); i++) {
            m[tickets[i][0]].insert(tickets[i][1]);
        }
        
        vector<string> result;
        dfs(m, "JFK", result);
        reverse(result.begin(), result.end());
        return result;
    }
private:
    void dfs(unordered_map<string, multiset<string>>& m,
        string airport, vector<string>& result) {
        
        while (!m[airport].empty()) {
            string next = *m[airport].begin(); // dereferen interator
            m[airport].erase(m[airport].begin()); // only erase one element that irerator points to, move it to the next
            dfs(m, next, result);
        }
        
        result.push_back(airport);
    }
};

// Python 解法, time complexity O(nlogn), space complexity O(n)
class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, vector<string>> m;
        for (auto ticket: tickets) {
            m[ticket[0]].push_back(ticket[1]);
        }
        for (auto &item: m) {
            sort(item.second.begin(), item.second.end(), greater<string>()); // reverse sort
        }

        vector<string> res;
        dfs("JFK", m, res);
        reverse(res.begin(), res.end());
        return res;
    }

    void dfs(string start, unordered_map<string, vector<string>>& m, vector<string>& res) {
        while (!m[start].empty()) {
            string nxt = m[start].back();
            m[start].pop_back();
            dfs(nxt, m, res);
        }
        res.push_back(start);
    }
};
