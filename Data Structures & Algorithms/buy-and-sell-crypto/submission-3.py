class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 10e9
        res = 0
        for p in prices:
            res = max(res, p - lowest)
            lowest = min(lowest, p)
        return res