// min heap
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        typedef tuple<int, int, int> PII;
        priority_queue<PII, vector<PII>, greater<PII>> pq;
        vector<vector<int>> res(k);
        for (auto& point: points) {
            int dist = -(point[0]*point[0] + point[1]*point[1]);
            if (pq.size() == k) {
                pq.push(make_tuple(dist, point[0], point[1]));
                pq.pop();
            }
            else pq.push(make_tuple(dist, point[0], point[1]));
        }
        
        for (auto i = 0; i < k; i++) {  // 切記, 不能用 for (auto& item: pq), priority queue 不能直接遍歷
            tuple<int, int, int> top = pq.top();
            pq.pop();
            res[i] = {get<1>(top), get<2>(top)};
        }
        return res;
    }
};

// max heap
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<vector<int>> maxHeap;
        for (auto& p : points) {
            int x = p[0], y = p[1];
            maxHeap.push({x*x + y*y, x, y});
            if (maxHeap.size() > k) {
                maxHeap.pop();
            }
        }
        vector<vector<int>> ans(k);
        for (int i = 0; i < k; ++i) {
            vector<int> top = maxHeap.top();
            maxHeap.pop();
            ans[i] = {top[1], top[2]};
        }
        return ans;
    }
};
