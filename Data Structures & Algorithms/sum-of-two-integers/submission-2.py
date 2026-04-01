class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            bita = (a >> i) & 1
            bitb = (b >> i) & 1
            curr = bitb ^ bita ^ carry
            carry = (bita and bitb) or (bita and carry) or (bitb and carry)
            if curr:
                res |= (1 << i)
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        return res


        