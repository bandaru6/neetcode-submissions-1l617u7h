class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        intervals = sorted(zip(startTime, endTime, profit)) 

        memo = {}

        def dfs(i):
            if i >= len(intervals):
                return 0
            if i in memo:
                return memo[i]

            def binarySearch(i):
                target = intervals[i][1]
                l = i + 1
                r = len(intervals) - 1

                while l <= r:
                    mid = (l + r) // 2
                    
                    if intervals[mid][0] >= target:
                        r = mid - 1
                    else:
                        l = mid + 1
                return l

            """j = i + 1
            while j < len(intervals):
                if intervals[i][1] <= intervals[j][0]:
                    break
                j += 1
            """
            res = max(dfs(i + 1), dfs(binarySearch(i)) + intervals[i][2])

            memo[i] = res

            return memo[i] 

        
        return dfs(0)
            
            