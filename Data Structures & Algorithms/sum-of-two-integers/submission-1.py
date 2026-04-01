class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            cur_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit and b_bit and carry) or (b_bit and carry) or (a_bit and b_bit) or (a_bit and carry)
            if cur_bit:
                res |= (1 << i)
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res

        