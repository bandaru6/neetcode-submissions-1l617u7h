class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def isPalindrome(string):
            for x in range(len(string)):
                if string[x] != string[len(string)- 1 - x]:
                    return False
            return True
        
        longest = s[0]
        for x in range(len(s)):
            for y in range(len(s)):
                if isPalindrome(s[x:y+1]):
                    longest = s[x:y+1] if len(s[x:y+1]) > len(longest) else longest
        
        return longest