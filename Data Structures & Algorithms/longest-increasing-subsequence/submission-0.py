class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        highest = 0
        dp = [[0] * (len(nums)+1) for x in range(len(nums) + 1)]

        prev = 100e9
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i - 1, -2, -1):
                LIS = dp[i+1][j+1]

                if j == -1 or nums[j] < nums[i]:
                    LIS = max(LIS, 1 + dp[i + 1][i + 1])
                
                dp[i][j + 1] = LIS

        return dp[0][0]