class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        small = min(nums)

        longest = 1
        curr = 0

        for i in range(len(nums)):
            if small + 1 in nums:
                curr += 1
                longest = max(curr, longest)
            else:
                curr = 1
                
        longest = 1
        curr = 1

        for index, value in enumerate(nums):
            val = value
            while (val + 1) in nums:
                curr += 1
                longest = max(longest, curr)
                val += 1
            curr = 1
        return longest

        return longest