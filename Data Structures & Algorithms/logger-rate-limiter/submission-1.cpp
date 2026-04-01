#include <unordered_map>

class Logger {
private:
    std::unordered_map<string, int> logs; 
public:
    Logger() {
    }
    bool shouldPrintMessage(int timestamp, string message) {
        bool message_logged = false;
        for (auto const&[key, value] : this->logs) {
            if (message == key) {
                message_logged = true;
            }
        }
        if (message_logged) {
            if (timestamp - this->logs[message] < 10) {
                return false;
            } 
        }
        this->logs[message] = timestamp;
        return true;
    }
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */
