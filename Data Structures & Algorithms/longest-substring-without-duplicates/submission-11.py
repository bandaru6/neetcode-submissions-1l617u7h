class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0
        visited = defaultdict(int)
        visited[s[l]] = l
        res = 1
        for r in range(1, len(s)):
            if s[r] in visited:
                l = max(l, visited[s[r]] + 1)
            
            visited[s[r]] = r

            print(l, r, s[l:r + 1])
            res = max(res, r + 1 - l)
        
        return res