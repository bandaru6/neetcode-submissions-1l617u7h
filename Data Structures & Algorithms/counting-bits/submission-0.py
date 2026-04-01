class Solution:
    def countBits(self, n: int) -> List[int]:
        ones = []
        for x in range(n + 1):
            res = 0
            while x:
                x = x & (x - 1)
                res += 1
            ones.append(res)
        return ones
