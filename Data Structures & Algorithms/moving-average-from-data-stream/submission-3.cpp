#include <vector>
class MovingAverage {
private:
    std::queue<int> data;
    int size;
    double sum;

public:
    MovingAverage(int size) {
        this->size = size;
        this->sum = 0;
    }
    
    double next(int val) {
        this->data.push(val);
        this->sum += val;

        if (this->data.size() > this->size) {
            this->sum -= this->data.front();
            this->data.pop();
        }

        return this->sum / this->data.size();
    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */
