class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergesort(arr):
            
            if len(arr) <= 1:
                return arr

            
            mid = len(arr) // 2
            left, right = mergesort(arr[:mid]), mergesort(arr[mid:])

            res = []
            i = j = 0

            while i < len(left) and j < len(right):
                
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            res = res + (left[i:] if i < j else right[j:])

            return res
        
        return mergesort(nums)