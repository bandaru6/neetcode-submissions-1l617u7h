class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}

        def dfs(i, cap):

            if (i, cap) in memo:
                return memo[(i, cap)]
            if i >= len(weight):
                return 0
            
            skip = dfs(i + 1, cap)

            take = 0
            if weight[i] <= cap:
                take = dfs(i, cap - weight[i]) + profit[i]
            
            memo[(i, cap)] = max(skip, take)

            return memo[(i, cap)]
        

        return dfs(0, capacity)