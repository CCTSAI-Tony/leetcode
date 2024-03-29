// 刷題用這個, 488ms
class Node {
public:
    int key, value;
    Node *prev, *next;
    Node(int key, int value) {
        this->key = key;
        this->value = value;
        this->prev = NULL;
        this->next = NULL;
    }
};

class LRUCache {
public:
    Node *head, *tail;
    int capacity, size;
    unordered_map<int, Node*> dic;
    LRUCache(int capacity) {
        this->capacity = capacity;
        this->size = 0;
        this->head = new Node(0, 0);
        this->tail = new Node(0, 0);
        this->head->next = this->tail;
        this->tail->prev = this->head;
    }
    
    int get(int key) {
        Node* n;
        if (dic.find(key) != dic.end()) {
            n = dic[key];
            _remove(n);
            _add(n);
            return n->value;
        }
        return -1;
    }
    
    void put(int key, int value) {
        Node* n;
        if (dic.find(key) != dic.end()) {
            n = dic[key];
            _remove(n);
        }
        n = new Node(key, value);
        _add(n);
        dic[key] = n;
        if (dic.size() > capacity) {
            n = head->next;
            dic.erase(n->key);
            _remove(n);
            delete n;  // free heap memory
        }
    }
    
    void _remove(Node* node) {
        Node* p = node->prev;
        Node* n = node->next;
        p->next = n;
        n->prev = p;
    }
    
    void _add(Node* node) {
        Node* p = tail->prev;
        p->next = node;
        tail->prev = node;
        node->prev = p;
        node->next = tail;
    }
};


class LRUCache {
public:
    
    // this list will have (key, value) pairs that we need
    list<pair<int, int>> cache;
    // this unordered_map will have the key and address of list where that key is stored
    unordered_map<int, list<pair<int,int>> :: iterator> myMap;
    int maxSize; // max Capacity
    
    // this is the main logic and game changing function
    // this function will remove the (key, value) from the cache
    // insert the new (key,value) in front of cache
    // update/enter the address of (key,address) in map
    void refreshPosition(int key, int value) {
        
        // find the position of the key and remove it from the cache
        cache.erase(myMap[key]);
        // push in front the new (key,value) pair
        cache.push_front(make_pair(key, value));
        // make entry in map as cache.begin() because we added it in front
        myMap[key] = cache.begin();
        
    }
   
    LRUCache(int capacity) {
        maxSize = capacity;
    }
    
    // check if that value is already present in map
    // if yes, then refresh the position to make it the first element in cache
    // return the value from the pair (key, value)
    // return -1 if not found
    int get(int key) {
        // if found in map
        if(myMap.find(key) != myMap.end()) {
            // *myMap[key] -> second will give us the corresponding value of the key
            // because myMap[key] stores the address of the pair and not the pair itself
            int value = (*myMap[key]).second;
            refreshPosition(key, value);
            return value;
        }
        return -1; // if not found
    }
    
    // if a pair is already present then just refresh it
    // check if that key exists in map, if it does then just refresh the position
    void put(int key, int value) {
        if(myMap.find(key) != myMap.end())
            refreshPosition(key, value); 
        // here we refresh (key, value) and not (key, (*myMap[key]).second) because if put [2,1] and put [2,2] is called
        // then get(2) should give ans 2 and not 1, so refresh with latest value and same key
        else {
            // push it in front of the cache
            cache.push_front(make_pair(key, value));
            myMap[key] = cache.begin();
            
            // if capacity is overflown after this insertion then remove the last element from cache
            if(myMap.size() > maxSize) {
                // erase the last element of the cache from map
                myMap.erase(cache.back().first);
                // pop that element from cache as well
                cache.pop_back();
            }
        }
    }
    
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */



