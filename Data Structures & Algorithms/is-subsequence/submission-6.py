class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        loc = 0

        for c in t:
            if loc == len(s):
                return True
            if c == s[loc]:
                loc += 1
        return loc == len(s)