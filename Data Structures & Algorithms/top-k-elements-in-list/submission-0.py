class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        
        for x in nums:
            freq[x] += 1
            
        return list(sorted(freq.keys(), key=lambda x: freq[x], reverse=True))[:k]

        