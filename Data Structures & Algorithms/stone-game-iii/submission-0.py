class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        memo = {}

        def dfs(i):
            if i >= len(stoneValue):
                return 0

            if i in memo:
                return memo[i]

            res = -10e9
            
            for x in range(i + 1, i + 4):
                res = max(res, sum(stoneValue[i:x]) - dfs(x))
            
            memo[i] = res

            return memo[i]
        
        ans = dfs(0)

        if ans > 0:
            return "Alice"
        elif ans < 0:
            return "Bob"

        return "Tie"
