class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        nums.sort(reverse=True)
        
        total = sum(nums)
        
        if total % k != 0:
            return False

        setsize = total // k
        
        if nums[0] > setsize:
            return False
        memo = {}

        def dfs(sets, cap, used):

            if sets == 1:
                return True

            if (sets, cap, used) in memo:
                return memo[(sets, cap, used)]

            take = False
            for x in range(len(nums)):

                if used[x] == True:
                    continue
                if nums[x] == cap:
                    temp = list(used)
                    temp[x] = True
                    if dfs(sets - 1, setsize, tuple(temp)):
                        memo[(sets, cap, used)] = True
                        return True
                elif nums[x] < cap:
                    temp = list(used)
                    temp[x] = True
                    if dfs(sets, cap - nums[x], tuple(temp)):
                        memo[(sets, cap, used)] = True
                        return True
            
            memo[(sets, cap, used)] = False

            return memo[(sets, cap, used)]

        return dfs(k, setsize, tuple((False for x in range(len(nums)))))







