class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs:
            while prefix not in s:
                prefix = prefix[:-1]
        return prefix
