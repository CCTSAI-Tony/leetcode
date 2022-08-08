#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> v;
        unordered_map<int,int> m;
        for(int i=0;i<nums.size();++i)
        {
            if(m.find(target-nums[i])!=m.end())
            {   
                v.push_back(m[target-nums[i]]);
                v.push_back(i);
                return v;
            }
            else
                m[nums[i]]=i;
        }
       return v;
        
    }
};

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> v;
        unordered_map<int,int> m;
        for(size_t i=0;i<nums.size();++i)
        {
            if(m.find(target-nums[i])!=m.end())
            {
                v.push_back(m[target-nums[i]]);
                v.push_back(i);
                return v;
            }
            else
                m[nums[i]]=i;
        }
       return v;
        
    }
};

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> v;
        unordered_map<int,int> m;
        for(auto i=0;i<nums.size();++i)
        {
            if(m.find(target-nums[i])!=m.end())
            {
                v.push_back(m[target-nums[i]]);
                v.push_back(i);
                return v;
            }
            else
                m[nums[i]]=i;
        }
       return v;
        
    }
};


#include <array>

int main()
{
    
    std::array<std::size_t, 10> a;
 
    // Example with C++23 size_t literal
    for (auto i = 0; i != a.size(); ++i)
        std::cout << (a[i] = i) << ' ';
    std::cout << '\n';
    
    // Example of decrementing loop
    for (std::size_t i = a.size(); --i;)  //do --i first, no third argument, and we can use auto also
        std::cout << a[i] << ' ';
 
    // Note the naive decrementing loop:
    //  for (std::size_t i = a.size() - 1; i >= 0; --i) ...
    // is an infinite loop, because unsigned numbers are always non-negative

    return 0;
}
