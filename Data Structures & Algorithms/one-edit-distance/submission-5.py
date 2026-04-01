class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        if s == t:
            return False

        shorter = s if len(s) < len(t) else t
        longer = t if len(s) < len(t) else s

        changes = 0
        for index, char in enumerate(shorter):

            if shorter[index] != longer[index]:
                if len(shorter) == len(longer):
                    return shorter[index + 1:] == longer[index + 1:]
           
                else:
                    return shorter[index:] == longer[index+1:] 
                
        return len(longer) == len(shorter) + 1