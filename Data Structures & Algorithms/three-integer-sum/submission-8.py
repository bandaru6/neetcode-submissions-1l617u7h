class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sort = sorted(nums)
        res = []
        for x in range(len(nums)):
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
                    if [sort[x], sort[l], sort[r]] not in res:
                        res.append([sort[x], sort[l], sort[r]])
                    l += 1

        return res
