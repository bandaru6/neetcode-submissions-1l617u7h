class Solution:
    def compress(self, chars: List[str]) -> int:
        
        length = len(chars)
        

        index = new = 0
        while index < length:
            chars[new] = chars[index]
            new += 1
            nex = index + 1

            while nex < length and chars[index] == chars[nex]:
                nex += 1
            
            if nex - index > 1:
                for char in str(nex - index):
                    chars[new] = char
                    new += 1
            index = nex

        return new
            



                
            