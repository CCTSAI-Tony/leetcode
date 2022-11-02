// 刷題用這個
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            vector<int> temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }
        int m = nums1.size(), n = nums2.size();
        int half_len = (m + n + 1) / 2;
        int imin = 0, imax = m;
        while (imin <= imax) {
            int i = (imin + imax) / 2;
            int j = half_len - i;
            if (i > 0 && nums1[i-1] > nums2[j]) imax = i - 1;
            else if (i < m && nums2[j-1] > nums1[i]) imin = i + 1;
            else {
                int max_of_left = 0, min_of_right = 0;
                if (i == 0) max_of_left = nums2[j-1];
                else if (j == 0) max_of_left = nums1[i-1];
                else max_of_left = max(nums1[i-1], nums2[j-1]);
                if ((m + n) % 2 != 0) return (double) max_of_left;
                if (i == m) min_of_right = nums2[j];
                else if (j == n) min_of_right = nums1[i];
                else min_of_right = min(nums1[i], nums2[j]);
                return (double) (max_of_left + min_of_right) / 2;
            }
        }
        return (double) -1;
    }
};




// Let me add some interpretation of the find kth function based on my understanding

// We have two arrays:

// nums1[0], nums1[1]....nums1[m - 1];

// nums2[0], nums2[2]....nums2[n - 1];

// the result after merging:

// num[0],num[1],num[2]...num[m + n - 1];

// Let‘s compare nums1[k / 2 - 1] and nums2[k / 2 - 1]

// if nums1[k / 2 - 1] < nums2 [k / 2 - 1]

// then the nums1[k / 2 - 1] and it's left side elements must smaller than kth number in num arrary(num[k - 1]).
// Why?
// Assume that nums1[k / 2 - 1] == num[k - 1];

// Let's count the number of elements which smaller than nums1[k / 2 - 1].

// Consider an extreme case : nums1[0]....nums1[k / 2 - 2] and nums2[0]...nums2[k / 2 - 2] smaller than nums1[k / 2 - 1];

// In this special case, we only have k / 2 - 1 + k / 2 - 1 = k - 2 elements smaller than the nums1[k / 2 - 1]. so nums1[k / 2 - 1] only can be (k - 1)th smallest number (num[k - 2]);
// So, it's a contradiction with our assumption.

// And now we could say, The num[k / 2 - 1] and it's left side elements must smaller than the Kth smallest number.
// so we could remove the elements which in this range and shrink the problem set.
// same idea when nums1[k / 2 - 1] > nums2 [k / 2 - 1]. we could remove the elements in the nums2;

// Correct me, if I'm wrong. Thanks

// Here is my AC code :

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size();
        int k = (m + n) / 2;
        int num1 = findKth(nums1, 0, m, nums2, 0, n, k + 1);
        if ((n + m) % 2 == 0)
        {
            int num2 = findKth(nums1, 0, m, nums2, 0, n, k);
            return (num1 + num2) / 2.0;
        }
        else return num1;
    }
    int findKth(vector<int> & nums1, int nums1_left, int nums1_right, vector<int> & nums2, int nums2_left, int nums2_right, int k)
    {
        int m = nums1_right - nums1_left;
        int n = nums2_right - nums2_left;
        if (m > n) return findKth(nums2, nums2_left, nums2_right, nums1, nums1_left, nums1_right, k);
        else if (m == 0)
            return nums2[nums2_left + k - 1];
        else if (k == 1)
            return min(nums1[nums1_left], nums2[nums2_left]);
        else {
            int s1LeftCount = min (k / 2, m);
            int s2LeftCount = k - s1LeftCount;
            if (nums1[nums1_left + s1LeftCount - 1] == nums2[nums2_left + s2LeftCount - 1])
                return nums1[nums1_left + s1LeftCount - 1];
            else if (nums1[nums1_left + s1LeftCount - 1] < nums2[nums2_left + s2LeftCount - 1])
                return findKth(nums1, nums1_left + s1LeftCount, nums1_right, nums2, nums2_left, nums2_right, k - s1LeftCount);
            else
            return findKth(nums1, nums1_left, nums1_right, nums2, nums2_left + s2LeftCount, nums2_right, k - s2LeftCount);
        }
    }
}

