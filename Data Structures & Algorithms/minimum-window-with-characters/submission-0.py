class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map, curr_map = defaultdict(int), defaultdict(int)
        needed = 0
        for x in t:
            if x not in t_map:
                needed += 1
            t_map[x] += 1
        
        l = 0
        curr = 0
        shortest = "a" * 10000
        for r in range(len(s)):
            
            curr_map[s[r]] += 1
            if curr_map[s[r]] == t_map[s[r]]:
                curr += 1
                

            while curr == needed:
                shortest = s[l:r + 1] if len(s[l:r + 1]) < len(shortest) else shortest
                
                l += 1
                curr_map[s[l - 1]] -= 1
                if curr_map[s[l - 1]] < t_map[s[l - 1]]:
                    curr -= 1
        
        return shortest if shortest != "a" * 10000 else ""
            


        
