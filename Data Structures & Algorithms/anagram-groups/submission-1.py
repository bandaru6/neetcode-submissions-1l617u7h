class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for x in strs:
            arr = [0] * 26
            for char in x:
                arr[ord(char) - ord("a")] += 1
            res[tuple(arr)].append(x)
        
        return list(res.values())
