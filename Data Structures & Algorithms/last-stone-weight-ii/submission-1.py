class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        memo = {}

        total = sum(stones)


        def dfs(i, currSum):

            if i >= len(stones):
                return abs((total - currSum) - currSum)

            if (i, currSum) in memo:
                return memo[(i, currSum)]
            
            skip = dfs(i + 1, currSum)
            take = dfs(i+1, currSum + stones[i])

            memo[(i, currSum)] = min(skip, take)

            return memo[(i, currSum)]

        return dfs(0, 0)

        



        
