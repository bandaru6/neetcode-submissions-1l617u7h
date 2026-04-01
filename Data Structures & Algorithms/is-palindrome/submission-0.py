class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        y = ''
        for x in s:
            y +=  x if (x.isdigit() or x.isalpha()) else ''
        print(y)
        for ind, val in enumerate(y):
            if len(y) == 1:
                break
            if val != y[len(y) - 1 - ind]:
                return False
        return True
