class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        if not numset:
            return 0

        visited = set()
        longest = 0
        i = 0

        while i < len(nums):
            start = nums[i]

            # skip if we’ve already consumed this value in a previous run
            if start in visited:
                i += 1
                continue

            # only expand if this is a start-of-run
            if (start - 1) not in numset:
                length = 1
                v = start
                visited.add(v)
                while (v + 1) in numset:
                    v += 1
                    visited.add(v)
                    length += 1
                longest = max(longest, length)

            i += 1

        return longest