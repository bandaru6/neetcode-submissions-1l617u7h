class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        maxL, l = 0, 0
        maxR, r = 0, len(height) - 1
        water = 0
        while l <= r:
            if maxL <= maxR:
                water += max(0, maxL - height[l])
                maxL = max(maxL, height[l])
                l += 1
            else:
                water += max(0, maxR - height[r])
                maxR = max(maxR, height[r])
                r -= 1
        return water