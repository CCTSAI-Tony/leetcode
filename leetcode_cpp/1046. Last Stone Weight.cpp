class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int, vector<int>, greater<int>> pq;
        for (auto stone: stones) pq.push(-stone);
        while (!pq.empty()) {
            int s1 = pq.top();
            pq.pop();
            if (pq.empty()) return -s1;
            int s2 = pq.top();
            pq.pop();
            if (s1 == s2) continue;
            pq.push(s1-s2);
        }
        return 0;
    }
};

