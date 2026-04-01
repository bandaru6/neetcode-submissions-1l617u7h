class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dfs(currm, currn, m, n):
            if currm == m-1 and currn == n-1:
                return 1
            if currm >= m or currn >= n:
                return 0 
            return dfs(currm + 1, currn, m, n) + dfs(currm, currn+1, m, n)
        
        return dfs(0, 0, m, n)