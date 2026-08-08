class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        l_max = height[l]
        r_max = height[r]
        water = 0

        while l <= r:
            if r_max < l_max:
                water += min(l_max, r_max) - height[r] if min(l_max, r_max) - height[r] > 0 else 0
                r_max = max(r_max, height[r])
                r -= 1
            else:
                
                
                water += min(l_max, r_max) - height[l] if min(l_max, r_max) - height[l] > 0 else 0

                l_max = max(l_max, height[l])
                l += 1

        return water
