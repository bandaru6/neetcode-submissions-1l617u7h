class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        resp = []
        for index, value in enumerate(nums):
            if value > 0:
                break
            if value == nums[index - 1] and index > 0:
                continue
            l, r = index + 1, len(nums) - 1
            if r == len(nums):
                continue
            while l < r:
                if value + nums[l] + nums[r] == 0:
                    resp.append([value, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif value + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return resp