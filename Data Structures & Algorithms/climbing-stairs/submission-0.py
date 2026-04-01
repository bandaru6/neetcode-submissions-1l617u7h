class Solution:
    def climbStairs(self, n: int) -> int:
        fib, fib2 = 0, 1
        resp = 0
        for x in range(n):
            tmp = fib2
            fib2 += fib
            fib = tmp

        return fib2