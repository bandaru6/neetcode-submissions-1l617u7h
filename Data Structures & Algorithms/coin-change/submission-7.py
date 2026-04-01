class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0


        for curr in range(1, len(dp)):
            for coin in coins:
                if curr - coin >= 0:
                    dp[curr] = min(dp[curr], 1 + dp[curr - coin])
                

        return dp[amount] if dp[amount] != amount+1 else -1
                

        """ BRUTE FORCE:
        if amount == 0:
            return 0
        dp = [10e9] * (amount + 1) #dp[curr] = min coins needed to reach amount from curr
        dp[amount] = 0 #base: if already at amount, need 0 more coins

        def dfs(curr):
            if curr > amount:
                return 10e9 #impossible path
            if dp[curr] != 10e9:
                return dp[curr]

            best = 10e9
            for coin in coins:
                best = min(best, 1 + dfs(curr + coin))

            dp[curr] = best
            return dp[curr]

        ans = dfs(0)
        return ans if ans != 10e9 else -1
        """
