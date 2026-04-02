class Solution {
public:
    bool isSubsequence(string s, string t) {


        int i = 0;
        for (char c: t) {
            if (s[i] == c) {
                i += 1;
            }
        }
        return i == s.size();
    }
};