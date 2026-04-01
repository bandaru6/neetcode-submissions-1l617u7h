class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prev = strs[0]
        for x in strs:
            while prev != x[0:len(prev)]:
                prev = prev[0:-1]
        
        return prev
