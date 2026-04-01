class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for word in strs:
            letters = [0] * 26
            for char in word:
                letters[ord(char) - ord('a')] += 1
            res[tuple(letters)].append(word)
        ret = []
        for x in res:
            ret.append(res[x])
        return ret