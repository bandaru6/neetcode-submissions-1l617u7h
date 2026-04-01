#include <string>

class Solution {
public:
    int calculate(string s) {
        int num = 0, prev = 0, total = 0;
        char op = '+';

        for (int i = 0; i <= s.size(); i++) {
            char ch = s[i];

            if (ch == ' ') {
                continue;
            }

            if ('0' <= ch and ch <= '9') {
                num = num * 10 + (ch - '0');
            }
            else {
                if (op == '+') {
                    total += prev;
                    prev = num;
                }
                else if (op == '-') {
                    total += prev;
                    prev = -num;
                }
                else if (op == '*') {
                    prev *= num;
                }
                else {
                    if (prev < 0) {
                        prev = -(-prev / num);
                    } else {
                        prev /= num;
                    }
                }
                op = ch;
                num = 0;
            }
        }
        total += prev;
        return total;
    }
};