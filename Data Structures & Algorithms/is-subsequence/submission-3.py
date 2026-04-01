class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i = 0
        for r in range(len(t)):
            if i < len(s):
                if s[i] == t[r]:
                    i += 1
        return i == len(s)  
