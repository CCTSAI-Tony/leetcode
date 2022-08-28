class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res;
        int l(0), r(numbers.size() - 1);
        while (l < r){
            int temp {numbers[l] + numbers[r]};
            if (temp < target) l++;
            else if(temp > target) r--;
            else{
                res.push_back(l+1);
                res.push_back(r+1);
                return res;
            }
        }
        return res;
    }
};



class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res;
        int l {0}, r {static_cast<int>(numbers.size()) - 1};
        while (l < r){
            int temp {numbers[l] + numbers[r]};
            if (temp < target) l++;
            else if(temp > target) r--;
            else{
                res.push_back(l+1);
                res.push_back(r+1);
                return res;
            }
        }
        return res;
    }
};


// https://stackoverflow.com/questions/60368422/non-constant-expression-cannot-be-narrowed-from-type-int-to-unsigned-long-lon

// When you use brace-initialization, it is forbidden for a narrowing conversion to be used to convert from the type of the value in the braced list to the type that the constructor actually requires. 
// heights[0].size()-1 has type size_t, and the constructor of std::vector<int> takes std::initializer_list<int>. Usually, int cannot represent all values of type size_t, 
// which means that size_t to int is a narrowing conversion. You can fix this using an explicit cast:

// dq.push_back({i,static_cast<int>(heights[0].size()-1)});
// When the type being constructed is std::pair<int, int>, it is a different story. No conversion actually occurs when calling the constructor; instead, the following constructor is called:

// template< class U1, class U2 >
// constexpr pair( U1&& x, U2&& y );

// Internally, presumably in the constructor initializer list, the constructor will convert size_t to int, but this will not be done inside braces, so it's legal.












