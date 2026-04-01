class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        l, r = 0, n - 1

        # find any occurrence
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                # leftmost
                L, R = 0, mid
                while L < R:
                    m = (L + R) // 2
                    if nums[m] < target:
                        L = m + 1
                    else:
                        R = m
                left = L

                # rightmost
                L, R = mid, n - 1
                while L < R:
                    m = (L + R + 1) // 2  # bias right
                    if nums[m] > target:
                        R = m - 1
                    else:
                        L = m
                right = L

                return [left, right]

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return [-1, -1]
        