class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        for x in nums:
            freq[x] += 1
        
        freq_ord = [[] for i in range(len(nums) + 1)]

        for item in freq.keys():
            freq_ord[freq[item]].append(item)

        print(freq_ord)
        freq_ord = freq_ord[::-1]
        res = []
        count = 0
        for x in freq_ord:
            if x == []:
                continue
            else:
                for y in x:
                    res.append(y)
                    count += 1
                    if count >= k:
                        return res
        return []




        # 1. store the counts of each int in nums using a dictionary
        # 2. create a list which stores lists
        # 3. add each number to the list with that frequency
        # 4. add this to a new list by iterating