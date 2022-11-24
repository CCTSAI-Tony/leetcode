// 刷題用這個, 參照python 解法
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> counts;
        for (auto t: tasks) counts[t]++;
        priority_queue<pair<int, char>> pq;
        for (auto count: counts) pq.push(make_pair(count.second, count.first));
        int total_interval = 0;
        while (!pq.empty()) {
            int period = 0;
            vector<pair<int, char>> temp;
            while ((!pq.empty() || !temp.empty()) and period < n + 1) {
                total_interval++;
                period++;
                if (!pq.empty()) {
                    pair<int, char> item = pq.top();
                    pq.pop();
                    if (item.first != 1) temp.push_back(make_pair(item.first-1, item.second));
                }
            }
            for (auto item: temp) pq.push(item);
        }
        return total_interval;
    }
};


class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> counts;
        for (char t : tasks) {
            counts[t]++;
        }
        priority_queue<pair<int, char>> pq;
        for (pair<char, int> count : counts) {
            pq.push(make_pair(count.second, count.first));
        }
        int alltime = 0;
        int cycle = n + 1;
        while (!pq.empty()) {
            int time = 0;
            vector<pair<int, char>> tmp;
            for (int i = 0; i < cycle; i++) {
                if (!pq.empty()) {
                    tmp.push_back(pq.top());
                    pq.pop();
                    time++;
                }
            }
            for (auto t : tmp) {
                if (--t.first) {
                    pq.push(t);
                }
            }
            alltime += !pq.empty() ? cycle : time;
        }
        return alltime;
    }
};

