class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people = sorted(people)
        print(people)
        boats, l, r = 0,0, len(people) - 1

        while l <= r:
            weight = people[l] + people[r]
            if weight > limit:
                boats += 1
                r -= 1
            else:
                boats += 1
                l += 1
                r -= 1
        
        return boats