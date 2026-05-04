class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        
        stack = [] #[index, height]
        maxArea = 0
        for i in range(len(heights)):
            new_index = i 
            while stack and stack[-1][1] > heights[i]:
                old_i, h = stack.pop(-1)
                maxArea = max(maxArea, h * (i - old_i))
                print(f"h:{h} old_i:{old_i} i:{i} h * (i - old_i) = {h * (i - old_i)}")
                new_index = min(new_index, old_i)
            
            stack.append([new_index, heights[i]])
        
        
        while stack:
            old_i, h = stack.pop(-1)
            maxArea = max(maxArea, h * (n - old_i))
            print(f"h:{h} old_i:{old_i} h * (n - old_i) = {h * (n - old_i)}")

                
        return maxArea


