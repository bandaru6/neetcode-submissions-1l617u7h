#include <unordered_map>
#include <utility>
#include <vector>

class TimeMap {
private:
    std::unordered_map<string, std::vector<std::pair<int, string>>> store;
public:

    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        this->store[key].push_back({timestamp, value});
        // this->store[key].push_back(std::pair<int, string>(timestamp, value));
    }
    
    string get(string key, int timestamp) {
        auto& values = this->store[key];
        int l = 0, r = values.size() - 1;
        string result = "";

        while (l <= r) {
            int m = l + (r - l) / 2;
            if (values[m].first <= timestamp) {
                result = values[m].second;
                l = m + 1;
            } else{
                r = m - 1;
            }
        }

        return result;
    }
};
