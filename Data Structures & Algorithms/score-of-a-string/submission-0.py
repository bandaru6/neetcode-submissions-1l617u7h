class Solution:
    def scoreOfString(self, s: str) -> int:
        
        res = 0

        for ind, val in enumerate(s[:-1]):
            res += abs(ord(val) - ord(s[ind + 1]))
        
        return res