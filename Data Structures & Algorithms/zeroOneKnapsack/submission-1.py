class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        memo = {}

        def dfs(i, capacity):

            if (i, capacity) in memo:
                return memo[(i, capacity)]
            if i == len(weight):
                return 0
            
            skip = dfs(i+1, capacity)

            take = 0
            if weight[i] <= capacity:
                take += profit[i] + dfs(i+1, capacity - weight[i])
            
            memo[(i, capacity)] = max(skip, take)

            return memo[(i, capacity)]
            
        return dfs(0, capacity)






