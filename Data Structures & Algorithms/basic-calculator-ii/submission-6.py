class Solution:
    def calculate(self, s: str) -> int:
        
        curr = 0 
        op = "+"
        stack = []
        for i in range(len(s)):
            if s[i] ==' '  and i != len(s) - 1:
                continue

            if s[i] not in ['+', '-', '*', '/', ' '] and i != len(s) - 1:
                curr = int(s[i]) if curr == 0 else int( str(curr) + s[i])
            else:
                if i == len(s) - 1 and s[i] != ' ':
                    curr = int(s[i]) if curr == 0 else int( str(curr) + s[i])
                if op == '+':
                    stack.append(curr)
                elif op == '-':
                    stack.append(-curr)
                elif op == '*':
                    prev = stack.pop()
                    stack.append(prev * curr)
                else:
                    prev = stack.pop()
                    stack.append(int(prev/curr))
                
                op = s[i]
                curr = 0
        print(stack)
        return sum(stack)

                


        



