// 刷題用這個, c++ 沒有 for else loop, time complexity O(c), space complexity O(u + min(u^2, n)), 
class Solution {
public:
    string alienOrder(vector<string>& words) {
        unordered_map<char, unordered_set<char>> adj_list;
        unordered_map<char, int> in_degree;
        for (auto word: words) {
            for (auto c: word) {
                in_degree[c] = 0;
            }
        }
        int n = words.size();
        for (int i=0; i<n-1; i++) {
            string first_word = words[i];
            string second_word = words[i+1];
            int l = min((int) first_word.size(), (int) second_word.size());
            int flag = 0; // c++ 沒有 for else loop
            for (int j=0; j<l; j++) {
                char c = first_word[j];
                char d = second_word[j];
                if (c != d) {
                    if (adj_list[c].find(d) == adj_list[c].end()) {
                        adj_list[c].insert(d);
                        in_degree[d]++;
                    }
                    flag = 1;
                    break;
                }
            }
            if (!flag) {
                if ((int) first_word.size() > (int) second_word.size()) {
                    return "";
                }
            }
        }
        string output;
        queue<char> q;
        unordered_map<char, int>::iterator it = in_degree.begin();
        while (it != in_degree.end()) {
            if (it->second == 0) {
                q.push(it->first);
            }
            it++;
        }
        while (!q.empty()) {
            char c = q.front();
            q.pop();
            output += c;
            for (auto d: adj_list[c]) {
                in_degree[d]--;
                if (in_degree[d] == 0) {
                    q.push(d);
                }
            }
        }
        return output.size() == in_degree.size() ? output : "";
    }
};




#include<iostream>
#include<map>
#include<vector>
#include<queue>
using namespace std;

class Solution {
public:
    string alienOrder(vector<string>& words) {
        map<char,int> degree;
        map<char, vector<char>> graph;
        int n = words.size();

        for (auto& word : words) {
            for (auto& ch : word) {
                degree[ch] = 0;
        }

        for (int i = 0; i < n - 1; i++) {
         int l = min((int)words[i].size(), (int)words[i + 1].size());
         for (int j = 0; j < l; j++) {
            char x = words[i][j];
            char y = words[i + 1][j];
            if (x != y) {
               graph[x].push_back(y);
               degree[y]++;
               break;
            }
         }
      }
      
      string ret = "";
      queue<char> q;
      map<char, int>::iterator it = degree.begin();
      while (it != degree.end()) {
         if (it->second == 0) {
            q.push(it->first);
         }
         it++;
      }

      while (!q.empty()) {
         char x = q.front();
         q.pop();
         ret += x;
         vector<char>::iterator sit = graph[x].begin();
         while (sit != graph[x].end()) {
            degree[*sit]--;
            if (degree[*sit] == 0) {
               q.push(*sit);
            }
            sit++;
         }
      }
      return ret.size() == degree.size() ? ret : "";
      }
    }
};
