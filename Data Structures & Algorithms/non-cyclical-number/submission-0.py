class Solution:
    def isHappy(self, n: int) -> bool:
        fast = self.sos(n)
        slow = n
        while slow != fast:
            if fast == 1 or slow == 1:
                return True
            fast = self.sos(self.sos(fast))
            slow = self.sos(slow)
        return True if fast == 1 else False
    def sos(self, n: int) -> int:
        sum = 0
        while n:
            digit = n % 10
            sum += digit ** 2
            n = n // 10
        return sum




        
            
        