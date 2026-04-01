class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        if not hashset:
            return 0
        small = min(nums)
                
        longest = 1
        curr = 1

        visited = set()
        i = 0
        while i < len(nums):
            val = nums[i]
            while (val + 1) in hashset:
                visited.add(val)
                curr += 1
                longest = max(longest, curr)
                val += 1
            curr = 1
            i += 1
        return longest