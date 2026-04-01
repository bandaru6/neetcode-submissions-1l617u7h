class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        minLen = 10e9
        l = 0
        for r in range(n+1):
            currSum = sum(nums[l:r])
            while currSum >= target:
                currLen = len(nums[l:r])
                minLen = min(minLen, currLen)
                l += 1
                currSum = sum(nums[l:r])
                
        
        return minLen if minLen != 10e9 else 0
            

