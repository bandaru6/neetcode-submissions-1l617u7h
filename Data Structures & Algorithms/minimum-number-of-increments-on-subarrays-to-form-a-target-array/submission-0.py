class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ops = 0
        prev = 0
        for i in target:
            if i > prev:
                ops += i - prev
            prev = i
        return ops

