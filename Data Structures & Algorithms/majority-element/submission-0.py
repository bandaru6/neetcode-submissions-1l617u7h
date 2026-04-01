class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq = defaultdict(int)
        for x in nums:
            freq[x] += 1

        arr = [[] for i in range(len(nums) + 1)]

        for item in freq.keys():
            arr[freq[item]].append(item)
        
        arr = arr[::-1]
        for x in arr:
            if x == []:
                continue
            else:
                return x[0]
        return 0
