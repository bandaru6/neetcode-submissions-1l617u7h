class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        if not hashset:
            return 0
        small = min(hashset)
                
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