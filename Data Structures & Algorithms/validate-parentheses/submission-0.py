class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        q = ""
        brackets = ['(', '[', '{']
        for index, value in enumerate(s):
            if value in brackets:
                q += value
            else:
                if value == ')' and q and q[-1] == '(':
                    q = q[:-1]
                    continue
                elif value == ']' and q and q[-1]== '[':
                    q = q[:-1]
                    continue
                elif value == '}' and q and q[-1] == '{':
                    q = q[:-1]
                    continue
                else:
                    return False
        return len(q) == 0

