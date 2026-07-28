class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        p = str(x)

        while len(p) > 1:
            if p[0] != p[-1]:
                return False
            p = p[1:-1]
        
        return True