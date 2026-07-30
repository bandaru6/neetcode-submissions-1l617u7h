class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums
        """
        l = 0
        r = len(nums) - 1
        
        i = 0
        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m 
            else:
                r -= 1
        print(m)
        arr1 = []
        arr2 = []
        if target <= nums[m]:
            arr1 = nums[:m+1]
        else:
            arr2 = nums[m+1:]

        l = 0
        r = len(arr1) - 1
        while l < r:
            m = (l + r) // 2
            print(arr1[m])
            if arr1[m] < target:
                l = m + 1
            elif arr1[m] > target:
                r = m 
            else:
                return True
        
        l = 0
        r = len(arr2) - 1
        while l < r:
            m = (l + r) // 2
            print(arr2[m])
            if arr2[m] < target:
                l = m + 1
            elif arr2[m] > target:
                r = m 
            else:
                return True

        return False
            """

