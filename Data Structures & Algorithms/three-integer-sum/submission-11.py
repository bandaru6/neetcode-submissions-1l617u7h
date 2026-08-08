class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sort = sorted(nums)
        res = []
        for x in range(len(nums)):

            if x > 0 and sort[x] == sort[x - 1]:
                continue
            r = len(nums) - 1
            l = x + 1
            while l < len(nums):
                if l >= r:
                    break
                if sort[x] + sort[l] + sort[r] > 0:
                    r -= 1
                elif sort[x] + sort[l] + sort[r] < 0:
                    l += 1
                else:

                    res.append([sort[x], sort[l], sort[r]])
                    l += 1
                    while l < len(nums) and sort[l] == sort[l-1]:
                        l += 1

        return res
