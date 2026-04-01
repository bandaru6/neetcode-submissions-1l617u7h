class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        freq2 = {}
        for x in s:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        for x in t:
            if x in freq2:
                freq2[x] += 1
            else:
                freq2[x] = 1
        return freq == freq2