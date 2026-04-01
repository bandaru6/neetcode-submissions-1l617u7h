from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort()

        flights = defaultdict(list)

        for src, dst in tickets:
            flights[src].append(dst)
        
        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in flights:
                return False

            temp = list(flights[src])
            for i, dst in enumerate(temp):
                res.append(dst)
                flights[src].pop(i)
                if dfs(dst):
                    return True
                res.pop()
                flights[src].insert(i, dst)
            
            return False
        
        dfs("JFK")
        return res