class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1 # ord(letter) maps to ASCII value
            
            res[tuple(count)].append(word)

        return list(res.values())
                
            
                
        