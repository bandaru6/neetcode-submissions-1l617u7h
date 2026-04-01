#include <vector>
class MovingAverage {
private:
    std::vector<int> data;
    int size;
public:
    MovingAverage(int size) {
        this->size = size;
    }
    
    double next(int val) {
        this->data.push_back(val);
        while (this->data.size() > this->size) {
            this->data.erase(this->data.begin());
        }
        double total = 0;
        for (auto const& curr: this->data) {
            total += curr;
        }
        return total / this->data.size();
    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */
