class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))
        
        def bfs():
            q = deque()

            q.append((src, 0, 0))

            cheapest = 10e9

            best = {(src, 0): 0}

            #visited = set()
            while q:
                curr = q.popleft()

                if curr[2] > k + 1:
                    continue

                if curr[0] == dst:
                    cheapest = min(cheapest, curr[1])
                    continue

                for nei, cost in adj[curr[0]]:

                    if (nei, curr[2] + 1) not in best or cost+curr[1] < best[(nei, curr[2] + 1)]:
                        best[(nei, curr[2] + 1)] = cost+curr[1]
                        q.append((nei, cost+curr[1], curr[2] + 1))

                
            
            return cheapest if cheapest != 10e9 else -1
        
        return bfs()
                    
        



