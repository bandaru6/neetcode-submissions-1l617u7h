class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for index, c in enumerate(s):
            if c == '(':
                stack.append(index)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    s[index] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)