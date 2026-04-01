class Solution:
    def romanToInt(self, s: str) -> int:
        
        num = 0
        i = 0
        while i < len(s):
            if s[i] == "M":
                num += 1000
            if s[i] == "D":
                num += 500
            if s[i] == "C":
                if i < len(s) - 1 and (s[i+1] == "D" or s[i+1] == "M"):
                    if s[i+1] == "D":
                        num += 400
                    if s[i+1] == "M":
                        num += 900
                    i += 1
                else:
                    num += 100
            if s[i] == "L":
                num += 50
            if s[i] == "X":
                if i < len(s) - 1 and (s[i+1] == "L" or s[i+1] == "C"):
                    if s[i+1] == "L":
                        num += 40
                    if s[i+1] == "C":
                        num += 90
                    i += 1
                else:
                    num += 10
            if s[i] == "V":
                num += 5
            if s[i] == "I":
                if i < len(s) - 1 and (s[i+1] == "V" or s[i+1] == "X"):
                    if s[i+1] == "V":
                        num += 4
                    if s[i+1] == "X":
                        num += 9
                    i += 1
                else:
                    num += 1

            i += 1 
        
        return num