class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largest = int(-10e5)
        curr_sum = 0
        for x in nums:
            curr_sum += x
            largest = max(largest, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        
        return largest