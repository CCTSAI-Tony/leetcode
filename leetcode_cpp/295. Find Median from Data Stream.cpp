class MedianFinder {
public:
    priority_queue<int> small;
    priority_queue<int> large;

    MedianFinder() {
    }
    
    void addNum(int num) {
        if (small.size() == large.size()) {
            large.push(-num);
            int large_top = -large.top();
            large.pop();
            small.push(large_top);
        }
        else {
            small.push(num);
            int small_top = -small.top();
            small.pop();
            large.push(small_top);
        }
    }
    
    double findMedian() {
        if (small.size() == large.size()) {
            return (double) (small.top() - large.top()) / 2;
        }
        else return (double) small.top(); //設計small 多一個
    }
};
