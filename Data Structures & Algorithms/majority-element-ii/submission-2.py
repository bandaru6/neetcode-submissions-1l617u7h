class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        third = math.floor(len(nums) / 3)
        res = [[], [], []]
        count = [0, 0, 0]

        for num in nums:
            
            if count[0] == 0 and num not in res:
                res[0] = num
                count[0] += 1
                continue
            if count[1] == 0 and num not in res:
                res[1] = num
                count[1] += 1
                continue
            if count[2] == 0 and num not in res:
                res[2] = num
                count[2] += 1
                continue
            if num in res:
                count[res.index(num)] += 1
            else:
                count[count.index(min(count))] -= 1
                if count[count.index(min(count))] == 0:
                    res[count.index(min(count))] = num
                    count[count.index(min(count))] = 1
        print(res)
        print(count)
        ret = []
        for index, value in enumerate(res):
            if (count[index] > third):
                
                ret.append(value)

        return ret



