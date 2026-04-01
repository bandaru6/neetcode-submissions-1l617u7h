class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        used = {}
        resp = []
        for x in range (len(nums)):
            if nums[x] in used:
                resp = sorted([x, used[nums[x]]])
            used[target - nums[x]] = x
        return resp