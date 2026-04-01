class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 10e9
        profit = 0
        for x in prices:
            low = min(low, x)
            profit = max(profit, x - low)
        return profit