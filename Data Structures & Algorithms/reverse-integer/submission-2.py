class Solution:
    def reverse(self, x: int) -> int:

        MAX = (2) ** 31 - 1
        MIN = -2 ** 31

        res = 0
        neg = x < 0
        
        x = abs(x)
            
        
        while x:
            digit = x % 10
            x //= 10

            if res > MAX // 10 or (res == MAX // 10 and digit >= MAX & 10):
                return 0
            res = res * 10 + digit
        return -res if neg else res