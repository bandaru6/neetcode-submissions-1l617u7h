class Solution:
    def calculate(self, s: str) -> int:

        op = '+'
        num = prev = total = 0

        for i in range(len(s) + 1):
            char = s[i] if i < len(s) else '+'

            if char == ' ':
                continue

            if '0' <= char <= '9':
                num = num * 10 + int(char)
            else:
                if op == '+':
                    total += prev
                    prev = num
                elif op == '-':
                    total += prev
                    prev = -num
                elif op == '*':
                    prev *= num
                else:
                    if prev < 0:
                        prev = -(-prev // num)
                    else:
                        prev = prev // num
                op = char
                num = 0
        
        total += prev
        return total

        



