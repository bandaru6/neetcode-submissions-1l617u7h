class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largest = int(-10e5)
        curr_sum = 0
        for x in nums:
            curr_sum += x
            if curr_sum < 0:
                largest = max(largest, curr_sum)
                curr_sum = 0
                continue
            else:
                largest = max(largest, curr_sum)
        
        return largest