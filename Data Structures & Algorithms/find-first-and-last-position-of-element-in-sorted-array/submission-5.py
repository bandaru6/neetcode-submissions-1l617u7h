class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l, r = 0, len(nums) - 1

        if target not in nums:
            return [-1, -1]

        while l <= r:
            mid = (r + l) // 2
            start = mid
            end = mid

            if nums[mid] == target:
                while start - 1 >= 0 and nums[start - 1] == target:
                    start -= 1
                while end + 1 < len(nums) and nums[end + 1] == target:
                    end += 1
                return [start, end]
            
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return [-1, -1]
        