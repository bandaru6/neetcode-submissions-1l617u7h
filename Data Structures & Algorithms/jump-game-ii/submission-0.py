class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        
        r = len(nums) - 1
        while r > 0:
            newpos = r
            l = r - 1
            while l >= 0:
                if nums[l] + l >= r:
                    newpos = l
                l -= 1

            jumps += 1
            r = newpos
        
        return jumps
            
            

