class Solution:
    def longestPalindrome(self, s: str) -> str:

        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[resIdx : resIdx + resLen]
            

        """
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
        """