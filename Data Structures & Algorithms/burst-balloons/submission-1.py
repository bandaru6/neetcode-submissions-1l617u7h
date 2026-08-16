class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        

        nums = [1] + nums + [1]

        memo = {}

        def dfs(l, r):

            if l + 1 >= r:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]
            
            best = 0
            for x in range(l + 1, r):
                left = dfs(l, x)
                right = dfs(x, r)

                lastPop = nums[l] * nums[x] * nums[r]

                best = max(best, left + lastPop + right)

            memo[(l, r)] = best
            return best

        return dfs(0, len(nums) - 1)



            
