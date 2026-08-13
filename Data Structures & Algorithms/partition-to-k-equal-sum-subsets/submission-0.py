class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total = sum(nums)
        setsize = total / k

        if setsize % 1 != 0:
            return False

        memo = {}

        def dfs(sets, cap, used):

            if sets == 1:
                return True

            if (sets, cap, used) in memo:
                return memo[(sets, cap, used)]

            take = False
            for x in range(len(nums)):

                if list(used)[x] == True:
                    continue
                if nums[x] == cap:
                    temp = list(used)
                    temp[x] = True
                    take = take or dfs(sets - 1, setsize, tuple(temp))
                elif nums[x] < cap:
                    temp = list(used)
                    temp[x] = True
                    
                    take = take or dfs(sets, cap - nums[x], tuple(temp))
            
            memo[(sets, cap, used)] = take

            return memo[(sets, cap, used)]

        return dfs(k, setsize, tuple((False for x in range(len(nums)))))







