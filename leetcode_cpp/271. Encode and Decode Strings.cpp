// A char (1 byte) is able to hold the character count of a string (max length is 200).
// 思路: 先計算string 長度, 之後decode時會用到
class Codec {
public:
    string encode(vector<string>& strs) {
        std::string ans;
        for (unsigned i=0; i<strs.size(); ++i) {
            ans += strs[i].size();  // Character count for string bytes, 重要!! 這個num 不會被cout print 出來 只有空格, 但我們要拿這個來decode 用
            ans += strs[i];
        }
        return ans;
    }

    vector<string> decode(string s) {
        std::vector<std::string> ans;
        unsigned i = 0;
        while (i < s.size()) {
            uint8_t cnt = s[i++];  // Use an unsigned byte to preserve the data pattern.
            ans.emplace_back(); // add 空字串
            while (cnt--) {
                ans.back() += s[i++]; // string 加字, ans.back() 給的是最後一個string item
            }
        }
        return ans;        
    }
};

// 重寫第二次, time complexity O(n)
class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string ans;
        for (int i = 0; i < strs.size(); i++){
            ans += strs[i].size();
            ans += strs[i];
        }
        return ans;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> res;
        int i {0};
        while (i < s.size()){
            uint8_t cnt {static_cast<uint8_t>(s[i++])}; // 不能用 uint16_t, or int => 2 or 4 bytes => get heap buffer overflow error
            res.emplace_back();
            while (cnt--){
                res.back() += s[i++];
            }  
        }
        return res;
    }
};

// 為什麼不能用 uint16_t, or int, 因為encode string 是1 byte singed char string, 超過127字符的字串會自動變成負數, 若decode 時沒有轉成正數就會報錯
// 使用unit8_t 轉換, 不能用unit16_t 這個是針對 2 byte signed integer 才有用
// ex: 158 => -98

// A heap buffer overflow is when you access outside an array that was allocated on the heap (i.e. using malloc()).

// The root cause of the heap-buffer-overflow problem is that you program visits the heap memory which is out of index.

// How many bytes is a char in C++? 1 byte

// Cause I use uint16_t(2 byte type) to catch the 1 byte val => lead to unexpected error

// When vectors are allocated, do they use memory on the heap or the stack?

// No, vect will be on the stack, but the array it uses internally to store the items will be on the heap. The items will reside in that array.


// While storing here ans += strs[i].size();

// why did we not have to convert the size to uint8_t ?


// ans: The data is always saved as a signed byte while encoding, because std::string consists of signed chars.
// It's only in the decoding that we need to interpret it as an unsigned byte, otherwise cnt could be negative.

// What is the differnce between UInt8 and uint8_t, or UInt16 and unit16_t?

// What does the _t imply?

// In C99 the available basic integer types (the ones without _t) were deemed insufficient, because their actual sizes may vary across different systems.

// So, the C99 standard includes definitions of several new integer types to enhance the portability of programs. The new types are especially useful in embedded environments.

// All of the new types are suffixed with a _t and are guaranteed to be defined uniformly across all systems.