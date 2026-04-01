class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        vals = set(nums)
        longest = 0
        for x in vals:
            if x - 1 not in vals:
                length = 1
                while x + length in vals:
                    length += 1
                longest = max(longest, length)
        return longest

