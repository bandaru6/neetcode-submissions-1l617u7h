class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        
        l = 0
        ans = 0

        maxD = deque()
        minD = deque()

        for r in range(len(nums)):
            while maxD and nums[maxD[-1]] < nums[r]:
                maxD.pop()
            
            maxD.append(r)

            while minD and nums[minD[-1]] > nums[r]:
                minD.pop()
            minD.append(r)

            while nums[maxD[0]] - nums[minD[0]] > limit:
                if maxD[0] == l:
                    maxD.popleft()
                if minD[0] == l:
                    minD.popleft()
                l += 1
            ans = max(ans, r - l + 1)

        return ans 




