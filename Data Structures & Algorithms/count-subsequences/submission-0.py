class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        memo = {}

        def dfs(i, j):

            if (i ,j) in memo:
                return memo[(i, j)]
            
            if j == len(t):
                return 1

            if i >= len(s):
                return 0

            print("state:", (i ,j))
            print("s[i]:", s[i], "t[j]:", t[j])
            print()

            res = 0
            if s[i] == t[j]:    
                res += dfs(i + 1, j + 1)
            
            res += dfs(i + 1, j)
            print(res)

            memo[(i, j)] = res

            return memo[(i, j)]
        
        return dfs(0,0)

