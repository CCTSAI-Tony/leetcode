//tle
class TimeMap {
public:
    unordered_map<string, vector<pair<string, int>>> memo;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        memo[key].emplace_back(make_pair(value, timestamp));
    }
    
    string get(string key, int timestamp) {
        if (memo.find(key) == memo.end()) return "";
        vector<pair<string, int>> array = memo[key];
        int l = 0, r = array.size() - 1;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (array[mid].second > timestamp) r = mid;
            else l = mid;
        }
        if (array[l].second > timestamp) return "";
        else if (array[r].second > timestamp) return array[l].first;
        else return array[r].first;
    }
};

// tle
class TimeMap {
public:
    unordered_map<string, vector<pair<string, int>>> memo;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        memo[key].push_back({value, timestamp});
    }
    
    string get(string key, int timestamp) {
        if (!memo.count(key)) return "";
        vector<pair<string, int>> array = memo[key];
        int l = 0, r = array.size() - 1;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (array[mid].second > timestamp) r = mid;
            else l = mid;
        }
        if (array[l].second > timestamp) return "";
        else if (array[r].second > timestamp) return array[l].first;
        else return array[r].first;
    }
};

// map lower bound
https://www.geeksforgeeks.org/map-lower_bound-function-in-c-stl/
//685ms, 利用map lowerbound 來得到答案, 比binary search 快, 紅黑樹
class TimeMap {
public:
   /** Initialize your data structure here. */
   unordered_map<string, map<int, string>> m;

   TimeMap() {}

   void set(string key, string value, int timestamp) {
      auto& inner_map = m[key];
      inner_map[-timestamp] = value;
   }

   string get(string key, int timestamp) {
      auto i = m.find(key);
      if (i == m.end()) return "";
      auto j = i->second.lower_bound(-timestamp);
      return j != i->second.end() ? j->second : "";
   }
};


// Syntax: map_name.lower_bound(key)
class TimeMap {
public:
    unordered_map<string, map<int, string, greater<>>> m;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        auto& inner_map = m[key];
        inner_map[timestamp] = value;
    }
    
    string get(string key, int timestamp) {
        auto i = m.find(key);
        if (i == m.end()) return "";
        auto j = i->second.lower_bound(timestamp);
        return j != i->second.end() ? j->second : "";
    }
};


