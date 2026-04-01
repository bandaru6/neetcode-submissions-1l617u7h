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

            temp = list(flights[src])
            for dst in temp:
                res.append(dst)
                flights[src].remove(dst)
                if dfs(dst):
                    return True
                res.pop()
                flights[src].append(dst)
            
            return False
        
        dfs("JFK")
        return res