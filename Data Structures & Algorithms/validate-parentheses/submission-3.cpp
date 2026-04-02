#include <stack>

class Solution {
public:
    bool isValid(string s) {
        std::stack<char> curr = std::stack<char>();
        for (char c: s) {
            if (c == '[' || c == '{' || c == '(') {
                curr.push(c);
            }
            else {
                if (curr.size() >= 1) {
                    if (c == ']' && curr.top() == '[') {
                        curr.pop();
                    }
                    else if (c == '}' && curr.top() == '{') {
                        curr.pop();
                    }
                    else if (c == ')' && curr.top() == '(') {
                        curr.pop();
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
                
            }
        }

        return curr.size() == 0;
    }
};
