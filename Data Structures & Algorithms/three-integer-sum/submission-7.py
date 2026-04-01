class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums = sorted(nums)

        for i, val in enumerate(nums):
            if val == nums[i - 1] and i > 0:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = val + nums[l] + nums[r] 
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res