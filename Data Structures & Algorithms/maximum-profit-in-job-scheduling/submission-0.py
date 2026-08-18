class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        intervals = sorted(zip(startTime, endTime, profit)) 

        memo = {}

        def dfs(i):
            if i >= len(intervals):
                return 0
            if i in memo:
                return memo[i]
            j = i + 1
            while j < len(intervals):
                if intervals[i][1] <= intervals[j][0]:
                    break
                j += 1
            res = max(dfs(i + 1), dfs(j) + intervals[i][2])

            memo[i] = res

            return memo[i] 

        
        return dfs(0)
            
            