class Solution:
    def compress(self, chars: List[str]) -> int:
        
        length = len(chars)
        
        s = ""
        i = 0

        while i < len(chars):
            s += chars[i]
            new = 1
            while i < len(chars) - 1 and chars[i] == chars[i+1]:
                i += 1
                new += 1
            if new > 1:
                s += str(new)
            
            i += 1
        for x in range(len(s)):
            chars[x] = s[x]
        return len(s)
            



                
            