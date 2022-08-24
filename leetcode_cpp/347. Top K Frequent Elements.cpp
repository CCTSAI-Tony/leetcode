// time complexity O(klogn)
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> map;
        for(int num : nums){
            map[num]++;
        }
        
        vector<int> res;
        // pair<first, second>: first is frequency,  second is number
        priority_queue<pair<int,int>> pq; 
        for(auto it = map.begin(); it != map.end(); it++){ //use iterator
            pq.push(make_pair(it->second, it->first)); //can use make_tuple to include more than two items
            if(pq.size() > (int)map.size() - k){
                res.push_back(pq.top().second);
                pq.pop();
            }
        }
        return res;
    }
};


//刷題用這個, 使用tuple
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res;
        unordered_map<int, int> map;
        for (auto num: nums){
            map[num]++;
        }
        priority_queue<tuple<int, int>> pq;
        for (auto item: map){
            pq.push(make_tuple(item.second, item.first));
            if (pq.size() > (map.size() - k)){
                int count;
                int num;
                tie(count, num) = pq.top();
                res.push_back(num);
                pq.pop();
                
            }
        }
        return res;
        
    }
};