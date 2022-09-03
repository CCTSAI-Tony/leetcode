// time complexity O(1), space complexity O(n)
class MinStack {
public:
    vector< pair<int,int> > s;
	
    MinStack() { }
    
    void push(int val) {
        if(s.empty())
            s.push_back({val,val});
        else
            s.push_back({val,min(s.back().second,val)});    
    }
    
    void pop() { s.pop_back(); }
    
    int top() { return s.back().first; }
    
    int getMin() { return s.back().second; }
};

// rewrite second time
class MinStack {
public:
    vector<pair<int, int>> stack;
    MinStack() {
        
    }
    
    void push(int val) {
        if (stack.empty()) stack.push_back(make_pair(val, val));
        else stack.push_back(make_pair(val, min(val, getMin())));
    }
    
    void pop() {
        stack.pop_back();
    }
    
    int top() {
        return stack.back().first;
    }
    
    int getMin() {
        return stack.back().second;
    }
};
