class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        prev = [0]*n
        curr = [0]*n

        for r in range(m - 1, -1, -1):
            if r == m - 1:
                curr[n - 1] = 1
            for c in range(n - 2, -1, -1):
                curr[c] = curr[c + 1] + prev[c]
            prev = curr
            
        return curr[0]



        """MEMO
        memo = [[0] * n for x in range(m)]
        def dfs(r, c):
            if r >= m or c >= n:
                return 0
            if r == m -1 and c == n -1:
                return 1
            if memo[r][c] != 0:
                return memo[r][c]
            memo[r][c] = dfs(r+1, c) + dfs(r, c+1)
            return memo[r][c]
        
        return dfs(0,0)
"""
        """ Brute Force
        def dfs(currm, currn, m, n):
            if currm == m-1 and currn == n-1:
                return 1
            if currm >= m or currn >= n:
                return 0 
            return dfs(currm + 1, currn, m, n) + dfs(currm, currn+1, m, n)
        
        return dfs(0, 0, m, n)
        """