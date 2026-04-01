class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for x in range(len(nums) - 1, -1, -1):
            if x + nums[x] >= goal:
                goal = x
        
        return goal == 0