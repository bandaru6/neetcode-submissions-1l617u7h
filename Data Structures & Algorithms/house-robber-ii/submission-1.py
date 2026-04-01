class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]

        
        h1, h2 = 0,0 
        for x in range(len(nums) - 1):
            temp = max(nums[x] + h1, h2)
            h1 = h2
            h2 = temp 
        largest = h2


        h1, h2 = 0,0
        for x in range(1, len(nums)):
            temp = max(nums[x] + h1, h2)
            h1 = h2
            h2 = temp 

        return max(largest, h2)


