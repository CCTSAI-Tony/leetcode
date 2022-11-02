class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = *max_element(piles.begin(), piles.end());  // 好招, 學起來!
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (check(piles, h, mid)) r = mid;
            else l = mid;
        }
        if (check(piles, h, l)) return l;
        return r;
    }
    
    bool check(vector<int>& piles, int h, int mid) {
        int res {0};
        for (auto pile: piles) {
            res += ceil((double) pile / mid);  // 不能用float, 精確度問題
        }
        return res <= h;
    }
};

// Many of the answers posted use the ceil library function to round up. However, depending on the floating point representation and the inputs, you could end up with the wrong answer. 
// I instead use an integer rounding trick I learned from programming in CUDA. Basically, 
// if you want to calculate ceil(x/y), where x and y are integers, and you want an integer result, you can simply write (x + y - 1)/y. 
//     The intuition is that / is integer division: you divide x by y and follow that operation by an integer floor operation. 
// Thus, 3 / 2 = (int)floor(1.5) = 1, but we want a result of 2. 
// With the alternate equation, (3 + 2 - 1) / 2 = (int) floor(4/2) = 2, which is what we want. If you do a quick check with other values, you'll see that the identity holds.

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = *max_element(piles.begin(), piles.end());
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (check(piles, h, mid)) r = mid;
            else l = mid;
        }
        if (check(piles, h, l)) return l;
        return r;
    }
    
    bool check(vector<int>& piles, int h, int mid) {
        int res {0};
        for (auto pile: piles) {
            res += (pile + mid - 1) / mid;
        }
        return res <= h;
    }
};

