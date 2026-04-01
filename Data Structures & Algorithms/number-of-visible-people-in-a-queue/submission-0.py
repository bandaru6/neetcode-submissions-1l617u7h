class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = []
        for index, height in enumerate(heights):
            total = 0
            maxlowerheight = 0

            for j in range(index + 1, len(heights)):
                if min(heights[index], heights[j]) > maxlowerheight:
                    total += 1
                maxlowerheight = max(maxlowerheight, heights[j])
            res.append(total)
        return res