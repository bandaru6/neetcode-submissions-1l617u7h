class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        
        largest_rectangle = 0
        for i in range(len(heights)):
            min_height = heights[i]
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                largest_rectangle = max(largest_rectangle, min_height*(j-i+1))
                
       
        return largest_rectangle


