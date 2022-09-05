// 刷題用這個, time complexity O(nlogn), space complexity O(n)
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size() , ans = 1;
        vector<pair<int,double>> cars(n);
        for(int i=0;i<n;i++){
            cars[i].first = position[i];
            cars[i].second = (double)(target - position[i])/(double)(speed[i]);
        }
        sort(cars.begin() , cars.end(), greater<>()); // greater<>() => descending order
        vector<double> stack;
        for (auto car: cars) {
            if (stack.empty()) stack.emplace_back(car.second);
            else if (car.second > stack.back()) stack.emplace_back(car.second);
        }
        return stack.size();
    }
};


class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size() , ans = 1;
        vector<pair<int,double>> cars(n);
        //positions of cars and the time taken to reach target. 
        for(int i=0;i<n;i++){
            cars[i].first = position[i];
            cars[i].second = (double)(target - position[i])/(double)(speed[i]);
        }
        sort(cars.begin() , cars.end());
        double slowest = cars[n-1].second;        

        for(int i=n-2;i>=0;i--){
            if(cars[i].second > slowest) {
                ans++; 
                slowest = cars[i].second;
            }
        }
        return ans;
    }
};


// Time Complexity:

// O(NlogN +N)
// NlogN for sorting
// N for iterate through all cars to form a mono stack.
// Space Complexity:

// O(N) for stack and vector of cars.

class Car{
public:
    Car(int pos, int speed){
        this->pos = pos;
        this->speed= speed;
    }
    int pos;
    int speed;
};

class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<Car> cars;
        int N = position.size();
        for(int i = 0; i<N; i++){
            cars.emplace_back(position.at(i), speed.at(i));
        }
        
        sort(cars.begin(), cars.end(), [](const Car& a, const Car& b){
            return a.pos<b.pos;
        });
        
        stack<float> mono;
        for(int i = 0; i<N; i++){
            float time = 
                (target-cars.at(i).pos)/(float)cars.at(i).speed;
            while(!mono.empty() && time >= mono.top()){
                mono.pop();
            }
            mono.push(time);
        }
        return mono.size();
    }
};
